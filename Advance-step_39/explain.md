# **Custom Response Types in FastAPI**

FastAPI allows developers to return custom responses such as HTML, plain text, file downloads, or streams, instead of just JSON. This is achieved using `Response` objects.

---

## **Key Features of Custom Responses**

1. **HTML Response**:
   - Use `HTMLResponse` for returning HTML content.

2. **Plain Text Response**:
   - Use `PlainTextResponse` for plain text.

3. **File Response**:
   - Use `FileResponse` for file downloads.

4. **Stream Response**:
   - Use `StreamingResponse` for streaming data.

5. **Custom Headers**:
   - Add custom headers to enhance response metadata.

### **Explanation of Features**

1. **HTML Response**:
   - Use `HTMLResponse` to render HTML directly in the browser.
   - Example: `/html` returns formatted HTML content.

2. **Plain Text Response**:
   - Use `PlainTextResponse` to return raw text, often used for logs or debugging.

3. **File Response**:
   - Use `FileResponse` for sending files like PDFs, images, or text files.
   - Specify `media_type` for proper file handling and `filename` for download behavior.

4. **Streaming Response**:
   - Use `StreamingResponse` for sending data in chunks (e.g., large files or live feeds).
   - `data_generator` in the example sends chunks of data one by one.

5. **Custom Headers**:
   - Modify headers in responses to include metadata (e.g., `X-Custom-Header`).
