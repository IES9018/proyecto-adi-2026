# ADR-009: Estrategia de Despliegue y Gestión de Recursos

- **Estado**: Aceptado
- **Fecha**: 2026-09-04
- **Decisores**: Equipo de desarrollo IES 9-018
- **Referencias**: ADR-005 (Despliegue Docker), ADR-008 (Testing)

## Contexto
El sistema de gobernanza digital se despliega en un servidor Debian 12 compartido con otros servicios (AdGuard Home, Netdata, Nextcloud). La memoria total disponible es 5.8GB, con un uso actual de ~4.2GB. Se requiere garantizar la estabilidad del servidor sin comprometer el rendimiento de otros servicios críticos.

## Decisión

### 1. Segregación de Entornos
Se crean archivos `.env` separados para cada entorno:
- `.env` - Desarrollo (variables por defecto, `ENVIRONMENT=development`)
- `.env.testing` - Testing (rate limiting deshabilitado)
- `.env.production` - Producción (secrets generados, `ENVIRONMENT=production`)

### 2. Límites de Recursos Docker
Se implementan límites de memoria en `docker-compose.prod.yml`:

| Servicio | Límite | Reserva | Justificación |
|----------|--------|---------|---------------|
| nginx | 128MB | 64MB | Reverse proxy ligero |
| frontend | 128MB | 64MB | SPA estática |
| backend | 512MB | 256MB | FastAPI + lógica de negocio |
| postgres | 1GB | 512MB | Base de datos relacional |
| **Total** | **1.76GB** | **912MB** | ~30% de RAM disponible |

### 3. Seguridad de Secretos
- Archivos `.env` en `.gitignore` (nunca se commitean)
- Permisos `600` (solo root puede leer)
- Secrets generados con `openssl rand -hex`

## Consecuencias
- **Positivas**: 
  - Previene que un contenedor consuma toda la RAM del servidor
  - Separación clara entre entornos
  - Fácil rollback a versión anterior
- **Negativas**: 
  - Requiere mantener múltiples archivos `.env`
  - Los límites pueden ser ajustados según necesidades futuras

## Notas de Implementación
- Para desplegar en producción: `docker compose -f docker-compose.prod.yml --env-file .env.production up -d`
- Para verificar límites: `docker stats`
- Para ajustar límites: Editar `docker-compose.prod.yml` y ejecutar `docker compose -f docker-compose.prod.yml up -d`
