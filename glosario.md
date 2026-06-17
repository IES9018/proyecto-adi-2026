### 🏫 **Institución:** IES 9-018 "Gobernador Celso Jaque"
### 📚 **Carrera:** Tecnicatura Superior en Desarrollo de Software
### 📖 **Materia:** Arquitectura y Diseño de Interfaces
### 👨‍🏫 **Profesor:** Paulo Alvarez
### 📅 **Año:** 2026 | **Curso:** 3° AÑO

---

# Glosario de Arquitectura de Software y Diseño de Interfaces

Este glosario centraliza los términos técnicos que usamos en la materia. Está diseñado para ser una referencia rápida y clara, explicando cada concepto desde cero, con ejemplos concretos y sin asumir conocimiento previo.

---

## Arquitectura de Software

### Arquitectura de Software
- **¿Qué es?** Es la estructura fundamental de un sistema: cómo se organizan sus piezas, cómo se comunican entre sí y qué reglas gobiernan esas interacciones.
- **Analogía:** Es el plano maestro de un edificio. Define dónde va cada cosa (cocina, baños, dormitorios), por dónde pasan los caños y cables, y cómo se conectan los pisos. Sin plano, los albañiles ponen ladrillos sin orden y el edificio se vuelve inhabitable.
- **¿Para qué sirve?** Para que el sistema sea mantenible, escalable y no se derrumbe cuando haya que hacer un cambio.

