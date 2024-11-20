# Sub-Dependencies in FastAPI

In FastAPI, **sub-dependencies** are dependencies that are themselves dependent on other dependencies. This allows you to create complex and reusable dependency chains where one dependency can rely on the output or behavior of another.

## How Sub-Dependencies Work

1. **Primary Dependency**:
   - A dependency that performs some initial task (e.g., authentication, database access).

2. **Secondary Dependency**:
   - Depends on the output of the primary dependency and adds more logic or processing.

3. **Dependency Injection**:
   - Inject dependencies recursively using `Depends()`.
