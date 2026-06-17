### 🏫 **Institución:** IES 9-018 "Gobernador Celso Jaque"
### 📚 **Carrera:** Tecnicatura Superior en Desarrollo de Software
### 📖 **Materia:** Arquitectura y Diseño de Interfaces
### 👨‍🏫 **Profesor:** Paulo Alvarez
### 📅 **Año:** 2026 | **Curso:** 3° AÑO

---

# Patrones de Diseño de Software

## La Analogía de la Receta de Cocina

Imaginá que querés cocinar salsa bolognesa. No arrancás desde cero probando mezclas. Buscás una **receta**: tomate, carne, cebolla, ajo, cocción lenta dos horas. La receta es el patrón.

Los patrones de diseño son **recetas probadas** para problemas comunes de software. No son código copiable, son ideas que adaptás a tu contexto.

---

## Patrón MVC (Modelo-Vista-Controlador)

El más famoso de todos. Separa tu aplicación en 3 capas.

| Capa | ¿Qué hace? | Analogía del restaurante |
|:-----|:-----------|:--------------------------|
| **Modelo** | Datos y lógica de negocio | La cocina: prepara la comida |
| **Vista** | Interfaz de usuario | El plato servido: lo que ve el cliente |
| **Controlador** | Coordina peticiones | El mozo: toma el pedido, lo lleva a cocina, trae el plato |

**Ejemplo real:** Pedís `GET /usuarios` (Controlador recibe), busca en DB (Modelo), devuelve HTML (Vista).

**¿Dónde se usa?** Rails, Laravel, Django, Spring, Next.js.

---

## Patrón de Capas (Layered Architecture)

Organiza el código en niveles verticales. Cada capa solo habla con la de abajo.

```
[Interfaz de Usuario]
       ↓
[Lógica de Aplicación]   ← cada capa solo usa la de abajo
       ↓
[Lógica de Negocio]
       ↓
[Acceso a Datos]
```

**Analogía:** Un edificio de oficinas. El 5to piso (RRHH) no necesita saber cómo funciona el ascensor, solo que lo lleva al 1er piso (Recepción). Cada piso tiene su función y no salta al sótano.

**Ventaja:** Podés cambiar la base de datos sin tocar la interfaz.
**Desventaja:** Si tenés muchas capas, puede volverse lento.

---

## Arquitectura Hexagonal (Ports & Adapters)

Creada por Alistair Cockburn. El núcleo (lógica de negocio) no sabe nada del mundo exterior.

```
[Web]  ──→ [Adaptador Web] ──→ |         | ←── [Adaptador DB] ←── [PostgreSQL]
[CLI]  ──→ [Adaptador CLI] ──→ | NÚCLEO  | ←── [Adaptador API] ←── [Servicio Externo]
[Test] ──→ [Adaptador Test] ── |         |
```

**Analogía del cargador USB-C:** Tu celular (núcleo) no sabe si está enchufado a la pared, a la compu o a una batería externa. Solo sabe que recibe electricidad por el puerto USB-C (el puerto es la interfaz, cada enchufe es un adaptador distinto).

**¿Para qué sirve?** Para poder cambiar cualquier cosa exterior sin tocar la lógica de negocio. Querés pasar de SQLite a PostgreSQL? Creás un nuevo adaptador y listo.

---

## Patrón Repository

Actúa como si fuera una "colección de objetos" en memoria, pero por detrás habla con la base de datos.

```python
# Sin Repository: mezclás lógica con SQL
def buscar_usuarios_activos():
    return db.query("SELECT * FROM usuarios WHERE activo = 1")

# Con Repository: tratás la DB como si fuera una lista
def buscar_usuarios_activos():
    return usuario_repo.find_by_activo(True)
```

**Analogía:** Llamás a la biblioteca y decís "¿tienen el libro 'Cien Años de Soledad'?" No te importa si el bibliotecario busca en el estante A, en el depósito o lo pide a otra sucursal. Solo querés el libro.

---

## Patrón Observer (Observador)

Un objeto (sujeto) notifica a otros (observadores) cuando algo cambia, sin que estén acoplados.

**Analogía:** Es como suscribirte a un canal de YouTube. No llamás al youtuber cada 5 minutos preguntando "¿ya subiste video?". Te suscribís, y cuando él sube algo, YouTube te avisa.

**Ejemplo real:** En un sistema de e-commerce, cuando se confirma una compra (sujeto), se notifican: servicio de emails, servicio de inventario, servicio de facturación (observadores).

---

## Patrón Singleton

Garantiza que una clase tenga **una sola instancia** en toda la aplicación.

**Analogía:** El presidente de un país. Solo hay uno a la vez. No podés crear "otro presidente". Si intentás, te da el mismo que ya existe.

**¿Dónde se usa?** Conexiones a base de datos, configuraciones globales, logger.

**Precaución:** Útil pero no abuses. Muchos singletons es señal de que algo está mal diseñado.

---

## Patrón Strategy

Te permite cambiar el comportamiento de un objeto en tiempo de ejecución intercambiando algoritmos.

**Analogía:** Una app de mapas. Para ir del punto A al B podés elegir "ruta más rápida", "ruta más corta" o "evitar autopistas". Cada estrategia es un algoritmo distinto, pero la app (el contexto) funciona igual.

```python
class CalculadoraPrecio:
    def __init__(self, estrategia):
        self.estrategia = estrategia  # Estrategia se puede cambiar

    def calcular(self, base):
        return self.estrategia(base)

# Uso:
calc = CalculadoraPrecio(estrategia_descuento_estudiante)
calc.calcular(100)  # Aplica descuento estudiante

calc.estrategia = estrategia_descuento_black_friday
calc.calcular(100)  # Aplica descuento Black Friday
```

---

## Cómo Elegir un Patrón

No hay "el mejor patrón". Hay el **más adecuado para tu problema**.

| Si tenés... | Considerá... |
|:-------------|:--------------|
| Muchas capas que dependen entre sí | **Arquitectura Hexagonal** para desacoplar |
| Una interfaz que cambia seguido | **MVC** para separar vistas del negocio |
| Varios algoritmos intercambiables | **Strategy** para poder cambiar en caliente |
| Un recurso compartido (DB, config) | **Singleton** para una única instancia |
| Muchos objetos que dependen de cambios | **Observer** para desacoplar notificaciones |
| Acceso a datos que querés abstraer | **Repository** para ocultar la complejidad de la DB |

---

## Para Recordar

> Los patrones no se imponen, se **descubren** cuando entendés el problema.
> Si forzás un patrón donde no aplica, empeorás el diseño.
> El andamiaje de agentes IA te va a **proponer patrones**. Tu trabajo es entender por qué y decidir si corresponde.

**Referencia recomendada:** [Refactoring Guru - Design Patterns](https://refactoring.guru/es/design-patterns): explicaciones visuales, con ejemplos en múltiples lenguajes.
