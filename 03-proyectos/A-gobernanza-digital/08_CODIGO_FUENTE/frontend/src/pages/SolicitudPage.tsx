import { useState, FormEvent } from "react";
import { useNavigate } from "react-router-dom";

export function SolicitudPage() {
  const navigate = useNavigate();
  const [form, setForm] = useState({
    proyecto: "",
    nivel: 1,
    subdominio: "",
    descripcion: "",
    objetivo_educativo: "",
    arquitectura: "hexagonal",
    url_repositorio: "",
    licencia: "MIT",
    lenguajes: "",
    frameworks: "",
    base_datos: "PostgreSQL",
  });

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    const res = await fetch("/api/solicitudes", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form),
    });
    if (res.ok) navigate("/panel/solicitante");
  };

  return (
    <form className="form-solicitud" onSubmit={handleSubmit}>
      <h2>Nueva Solicitud</h2>
      <label>Nombre del proyecto</label>
      <input value={form.proyecto} onChange={(e) => setForm({ ...form, proyecto: e.target.value })} required />
      <label>Nivel</label>
      <select value={form.nivel} onChange={(e) => setForm({ ...form, nivel: Number(e.target.value) })}>
        <option value={1}>Nivel 1 — Experimental</option>
        <option value={2}>Nivel 2 — Institucional</option>
        <option value={3}>Nivel 3 — Público</option>
      </select>
      <label>Subdominio</label>
      <input value={form.subdominio} onChange={(e) => setForm({ ...form, subdominio: e.target.value })} required />
      <label>Descripción</label>
      <textarea value={form.descripcion} onChange={(e) => setForm({ ...form, descripcion: e.target.value })} required />
      <label>Arquitectura</label>
      <select value={form.arquitectura} onChange={(e) => setForm({ ...form, arquitectura: e.target.value })}>
        <option value="monolitica">Monolítica</option>
        <option value="capas">Capas</option>
        <option value="hexagonal">Hexagonal</option>
        <option value="microservicios">Microservicios</option>
      </select>
      <label>URL Repositorio</label>
      <input value={form.url_repositorio} onChange={(e) => setForm({ ...form, url_repositorio: e.target.value })} required />
      <button type="button" onClick={() => navigate("/panel/solicitante")}>Cancelar</button>
      <button type="submit">Enviar Solicitud</button>
    </form>
  );
}
