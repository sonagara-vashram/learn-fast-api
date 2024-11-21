# Dependencies in Path Operation Decorators

In FastAPI, you can declare dependencies **directly in the path operation decorators** instead of within the function parameters. This is particularly useful when you want to apply the same dependencies to multiple endpoints or keep the function signatures clean.

---

## Key Features

1. **Global Dependency Declaration**:
   - Add dependencies at the **decorator level**.
   - Applies to the endpoint without appearing in the function arguments.

2. **Reusable Logic**:
   - Use the same dependency across multiple routes by defining it once.

3. **Cleaner Code**:
   - Keeps path operation function signatures minimal.

### Explanation of the Script

1. **Dependency Declaration in Decorator**:
   - In `/secure-data/`, the `verify_token` dependency is applied in the `dependencies` parameter of the `@app.get` decorator.
   - The function does not take the dependency as an argument, making it clean.

2. **Inline Dependency Use**:
   - In `/secure-info/`, the `verify_token` dependency is explicitly used as a function parameter (`user: dict = Depends(verify_token)`).
   - This allows access to the returned value (`user`), enabling additional logic inside the route.

3. **Custom Dependency Logic**:
   - `verify_token` checks the token and raises an `HTTPException` if it is invalid.
   - If valid, it returns user details (e.g., username and permissions).

### Benefits of Using Dependencies in Path Operation Decorators

1. **Centralized Logic**:
   - Define once, use across multiple routes.

2. **Cleaner Code**:
   - Keeps function parameters focused only on endpoint-specific logic.

3. **Customizability**:
   - Combine decorator-level dependencies with inline dependencies for greater flexibility.
