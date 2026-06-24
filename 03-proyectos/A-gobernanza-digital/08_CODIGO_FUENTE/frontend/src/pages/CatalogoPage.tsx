import { useState, useEffect } from "react";

interface Solicitud {
  id: string;
  proyecto: string;
  nivel: number;
  subdominio: string;
  descripcion: string;
  estado: string;
  creada_en: string;
}

export function CatalogoPage() {
  const [servicios, setServicios] = useState<Solicitud[]>([]);
  const [nivel, setNivel] = useState<number | null>(null);
  const [busqueda, setBusqueda] = useState("");

  useEffect(() => {
    const params = new URLSearchParams();
    if (nivel) params.set("nivel", String(nivel));
    if (busqueda) params.set("q", busqueda);
    fetch(`/api/catalogo?${params}`)
      .then((r) => r.json())
      .then(setServicios);
  }, [nivel, busqueda]);

  return (
    <div className="catalogo">
      <h1>Servicios Digitales Activos — IES 9-018</h1>
      <div className="filtros">
        <select value={nivel ?? ""} onChange={(e) => setNivel(e.target.value ? Number(e.target.value) : null)}>
          <option value="">Todos los niveles</option>
          <option value="1">Nivel 1 — Experimental</option>
          <option value="2">Nivel 2 — Institucional</option>
          <option value="3">Nivel 3 — Público</option>
        </select>
        <input placeholder="Buscar..." value={busqueda} onChange={(e) => setBusqueda(e.target.value)} />
      </div>
      {servicios.length === 0 && <p>No hay servicios activos en este momento.</p>}
      {servicios.map((s) => (
        <div key={s.id} className="card">
          <h3>{s.proyecto}</h3>
          <span className="nivel">Nivel {s.nivel}</span>
          <p>{s.descripcion}</p>
          <small>Aprobado: {new Date(s.creada_en).toLocaleDateString("es-AR")}</small>
        </div>
      ))}
    </div>
  );
}
