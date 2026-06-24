# Guía de Deploy — Servidor Escolar

**Agente:** Tech Lead | **Destino:** Debian 12, Docker, Nginx, Cloudflare, Tailscale

---

## Arquitectura de deploy

```
Internet → Cloudflare DNS → Servidor Debian 12 → Nginx :80/:443
                                                    ├── Frontend :3000 (React)
                                                    └── Backend :8000 (FastAPI) → PostgreSQL :5432
```

---

## Paso 1: Preparar el servidor

```bash
# Conectarse por SSH (Tailscale)
ssh admin@100.x.x.x

# Clonar el fork institucional del proyecto
cd /opt/escuela
git clone https://github.com/IES9018/gobernanza-digital.git
cd gobernanza-digital
```

---

## Paso 2: Configurar variables de entorno

```bash
cp .env.example .env
# Editar .env con valores reales:
nano .env
```

```env
DATABASE_URL=postgresql://gobernanza:REEMPLAZAR@postgres:5432/gobernanza
SECRET_KEY=REEMPLAZAR-CON-SECRETO-SEGURO
ENVIRONMENT=production
SMTP_HOST=smtp.institucional.edu.ar
SMTP_PORT=587
DB_PASSWORD=REEMPLAZAR
```

---

## Paso 3: Configurar Nginx

```nginx
server {
    listen 80;
    server_name gobernanzadigital.ies9018malargue.edu.ar;

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /api/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

```bash
sudo ln -s /opt/escuela/gobernanza-digital/nginx.conf /etc/nginx/sites-enabled/gobernanza
sudo nginx -t
sudo systemctl reload nginx
```

---

## Paso 4: Levantar los servicios

```bash
docker compose up -d
docker compose ps  # Verificar que todo esté corriendo
```

---

## Paso 5: Configurar Cloudflare

1. Agregar registro A: `gobernanzadigital` → IP del servidor
2. Activar proxy (nube naranja) para protección DDoS básica
3. Configurar SSL/TLS: Full (strict)

**Solo el admin técnico tiene acceso a Cloudflare.**

---

## Paso 6: Verificar

```bash
# Probar backend
curl https://gobernanzadigital.ies9018malargue.edu.ar/api/health

# Probar frontend
curl -I https://gobernanzadigital.ies9018malargue.edu.ar
```

---

## Rollback

```bash
git checkout <commit-anterior>
docker compose up -d --build
```

---

## 🧠 Analogía del @docente

> Deployar es como **abrir un local al público**. Durante meses construiste en tu taller (desarrollo). Ahora ponés todo en cajas (Docker), lo llevás al local (servidor), lo desempacás, conectás la electricidad (Nginx), el gas (PostgreSQL), colgás el cartel (DNS) y abrís la persiana. Si algo no funciona, tenés el número del electricista (rollback).
