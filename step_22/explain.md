# JSON Compatible Encoder

The **JSON Compatible Encoder** in FastAPI is used to convert Python objects into JSON-compatible data structures. It is particularly useful when you need to serialize custom objects (e.g., database models, Pydantic models, or complex data types) into JSON-compatible formats like dictionaries, lists, and primitives (int, float, str, bool, None).

FastAPI provides the `jsonable_encoder` utility for this purpose.

## Key Features of `jsonable_encoder`

1. Converts Pydantic models, datetime objects, and other Python types into JSON-compatible formats.
2. Ensures nested data structures are properly serialized.
3. Allows custom handling of non-serializable objects.

### Key Sections in the Script

1. **Basic Encoding**:
   - In the `/items/` endpoint, a Pydantic model (`Item`) is encoded into a JSON-compatible dictionary using `jsonable_encoder`.

2. **Nested Data Handling**:
   - In the `/orders/` endpoint, the `Order` model contains a list of nested `Item` models, which are serialized automatically.

3. **Custom Encoding**:
   - The `/custom-object/` endpoint demonstrates handling non-serializable objects by defining a `custom_encoder` dictionary to specify how to serialize the `CustomObject`.

### How `jsonable_encoder` Works

- Converts Python objects into formats compatible with JSON:
  - `datetime` → ISO 8601 string (`2024-11-10T10:00:00`).
  - `Pydantic` models → dictionaries.
  - Lists, dictionaries, and primitives remain unchanged.
- Handles nested structures (e.g., lists of models, models inside models).

### Benefits of Using `jsonable_encoder`

1. **JSON Compatibility**: Ensures all returned data is JSON-compatible without manual conversion.
2. **Automatic Handling**: Works seamlessly with Pydantic models and nested data structures.
3. **Customizability**: Allows you to define custom serialization logic for unsupported data types.
