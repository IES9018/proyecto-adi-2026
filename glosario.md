# Glosario del curso (inglés → castellano)

Términos que aparecen en los TPs en inglés o como siglas. Cada uno con una frase corta para no frenar la lectura.

- **RF** = Requisito Funcional. Qué debe *hacer* el sistema ("el sistema permite…").
- **RNF** = Requisito No Funcional. Restricción de calidad (rendimiento, seguridad, accesibilidad).
- **SPEC** = Especificación. El documento `SPEC.md` que define qué vas a construir.
- **ADR** = Architecture Decision Record (Registro de Decisión de Arquitectura). Por qué elegiste X sobre Y.
- **Non-Goal** = Fuera de alcance. Lo que decidís explícitamente NO construir en esta etapa.
- **Mermaid** = Lenguaje de diagramas en texto (Markdown) que GitHub dibuja solo.
- **diff / diffable** = Diferenciable. Que se puede comparar versión a versión, igual que el código.
- **OpenAPI** = Formato estándar para describir una API (sus endpoints, parámetros y respuestas).
- **API** = Application Programming Interface. El contrato por el que dos programas se hablan.
- **REST** = Estilo de API sobre HTTP (la más común; usa GET/POST/etc.).
- **GraphQL** = Alternativa a REST: en vez de varios endpoints, usás un schema (SDL) con una sola consulta.
- **SDL** = Schema Definition Language. El lenguaje en que se escribe el schema de GraphQL.
- **JWT** = JSON Web Token. Token firmado que identifica y autentica a un usuario en una API.
- **SPA** = Single Page Application. Web que corre toda del lado del navegador (ej. React).
- **SSR** = Server Side Rendering. La página se genera en el servidor (mejor para SEO y primer render).
- **MPA** = Multi Page Application. Web tradicional, una página por URL.
- **PWA** = Progressive Web App. Sitio web que se comporta como app (instalable, funciona offline).
- **CI** = Integración Continua. Pipeline que prueba tu código automáticamente en cada cambio.
- **CD** = Entrega Continua. Automatiza el paso a producción después de la CI.
- **STRIDE** = Modelo de amenazas: **S**poofing (suplantación), **T**ampering (manipulación), **R**epudiation (repudio), **I**nfo disclosure (divulgación), **D**oS (denegación), **E**levation (elevación de privilegios).
- **IDOR** = Insecure Direct Object Reference. Falta de control de acceso a objetos por su ID (ej. `/usuario/5` sin permiso).
- **linter / lint** = Herramienta que revisa reglas de estilo y errores en el código automáticamente.
- **LCP** = Largest Contentful Paint. Métrica: tiempo en pintar el elemento más grande (< 2.5 s está bien).
- **INP** = Interaction to Next Paint. Métrica: tiempo de respuesta a la interacción del usuario (< 200 ms está bien).
- **HIG** = Human Interface Guidelines. Guía de diseño de Apple.
- **WCAG** = Web Content Accessibility Guidelines. Norma de accesibilidad web. "AA" es un nivel de cumplimiento.
- **Gherkin** = Formato de texto para criterios de aceptación (Given / When / Then).
- **Nielsen** = Jakob Nielsen, autor de las 10 heurísticas de usabilidad.
- **C4** = Context, Containers, Components, Code. Modelo de 4 niveles para diagramar arquitectura.
- **Changelog** = Registro de cambios versionado (qué cambió y cuándo).
- **supersede** = Reemplazar. Un ADR nuevo *supersede* a uno viejo (no se borra, se marca obsoleto).
- **Postmortem** = Análisis de lo que salió mal para aprender (sin buscar culpables).
- **PR** = Pull Request. Solicitud de cambio que se revisa antes de mergear.
- **self-merge** = Vos misma mergeás tu propio PR (regla de la cátedra).
- **arnés** = `.opencoderules` (o el equivalente de tu herramienta) que limita a tu agente de IA.
- **Keep a Changelog** = Formato estándar de changelog (`[1.0.0] - fecha` con categorías).
