# **Classes as Dependencies in FastAPI**

In FastAPI, you can use classes as dependencies to manage and share logic across multiple endpoints. This is particularly useful for complex use cases such as:

- Managing state (e.g., configuration or database connections).
- Applying reusable logic (e.g., authentication or filtering).
- Enabling dependency injection with customizable behavior.

Using classes as dependencies allows you to define **logic once** and inject it into endpoints easily.

## **How Classes as Dependencies Work**

1. **Dependency Class**:
   - A class with attributes and methods that encapsulate reusable logic.
   - The `__init__` method can accept parameters that affect the class's behavior.

2. **Dependency Injection**:
   - Use `Depends()` to inject the class into path operations.
   - Access the class’s methods or attributes within the endpoint.
