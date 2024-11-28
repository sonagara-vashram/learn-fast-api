# Metadata and Docs URLs in FastAPI

In FastAPI, you can customize the **metadata** and URLs for the automatically generated API documentation. This is useful for tailoring the documentation to your project's branding or requirements.

## Features of Metadata and Docs URLs

1. **Metadata**:
   - Includes the **title**, **description**, **version**, **terms of service**, **contact information**, and **license information**.
   - Appears on the Swagger UI and ReDoc documentation pages.

2. **Docs URLs**:
   - Customize the default URLs for Swagger UI (`/docs`) and ReDoc (`/redoc`).
   - Disable either or both by setting their URL to `None`.

### Explanation

1. **Metadata Parameters**:
   - **`title`**: The title of your API (e.g., "My API").
   - **`description`**: A detailed description of the API.
   - **`version`**: The version of the API (e.g., "1.0.0").
   - **`terms_of_service`**: A URL pointing to your terms of service.
   - **`contact`**: A dictionary containing:
     - `name`: Contact person's name.
     - `url`: A website or support link.
     - `email`: An email for contacting support.
   - **`license_info`**: A dictionary with:
     - `name`: License type (e.g., "MIT").
     - `url`: URL pointing to the license details.

2. **Custom Docs URLs**:
   - **`docs_url`**: Customizes the Swagger UI endpoint (default: `/docs`).
   - **`redoc_url`**: Customizes the ReDoc endpoint (default: `/redoc`).
   - Set these parameters to `None` to disable the respective documentation.
