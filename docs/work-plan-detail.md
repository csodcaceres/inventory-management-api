# Work Plan — Inventory Management API

Modo de trabajo: paso a paso · una tarea a la vez · confirmación requerida entre pasos
Última actualización: __ / __ / ____

Fase 0 — Setup del proyecto

[x] - Copiar esqueleto del fastapi-template (sin .git)
[] - Inicializar git init
[] - Crear README.md inicial
[] - Crear .gitignore
[] - Configurar Settings en app/core/config.py
[] - Crear .env.example
[] - Crear .env
[] - Verificar uv run uvicorn app.main:app --reload + Swagger /docs
[] - Commit inicial

Fase 1 — Infraestructura base
- Configurar alembic.ini
- Crear env.py (alembic)
- Crear carpeta migrations
- Primera migración (base)
- Crear capa app/models
- Crear capa app/schemas
- Crear capa app/repositories
- Crear capa app/services
- Crear capa app/api/routers
- Crear excepción de dominio NotFoundException
- Crear excepción de dominio ConflictException
- Crear global exception handler
- Crear tests/conftest.py
- Setup DB de test en memoria + fixtures
- Commit
Fase 2 — Módulo Categories
- Crear model Category
- Crear schema Category
- Crear repository Category
- Crear service Category
- Crear router /categories (CRUD)
- Tests unit del service
- Tests de integración de endpoints
- Commit
Fase 3 — Módulo Suppliers
- Crear model Supplier
- Crear schema Supplier
- Crear repository Supplier
- Crear service Supplier
- Crear router /suppliers (CRUD)
- Tests unit del service
- Tests de integración de endpoints
- Commit
Fase 4 — Módulo Products
- Crear model Product
- Crear schema Product
- Crear repository Product
- Crear service Product (reglas SKU único / FKs válidas)
- Crear router /products (CRUD + paginación + filtros)
- Tests unit del service
- Tests de integración de endpoints
- Commit
Fase 5 — Módulo Stock Movements
- Crear model StockMovement
- Crear schema StockMovement
- Crear repository StockMovement
- Crear service StockMovement (regla: OUT ≤ stock, transacción atómica)
- Crear endpoint POST /products/{id}/movements
- Crear endpoint GET /movements
- Crear endpoint stock actual
- Tests unit + integración
- Commit
Fase 6 — Módulo Purchase Orders
- Crear model PurchaseOrder
- Crear model PurchaseOrderItem
- Crear schemas
- Crear repository
- Crear service (lógica de recepción → stock + movimiento)
- Crear router CRUD /purchase-orders
- Crear endpoint de recepción
- Tests unit + integración
- Commit
Fase 7 — Alertas y resumen
- Crear endpoint GET /products/low-stock
- Crear endpoints de resumen (valor total, totales por categoría)
- Tests
- Commit
Fase 8 — PostgreSQL (producción)
- Agregar dependencia psycopg
- Configurar DATABASE_URL para PostgreSQL
- Verificar migraciones contra Postgres
- Commit
Fase 9 — Calidad y documentación
- README final
- Docs: architecture.md
- Docs: api-conventions.md
- Docs: project-rules.md
- Correr Ruff
- Suite completa de tests en verde
- Commit
Fase 10 — Entrega
- Verificación final (flujo completo en Swagger)
- Revisión del historial de commits
- Etiqueta final v1.0.0