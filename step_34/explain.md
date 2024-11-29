# Serving Static Files in FastAPI

FastAPI allows you to serve **static files** (like images, JavaScript, CSS, HTML files) using the `StaticFiles` class from `fastapi.staticfiles`. This is particularly useful for serving frontend files, assets, or other static resources directly from your FastAPI app.

## Key Features of Static Files

1. **Static File Serving**:
   - Serve files like images, CSS, or JavaScript directly from a folder.

2. **Mounting a Static Directory**:
   - Define a specific URL path where the static files will be accessible.

3. **Frontend Integration**:
   - Useful for integrating with frontend frameworks (React, Vue, etc.).

### Explanation

1. **`StaticFiles`**:
   - A class provided by FastAPI to serve files from a directory.

2. **`app.mount`**:
   - Mounts a directory (`"static"`) to a specific URL path (`/static`).
   - Files inside the `static/` folder can be accessed via `/static/<filename>`.

3. **Folder Structure**:
   Ensure you have a `static` folder with some files. Example structure:

   ```static
   static/
       style.css
       script.js
       image.png
   ```

4. **Accessing Static Files**:
   - If you have `image.png` in the `static` folder, it will be accessible at:

     ```url
     http://127.0.0.1:8000/static/image.png
     ```
