# FastAPI Response Model (Return Type)

## Introduction

Response models in FastAPI allow you to specify the structure of the data returned by your API endpoints. Using **Pydantic models** as response models helps ensure the response conforms to a defined schema. This structure improves API documentation and reduces errors when clients interact with the API by letting them know exactly what data to expect.

## Key Points about Response Models

1. **Validation**: FastAPI validates the data before sending it as a response, ensuring it matches the specified schema.
2. **Automatic Documentation**: When you use response models, FastAPI’s auto-generated documentation (Swagger UI) clearly shows the structure of the response data.
3. **Data Shaping**: Response models can help filter or reshape the data so that only the necessary fields are sent back to the client.

## Setting Up a Response Model

To define a response model:

1. Use a **Pydantic model** to represent the structure of the response.
2. Pass the Pydantic model to the `response_model` parameter in your route decorator.