### Patrón de Diseño (Design Pattern)
- **¿Qué es?** Una solución probada y reutilizable para un problema común de diseño de software. No es código copiable, es una idea que se adapta.
- **Analogía:** Es como una receta de cocina. La receta de "salsa bolognesa" te dice los ingredientes y pasos generales, pero cada cocinero la adapta a su gusto. En software, el patrón MVC te dice cómo separar datos, interfaz y lógica, pero cada proyecto lo implementa distinto.
- **Ejemplos reales:** MVC, Singleton, Observer, Factory, Strategy, Repository.
- **Referencia:** [Refactoring Guru - Design Patterns](https://refactoring.guru/es/design-patterns)

### Arquitectura Hexagonal (Ports & Adapters)
- **¿Qué es?** Un estilo de arquitectura donde la lógica de negocio (el "núcleo") está totalmente aislada del mundo exterior (base de datos, web, APIs). Se comunica con el exterior a través de "puertos" (interfaces) y "adaptadores" (implementaciones concretas).
- **Analogía:** Es como un cargador de celular USB-C. El celular (núcleo) no sabe si está conectado a un enchufe de pared, a una computadora o a una batería portátil. Solo sabe que recibe electricidad por el puerto USB-C. Cada fuente de energía es un "adaptador" distinto, pero el celular no necesita cambiar.
- **¿Para qué sirve?** Para poder cambiar la base de datos, el framework web o el sistema de mensajería sin tocar la lógica de negocio.

### MVC (Modelo-Vista-Controlador)
- **¿Qué es?** Un patrón arquitectónico que separa la aplicación en tres capas: Modelo (datos y lógica), Vista (interfaz de usuario) y Controlador (maneja las peticiones y coordina).
- **Analogía:** Es como un restaurante. El Modelo es la cocina (prepara la comida, maneja ingredientes). La Vista es el plato servido en la mesa (lo que ve el cliente). El Controlador es el mozo (recibe el pedido, lo lleva a cocina, trae el plato a la mesa).
- **¿Dónde se usa?** Ruby on Rails, Laravel, Django, Spring MVC, Next.js (app router).

### C4 Model
- **¿Qué es?** Un método para dibujar la arquitectura de software en 4 niveles de zoom: Contexto (el sistema y su entorno), Contenedores (aplicaciones y bases de datos), Componentes (módulos internos) y Código (clases y funciones).
- **Analogía:** Es como Google Maps. El nivel Contexto es el mapa del país, Contenedores es el mapa de la provincia, Componentes es el mapa de la ciudad, y Código es el Street View de una calle.
- **Referencia:** [c4model.com](https://c4model.com)

### ADR (Architecture Decision Record)
- **¿Qué es?** Un documento corto que registra una decisión arquitectónica importante: qué problema se enfrentó, qué opciones se consideraron, cuál se eligió y por qué, y qué consecuencias trae.
- **Analogía:** Es el acta de una reunión de directorio. No solo dice "se decidió comprar el edificio", sino que explica por qué se compró ESE edificio y no otro, qué alternativas se evaluaron y qué implicancias tiene para el presupuesto.
- **Formato típico:** Título, Contexto, Decisión, Consecuencias.
- **Referencia:** [adr.github.io](https://adr.github.io)

### Monolito vs Microservicios
- **¿Qué es?** Un monolito es una aplicación donde todo el código vive junto y se despliega como una sola unidad. Los microservicios dividen la aplicación en piezas independientes, cada una con su propia base de datos y ciclo de vida.
- **Analogía:** Monolito es un shopping: todas las tiendas están bajo el mismo techo, comparten seguridad y estacionamiento. Microservicios son locales independientes en distintas calles: cada uno tiene su propia llave, alarma y horario. El shopping es más fácil de administrar al principio; los locales independientes escalan mejor cuando crecés.
- **¿Cuál usar?** Para proyectos educativos, **monolito bien modularizado**. Microservicios solo cuando el sistema es tan grande que un solo equipo no puede manejarlo.

### API REST
- **¿Qué es?** Un conjunto de reglas para que dos sistemas se comuniquen por HTTP usando operaciones estándar: GET (leer), POST (crear), PUT (actualizar), DELETE (borrar).
- **Analogía:** Es como el menú de un restaurante. El menú (API) te dice qué platos podés pedir (endpoints), qué ingredientes lleva cada uno (parámetros) y cómo hacés el pedido (método HTTP: GET para ver el menú, POST para ordenar). La cocina (servidor) prepara y entrega sin que vos entres a la cocina.
- **Ejemplo:** `GET /usuarios` devuelve la lista de usuarios. `POST /usuarios` crea uno nuevo.

---

## Diseño de Interfaces

### HCI (Human-Computer Interaction)
- **¿Qué es?** La disciplina que estudia cómo las personas interactúan con las computadoras. Busca diseñar sistemas que sean fáciles, eficientes y placenteros de usar.
- **Analogía:** Es como la ergonomía de una silla de oficina. Un diseñador de sillas estudia la postura humana para que la silla sea cómoda. Un diseñador HCI estudia cómo la gente lee, hace clic y navega para que la interfaz sea intuitiva.
- **¿Para qué sirve?** Para que los usuarios no abandonen tu sistema por frustración.

### UX (User Experience)
- **¿Qué es?** La experiencia completa que tiene una persona al usar un producto: cómo se siente, qué tan fácil le resulta, si logra lo que quiere hacer.
- **Analogía:** No es solo qué tan linda es la puerta del banco (UI), sino qué tan rápido te atienden, si el formulario es claro, si te vas sintiendo que resolviste tu trámite (UX). La UX es el viaje completo.
- **Diferencia clave:** UI es lo que ves (botones, colores, tipografía). UX es lo que sentís al usarlo.

### Wireframe
- **¿Qué es?** Un dibujo esquemático de baja fidelidad que muestra la estructura de una pantalla: dónde va el menú, el contenido, los botones. Sin colores ni detalles visuales.
- **Analogía:** Es el plano de una casa en borrador a lápiz: "acá va la cocina, acá el living, esta pared se puede tirar". No tiene muebles ni decoración. Sirve para discutir la distribución antes de pintar.
- **Herramientas:** Lápiz y papel, Excalidraw, Figma, o el agente IA generando wireframes en Mermaid.

### Mockup
- **¿Qué es?** Una versión visual de alta fidelidad que muestra exactamente cómo se verá la interfaz, con colores, tipografía, imágenes y contenido realista.
- **Analogía:** Es el render 3D que te muestra el arquitecto para venderte el departamento. Ya se ven los muebles, el color de las paredes, la luz. Pero todavía no se puede vivir ahí.

### Responsive Design
- **¿Qué es?** Técnica de diseño web para que una misma página se vea bien en celular, tablet y computadora, adaptando automáticamente su disposición.
- **Analogía:** Es como un líquido que toma la forma del recipiente. El mismo contenido (agua) se adapta a una botella alta, un plato hondo o un vaso ancho. La página se adapta al ancho de la pantalla sin perder contenido.

---

## Metodologías y Herramientas

### Scrum
- **¿Qué es?** Un marco de trabajo ágil para gestionar proyectos en ciclos cortos (sprints) de 1 a 4 semanas. Roles: Product Owner (define qué hacer), Scrum Master (facilita el proceso), Developers (hacen el trabajo).
- **Analogía:** Es como preparar una cena de 10 platos. En lugar de cocinar todo de golpe y servir frío, hacés un plato por vez (sprint), lo servís caliente, pedís feedback ("¿le falta sal?") y ajustás el siguiente plato.
- **¿Para qué sirve?** Para entregar valor rápido, recibir feedback temprano y no esperar al final para descubrir que hiciste cualquier cosa.

### Sprint
- **¿Qué es?** Un ciclo corto de trabajo (1-4 semanas) con un objetivo claro y entregable al final.
- **Analogía:** Es una etapa en una carrera de postas. Cada corredor (sprint) tiene una distancia fija, entrega el testimonio (entregable) y el siguiente sigue.

### CI/CD (Continuous Integration / Continuous Deployment)
- **¿Qué es?** CI: integrar cambios de código frecuentemente y correr tests automáticos para detectar errores rápido. CD: desplegar automáticamente a producción lo que pasó los tests.
- **Analogía:** Es como una línea de montaje en una fábrica. Cada pieza que llega (commit) es revisada automáticamente por control de calidad (tests). Si pasa, se empaqueta y se manda al camión de reparto (deploy). Si falla, la línea se detiene hasta arreglarlo.
- **Herramienta:** GitHub Actions, GitLab CI, Jenkins.

### Docker
- **¿Qué es?** Una herramienta que empaqueta una aplicación y todas sus dependencias en un "contenedor" que corre igual en cualquier computadora.
- **Analogía:** Es como un container de barco. Adentro viaja tu auto exactamente como lo dejaste, sin desarmar. Llega al puerto de destino y sale andando. No importa si el barco es distinto o el puerto es otro: el container es estándar.
- **¿Para qué sirve?** Para que "en mi máquina funciona" deje de ser una excusa.

---

## Trabajo Colaborativo

### Git
- **¿Qué es?** Un sistema de control de versiones que registra cada cambio en tu proyecto como una "foto" (commit) que podés recuperar en cualquier momento.
- **Analogía:** Es como el "historial de versiones" de Google Docs pero muchísimo más potente. Podés volver a cualquier versión anterior, crear ramas alternativas de tu documento, y después fusionarlas sin perder nada.

### Conventional Commits
- **¿Qué es?** Una convención para escribir mensajes de commit con un formato estándar: `tipo: descripción breve`. Tipos: `feat` (funcionalidad nueva), `fix` (corrección), `docs` (documentación), `refactor` (mejora de código).
- **Analogía:** Es como etiquetar cajas en una mudanza: "COCINA: platos", "BAÑO: toallas", "ROPA: invierno". Cuando necesitás encontrar algo, sabés exactamente en qué caja buscar.
- **Referencia:** [conventionalcommits.org](https://www.conventionalcommits.org)

### SemVer (Semantic Versioning)
- **¿Qué es?** Un estándar para numerar versiones de software: `MAJOR.MINOR.PATCH` (ej: `2.1.4`). MAJOR: cambios que rompen compatibilidad. MINOR: funcionalidad nueva sin romper nada. PATCH: correcciones de bugs.
- **Analogía:** Es como las ediciones de un libro. 1° edición, 2° edición (MAJOR, cambió contenido). Reimpresión con erratas corregidas (PATCH). Edición ampliada con nuevo capítulo (MINOR).

### Pull Request (PR)
- **¿Qué es?** Una solicitud formal para que tus cambios en una rama sean revisados y fusionados a la rama principal del proyecto. Es el mecanismo estándar de colaboración en GitHub.
- **Analogía:** Es como entregar un borrador de tu libro al editor. El editor lo lee, sugiere cambios, te lo devuelve. Corregís y lo volvés a entregar. Cuando está aprobado, se publica (merge).
- **¿Para qué sirve?** Para que el código sea revisado antes de entrar al proyecto principal. Nadie escribe directo en `main`.

---

## Agentes IA en Desarrollo de Software

### Andamiaje de Agentes IA
- **¿Qué es?** Un método de trabajo donde usás múltiples prompts de IA con roles especializados (arquitecto, modelador, implementador, verificador) que trabajan en orden, leyendo el output del anterior, bajo tu supervisión.
- **Analogía:** Es como dirigir una obra de teatro. Vos sos el director. Cada agente es un actor con un personaje distinto. El Arquitecto diseña la escenografía, el Modelador define la utilería, el Implementador construye, el Verificador controla que todo funcione. Vos revisás cada acto antes de pasar al siguiente.
- **¿Para qué sirve?** Para que la IA no te entregue un proyecto entero y caótico, sino piezas revisables una por una, manteniendo el control del proceso.

### Prompts
- **¿Qué es?** Instrucciones en lenguaje natural que le das a un modelo de IA para que realice una tarea específica. Un buen prompt define el rol, el objetivo, el formato de salida y las restricciones.
- **Analogía:** Es como un brief que le das a un diseñador gráfico: "Necesito un logo para una cervecería artesanal, estilo rústico, colores tierra, que funcione en blanco y negro, formato PNG y SVG". Cuanto más claro el brief, mejor el resultado.

### Agente (en IA)
- **¿Qué es?** Un prompt especializado que le da a la IA un rol fijo (ej: "Arquitecto de Software") con reglas estrictas sobre lo que puede y no puede hacer, y que trabaja de forma secuencial con otros agentes.
- **Analogía:** Es un empleado con una descripción de puesto muy clara. El Arquitecto no toca código, el Implementador no escribe tests. Cada uno hace lo suyo y le pasa el trabajo al siguiente.

### Mermaid
- **¿Qué es?** Un lenguaje de texto simple para crear diagramas (flujos, secuencias, clases, arquitectura) que se renderizan automáticamente en GitHub, VS Code y otras plataformas.
- **Analogía:** Es como escribir una receta con emojis en lugar de dibujar. En vez de dibujar un diagrama con formas y flechas en una herramienta gráfica, escribís un texto corto que se convierte en diagrama automáticamente.
- **Ejemplo:** `graph LR; A[Cliente] --> B[Servidor]; B --> C[Base de Datos]` se ve como un diagrama de flechas.
- **Referencia:** [mermaid.js.org](https://mermaid.js.org)

---

## Referencias Generales

| Término | Recurso |
|---------|---------|
| Conventional Commits | [conventionalcommits.org](https://www.conventionalcommits.org) |
| Semantic Versioning | [semver.org](https://semver.org) |
| C4 Model | [c4model.com](https://c4model.com) |
| ADR (Architecture Decision Records) | [adr.github.io](https://adr.github.io) |
| Design Patterns | [refactoring.guru/design-patterns](https://refactoring.guru/es/design-patterns) |
| Mermaid Diagrams | [mermaid.js.org](https://mermaid.js.org) |
| OWASP Top 10 (Seguridad) | [owasp.org/Top10](https://owasp.org/www-project-top-ten/) |
| 12 Factor App | [12factor.net](https://12factor.net/es/) |
| Keep a Changelog | [keepachangelog.com](https://keepachangelog.com/es/1.0.0/) |
| Guía de Git y GitHub | [docs.github.com](https://docs.github.com/es) |
