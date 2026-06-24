"""Casos de uso del dominio de solicitudes de alojamiento.

Implementa la lógica de negocio de crear solicitudes, evaluar técnicamente
y emitir resoluciones. Reciben los repositorios por inyección de dependencia
y validan reglas de negocio antes de persistir.
"""

import uuid
from datetime import datetime, timezone

from src.domain.models import (
    Solicitud,
    EvaluacionTecnica,
    Resolucion,
    EstadoSolicitud,
    DictamenTecnico,
    DecisionResolucion,
)
from src.domain.ports import SolicitudRepository


def _ahora() -> datetime:
    """Fecha/hora actual en UTC."""
    return datetime.now(timezone.utc)


class CrearSolicitud:
    """Caso de uso: Crear una nueva solicitud de alojamiento.

    Valida que los campos obligatorios estén presentes y que el nivel
    esté en el rango 1-3. La solicitud se crea en estado PENDIENTE_TECNICA
    para que pase directamente a evaluación.
    """

    def __init__(self, repo: SolicitudRepository) -> None:
        """Inyecta el repositorio de solicitudes.

        Args:
            repo: Implementación concreta de SolicitudRepository.
        """
        self.repo = repo

    def ejecutar(self, datos: dict, solicitante_email: str) -> Solicitud:
        """Crea y persiste una nueva solicitud.

        Args:
            datos: Diccionario con los campos del formulario de solicitud.
            solicitante_email: Email del usuario autenticado que crea la solicitud.

        Returns:
            La solicitud creada con su ID asignado.

        Raises:
            ValueError: Si faltan campos obligatorios o el nivel es inválido.
        """
        # ── Validar campos obligatorios ──────────────────────────────────
        obligatorios = [
            "proyecto", "nivel", "subdominio", "descripcion",
            "objetivo_educativo", "arquitectura", "url_repositorio",
            "licencia", "lenguajes", "base_datos",
        ]
        for campo in obligatorios:
            if not datos.get(campo):
                raise ValueError(f"El campo '{campo}' es obligatorio.")

        nivel = datos.get("nivel")
        if nivel not in (1, 2, 3):
            raise ValueError("El nivel debe ser 1, 2 o 3.")

        # ── Construir entidad de dominio ─────────────────────────────────
        ahora = _ahora()
        solicitud = Solicitud(
            id=str(uuid.uuid4()),
            proyecto=datos["proyecto"],
            nivel=nivel,
            subdominio=datos["subdominio"],
            descripcion=datos["descripcion"],
            objetivo_educativo=datos["objetivo_educativo"],
            arquitectura=datos["arquitectura"],
            justificacion_arquitectura=datos.get("justificacion_arquitectura"),
            patron_diseno=datos.get("patron_diseno"),
            url_repositorio=datos["url_repositorio"],
            licencia=datos["licencia"],
            lenguajes=datos["lenguajes"],
            frameworks=datos.get("frameworks"),
            base_datos=datos["base_datos"],
            puertos=datos.get("puertos"),
            acceso_publico=datos.get("acceso_publico", False),
            autenticacion=datos.get("autenticacion"),
            roles_usuario=datos.get("roles_usuario"),
            datos_personales=datos.get("datos_personales", False),
            contenido_usuarios=datos.get("contenido_usuarios", False),
            estado=EstadoSolicitud.PENDIENTE_TECNICA,
            solicitante_email=solicitante_email,
            creada_en=ahora,
            actualizada_en=ahora,
        )

        return self.repo.guardar(solicitud)


