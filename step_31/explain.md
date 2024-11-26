# Working with SQL (Relational) Databases in FastAPI

FastAPI provides robust support for working with SQL (relational) databases like PostgreSQL, MySQL, or SQLite. You can use an ORM (Object-Relational Mapper) like **SQLAlchemy** or **Tortoise ORM** for efficient database interaction.

## Key Components

1. **Database Connection**:
   - Use a library like `asyncpg` (for PostgreSQL) or `aiomysql` (for MySQL).
   - ORMs like SQLAlchemy manage connections internally.

2. **Models**:
   - Define database tables as Python classes.

3. **CRUD Operations**:
   - Perform Create, Read, Update, Delete operations via ORM or raw queries.

### Explanation

1. **Database Setup**:
   - SQLite is used here as an example database.
   - `SQLAlchemy` is used to define models and manage database operations.

2. **Model**:
   - `Item` class represents a database table with `id`, `name`, and `description` columns.

3. **Session Dependency**:
   - `get_db` ensures that a database session is created and properly closed after the request.

4. **Routes**:
   - `POST /items/`: Adds a new item to the database.
   - `GET /items/{item_id}`: Fetches an item by its ID.
