# Docker Optimization Project

##  Objective
To build an ultra-lightweight Docker image (<10MB) for serving a static portfolio using Alpine Linux and multi-stage builds.

---

## ⚙️ Tech Stack
- Docker
- Alpine Linux
- BusyBox HTTP Server
- HTML & CSS

---

##  Approach

1. Used **multi-stage builds** to separate build and runtime environments
2. Used **Alpine Linux** for lightweight base image
3. Used **BusyBox** for minimal HTTP server
4. Optimized image size using `.dockerignore`

---

##  How to Run

```bash
docker build -t portfolio .
docker run -p 8080:8080 portfolio