class EvaluarTecnicamente:
    """Caso de uso: Evaluar técnicamente una solicitud.

    Solo puede ejecutarse si la solicitud está en estado PENDIENTE_TECNICA.
    Calcula el dictamen automáticamente a partir del checklist de 10 ítems:
      - 10/10 → APTO
      - 7-9/10 → CONDICIONAL
      - 0-6/10 → NO_APTO

    Si el dictamen es NO_APTO, la solicitud pasa a RECHAZADA.
    En caso contrario, pasa a PENDIENTE_INSTITUCIONAL.
    """

    def __init__(self, repo: SolicitudRepository) -> None:
        self.repo = repo

    def ejecutar(
        self,
        solicitud_id: str,
        checklist: dict,
        observaciones: str | None,
        evaluador_email: str,
    ) -> EvaluacionTecnica:
        """Ejecuta la evaluación técnica de una solicitud.

        Args:
            solicitud_id: ID de la solicitud a evaluar.
            checklist: Diccionario con los 10 ítems (bool o None).
            observaciones: Observaciones textuales del evaluador.
            evaluador_email: Email del admin técnico que evalúa.

        Returns:
            La evaluación técnica creada.

        Raises:
            ValueError: Si la solicitud no existe o no está en el estado correcto.
        """
        solicitud = self.repo.buscar_por_id(solicitud_id)
        if not solicitud:
            raise ValueError(f"No existe la solicitud con ID {solicitud_id}.")

        if solicitud.estado != EstadoSolicitud.PENDIENTE_TECNICA:
            raise ValueError(
                f"La solicitud debe estar en estado PENDIENTE_TECNICA, "
                f"pero está en {solicitud.estado.value}."
            )

        # ── Calcular dictamen ────────────────────────────────────────────
        items_clave = [
            "repo_publico", "licencia_compatible", "https_configurado",
            "hash_contrasenas", "vars_entorno", "puerto_localhost",
            "headers_seguridad", "dockerizado", "logs_configurados",
            "backup_definido",
        ]
        cumplidos = sum(1 for k in items_clave if checklist.get(k))
        total = len(items_clave)

        if cumplidos == total:
            dictamen = DictamenTecnico.APTO
        elif cumplidos >= 7:
            dictamen = DictamenTecnico.CONDICIONAL
        else:
            dictamen = DictamenTecnico.NO_APTO

        # ── Crear evaluación ─────────────────────────────────────────────
        evaluacion = EvaluacionTecnica(
            id=str(uuid.uuid4()),
            solicitud_id=solicitud_id,
            evaluador_email=evaluador_email,
            **{k: checklist.get(k) for k in items_clave},
            dictamen=dictamen,
            observaciones=observaciones,
            fecha=_ahora(),
        )

        evaluacion = self.repo.guardar_evaluacion_tecnica(evaluacion)

        # ── Actualizar estado ────────────────────────────────────────────
        if dictamen == DictamenTecnico.NO_APTO:
            self.repo.actualizar_estado(solicitud_id, EstadoSolicitud.RECHAZADA)
        else:
            self.repo.actualizar_estado(
                solicitud_id, EstadoSolicitud.PENDIENTE_INSTITUCIONAL
            )

        return evaluacion


class EmitirResolucion:
    """Caso de uso: Emitir una resolución final sobre una solicitud.

    Solo puede ejecutarse si la solicitud está en estado
    PENDIENTE_INSTITUCIONAL. La resolución aprueba o rechaza definitivamente.
    """

    def __init__(self, repo: SolicitudRepository) -> None:
        self.repo = repo

    def ejecutar(
        self,
        solicitud_id: str,
        decision: str,
        fundamentos: str,
        condiciones: str | None,
        evaluador_email: str,
    ) -> Resolucion:
        """Emite la resolución final de una solicitud.

        Args:
            solicitud_id: ID de la solicitud.
            decision: "aprobada" o "rechazada".
            fundamentos: Texto que justifica la decisión.
            condiciones: Condiciones adicionales (opcional).
            evaluador_email: Email del directivo que resuelve.

        Returns:
            La resolución creada.

        Raises:
            ValueError: Si la solicitud no existe, no está en el estado correcto,
                        o la decisión es inválida.
        """
        solicitud = self.repo.buscar_por_id(solicitud_id)
        if not solicitud:
            raise ValueError(f"No existe la solicitud con ID {solicitud_id}.")

        if solicitud.estado != EstadoSolicitud.PENDIENTE_INSTITUCIONAL:
            raise ValueError(
                f"La solicitud debe estar en estado PENDIENTE_INSTITUCIONAL, "
                f"pero está en {solicitud.estado.value}."
            )

        if decision not in ("aprobada", "rechazada"):
            raise ValueError("La decisión debe ser 'aprobada' o 'rechazada'.")

        decision_enum = DecisionResolucion(decision)

        # Generar número de resolución
        prefijo = _ahora().strftime("%Y%m%d")
        numero = f"RES-{prefijo}-{solicitud_id[:8].upper()}"

        resolucion = Resolucion(
            id=str(uuid.uuid4()),
            solicitud_id=solicitud_id,
            numero=numero,
            decision=decision_enum,
            fundamentos=fundamentos,
            condiciones=condiciones,
            fecha=_ahora(),
        )

        resolucion = self.repo.guardar_resolucion(resolucion)

        # Actualizar estado de la solicitud
        nuevo_estado = (
            EstadoSolicitud.APROBADA
            if decision_enum == DecisionResolucion.APROBADA
            else EstadoSolicitud.RECHAZADA
        )
        self.repo.actualizar_estado(solicitud_id, nuevo_estado)

        return resolucion
