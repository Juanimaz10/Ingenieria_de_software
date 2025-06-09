# Ingeniería de Software - Proyecto

## 📚 Información de la Materia

**Asignatura:** Ingeniería de Software  
**Curso:** 4º Año  
**Carrera:** Ingeniería en Informática  
**Profesor Titular:** Lic. Pablo Andrés Prats  

## 🎯 Proyecto

El proyecto de **Gestión de Stock**  incluye:

- Una arquitectura **Monolítica** 
    - https://github.com/Juanimaz10/Ingenieria_de_software
- Metodologías ágiles utilizando Scrum a través de **GitHub Projects**
- Contenedor para servicios y para el proyecto con Docker (carpeta docker)

## 📋 Metodología de Trabajo

### Desarrollo Ágil con Scrum

El proyecto se desarrolla siguiendo la metodología **Scrum** con las siguientes características:

- **Trabajo grupal** con rotación de roles cada 2 semanas
- **Roles:** Product Owner: Pablo Andrés Prats, Scrum Master: **Juan Imaz** y Equipo de Desarrollo
- **Stakeholder:** Pablo Andrés Prats

## 🛠️ Tareas del Proyecto

### Gestión del Proyecto
- [ ] Redacción de **historias de usuario**
- [ ] **Planificación y ejecución de Sprints** a través de **GitHub Projects**

### Diseño y Arquitectura
- [ ] Implementación de **diagramas de clases** (carpeta docs)
- [ ] Creación de **diagramas de secuencia** (carpeta docs)
- [ ] Aplicación de **arquitectura de microservicios**
- [ ] Patrones de **microservicios**:
    - Patrón API Gateway
    - Strangler
    - Decompose by Business Capability
- [ ] Diseño de **APIs** para comunicación entre servicios

### Desarrollo y Despliegue
- [ ] Creación y despliegue de **contenedores Docker**
    - Dockerfile
    - docker-compose.yml
    - Para construir:docker build -t stock:TAG .
    - Para construir una red:docker network create mired
    - Para ejecucción:docker compose up -d
- [ ] Implementación de servicios independientes (PostgreSQL) a través de contenedores.
- [ ] Aplicación de patrones de diseño

### Control de Versiones
- [ ] Uso de **Git** con flujos de trabajo **Trunk-based Development**
- [ ] **Versionado** adecuado del código

 -🎯Una arquitectura **Microservicio** 
    - receipt_microservice: https://github.com/AugustoCastroo/receipt_microservice
    - MicroserviceNotification: https://github.com/Almonacid98/MicroserviceNotification
    - Article-Micro-Service: https://github.com/Pachi69/Article-Micro-Service
    - stock-microservice: https://github.com/Facumerino03/stock-microservice
- Metodologías ágiles utilizando Scrum a través de **GitHub Projects**
- Contenedor para servicios y para el proyecto con Docker (carpeta docker)

## 🏗️ Estructura del Proyecto

```
Gestión de Stock/
├── docs/
│   └── (diagramas)
├── app/
│   ├── models/
│   ├── controllers/
│   ├── mappings/
│   ├── services/
│   ├── routes/
│   └── repositories/
├── app/
├── docker/
│   ├── db
│   │   ├── data/
│   │   └── docker-compose.yml
│   └── app
│        └── docker-compose.yml
├── tests/
└── README.md
└── Dockerfile
```

## 🔧 Tecnologías Utilizadas

- **Lenguaje:** Python
- **Framework:** Flask
- **Arquitectura:** Monolítico - Aplicación Cliente Servidor (Backend)
- **Control de Versiones:** Git
- **Comunicación:** APIs REST/JSON
- **Principios y Patrones:** YAGNI, SOLID, DRY, MVC, Repository

## 📚 Bibliografía

- **Pressman, R.S.** - "Ingeniería del Software. Un Enfoque Práctico" (7ma Ed.) - McGraw Hill
- **Kniberg, H.** - "Scrum y XP desde las Trincheras" - InfoQ.com
- **Jacobson, I., Booch, G., Rumbaugh, J.** - "El Proceso Unificado de Desarrollo de Software" - Pearson
- **Blé Jurado, C.** - "Diseño Ágil con TDD" - Creative Commons
- **Iradier, Á., Martínez, I.** - "Docker para DevOps de noob a experto" - Creative Commons

## 👥 Equipo de Desarrollo

- **Juan Imaz**
- **Gabriel Almonacid**
- **Mauro Eliel Mato**
- **José Ruti**
- **Augusto Castro**
- **Facundo Merino**
- **Javier Maximiliano**
- **Dolores Herrera Garcia da ROSA**
---
