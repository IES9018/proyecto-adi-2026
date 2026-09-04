import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { CatalogoPage } from "./pages/CatalogoPage";
import { SolicitudPage } from "./pages/SolicitudPage";

function HomePage() {
  return (
    <div style={{ textAlign: "center", padding: "4rem 2rem", fontFamily: "system-ui" }}>
      <h1>Gobernanza de Servicios Digitales</h1>
      <h2>IES 9-018 — Gobernador Celso Jaque</h2>
      <div style={{ marginTop: "2rem", display: "flex", gap: "1rem", justifyContent: "center" }}>
        <a href="/catalogo" style={{ padding: "0.75rem 1.5rem", background: "#2563eb", color: "white", borderRadius: "0.5rem", textDecoration: "none" }}>Ver Catálogo</a>
        <a href="/solicitudes/nueva" style={{ padding: "0.75rem 1.5rem", background: "#059669", color: "white", borderRadius: "0.5rem", textDecoration: "none" }}>Nueva Solicitud</a>
      </div>
    </div>
  );
}

createRoot(document.getElementById("root")!).render(
  <StrictMode><BrowserRouter><Routes>
    <Route path="/" element={<HomePage />} />
    <Route path="/catalogo" element={<CatalogoPage />} />
    <Route path="/solicitudes/nueva" element={<SolicitudPage />} />
  </Routes></BrowserRouter></StrictMode>
);
