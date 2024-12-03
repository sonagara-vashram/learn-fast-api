# **Additional Status Codes in FastAPI**

FastAPI allows you to define custom status codes for your path operations to handle different scenarios, such as success, errors, or other HTTP status conditions.

---

## **Key Features**

1. **Set a Custom Status Code**:
   - Use the `status_code` parameter in path operations to return specific HTTP status codes (e.g., 201, 204, etc.).

2. **Predefined Status Codes**:
   - FastAPI provides `status` from `fastapi` for predefined HTTP status codes for readability.

3. **Custom Responses with `responses`**:
   - Define additional response codes and descriptions using the `responses` parameter.

### **Explanation**

1. **Custom Status Codes**:
   - `status.HTTP_201_CREATED`: For successful creation (POST).
   - `status.HTTP_204_NO_CONTENT`: For successful deletion (DELETE).
   - `status.HTTP_202_ACCEPTED`: For asynchronous updates (PUT or POST).

2. **Error Handling**:
   - Use `HTTPException` to raise specific error codes (e.g., 400 or 404).

3. **Custom Responses**:
   - The `responses` parameter adds descriptions for different status codes, making API docs more descriptive.
