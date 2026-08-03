# Plan de trabajo — inventory-management-api

Proyecto nuevo (directorio vacío) construido sobre la arquitectura del fastapi-template (capas: router → service → repository → database, con modelos y schemas Pydantic). Alcance confirmado: todos los módulos, sin auth por ahora, SQLite (dev) + PostgreSQL (prod), tests unit + integración con pytest.

## Fase 0 — Setup del proyecto

[] - Copiar el esqueleto del fastapi-template a inventory-management-api (app/core, app/database, app/main.py, docs, pyproject.toml, .env.example, .gitignore).
[] - Inicializar git y repositorio; ajustar Settings: app_name=Inventory Management API, app_version=0.1.0.
[] - Verificar uv run uvicorn app.main:app --reload y Swagger en /docs.

## Fase 1 — Infraestructura base

[] - Configurar Alembic (alembic.ini, env.py, carpeta migrations, primera migración).
[] - Crear estructura de capas vacía: app/api/routers, app/services, app/repositories, app/models, app/schemas.
[] - Excepciones de dominio (NotFoundException, ConflictException) + global exception handler.
[] - Setup de tests: tests/conftest.py con DB SQLite en memoria, fixtures de sesión/cliente y factory de datos.

## Fase 2 — Módulo Categories

[] - Model Category (name único, description), schema, repository, service, router CRUD en /categories.
[] - Tests unit + integración (CRUD, duplicado → 409, inexistente → 404).

## Fase 3 — Módulo Suppliers

[] - Model Supplier (name, contact_name, email, phone, address), repository, service, router CRUD en /suppliers.
[] - Tests.

## Fase 4 — Módulo Products

[] - Model Product (sku único, name, description, price, quantity, reorder_level, FK category_id, FK supplier_id).
[] - Reglas: SKU duplicado → 409; categoría/proveedor inexistente → 404.
[] - Router en /products con paginación (skip/limit), filtrado (categoría, proveedor, búsqueda por nombre/SKU) y ordenamiento.
[] - Tests.

## Fase 5 — Módulo Stock Movements

[] - Model StockMovement (product_id, quantity firmada, movement_type IN/OUT, reason, created_at).
[] - Regla de negocio: un OUT no puede superar el stock disponible (conflicto con transacción atómica que actualiza Product.quantity).
[] - Endpoints: POST /products/{id}/movements, GET /movements (filtros por producto/tipo), stock actual por producto.
[] - Tests.

## Fase 6 — Módulo Purchase Orders

[] - Models PurchaseOrder (estado: pending/received/cancelled, supplier_id) + PurchaseOrderItem (product_id, quantity, unit_cost).
[] - Servicio: al marcar la orden como received, aplica entrada de stock y registra el movimiento asociado.
[] - Router CRUD en /purchase-orders + endpoint de recepción.
[] - Tests.

## Fase 7 — Alertas y resumen

[] - GET /products/low-stock (quantity ≤ reorder_level).
[] - Resumen de inventario: valor total, totales por categoría (opcional).

## Fase 8 — PostgreSQL (producción)

[] - Añadir psycopg como dependencia; DATABASE_URL apuntando a PostgreSQL vía .env.
[] - Probar migraciones con el engine de Postgres.

## Fase 9 — Calidad y documentación

[] - README propio del proyecto + docs (architecture, api-conventions, project-rules).
[] - Ruff, type hints; correr toda la suite de tests.

## Fase 10 — Entrega

[] - Verificación final (uvicorn + Swagger, flujo completo: categorías → proveedores → productos → movimientos → órdenes) y commit inicial.