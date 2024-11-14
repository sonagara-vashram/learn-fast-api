# FastAPI Request Files

## Introduction

When a client uploads a file in an HTTP request, it typically uses the `multipart/form-data` encoding. FastAPI provides the `File` class to handle such file uploads directly, making it easy to retrieve and process the files. You can use this feature for uploading images, documents, and other media files.

## Key Points about Request Files

1. **Multipart Encoding**: File uploads use `multipart/form-data`, which is handled by FastAPI when you use the `File` class.
2. **File Validation**: You can specify file size limits and types, and FastAPI will validate these files based on your configuration.
3. **Optional and Multiple Files**: You can make files optional or allow multiple files to be uploaded by modifying the endpoint parameters.

## Setting Up Request Files

To handle request files:

1. Use the `File` class from `fastapi`.
2. Define the file parameter in your endpoint using `File(...)`.
