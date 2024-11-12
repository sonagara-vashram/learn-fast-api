# FastAPI Form Data

## Introduction

Form Data is used when data is submitted from an HTML form using the `POST` method with the `Content-Type` set to `application/x-www-form-urlencoded` or `multipart/form-data` (for file uploads). In FastAPI, you can handle form data directly using the `Form` class, which allows easy access to values sent via forms.

## Key Points about Form Data in FastAPI

1. **Single Values**: Form Data is typically used to capture simple, single values, like text, numbers, or dropdown selections.
2. **File Uploads**: Form Data can also handle files (using `File` class).
3. **Multiple Fields**: You can define multiple form fields in the endpoint function, and FastAPI will capture each one based on the `Form` class usage.

## Setting Up Form Data

To work with form data:

1. Use the `Form` class to declare form fields in your endpoint function.
2. Ensure that the client sends data with `application/x-www-form-urlencoded` or `multipart/form-data` encoding.
