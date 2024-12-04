from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse, PlainTextResponse, FileResponse, StreamingResponse
import io

app = FastAPI()

# 1. HTML Response
@app.get("/html", response_class=HTMLResponse)
async def get_html():
    html_content = """
    <html>
        <head>
            <title>Custom HTML Response</title>
        </head>
        <body>
            <h1>Hello, FastAPI!</h1>
            <p>This is an example of HTML response.</p>
        </body>
    </html>
    """
    return html_content

# 2. Plain Text Response
@app.get("/text", response_class=PlainTextResponse)
async def get_text():
    return "This is a plain text response from FastAPI!"

# 3. File Response
@app.get("/file")
async def get_file():
    file_path = "example.txt"  # Make sure this file exists in your directory
    return FileResponse(file_path, media_type="text/plain", filename="example.txt")

# 4. Streaming Response
@app.get("/stream")
async def stream_data():
    async def data_generator():
        for i in range(5):
            yield f"Chunk {i + 1}\n"
    return StreamingResponse(data_generator(), media_type="text/plain")

# 5. Custom Headers with Response
@app.get("/custom-headers")
async def custom_headers():
    content = {"message": "This response has custom headers."}
    headers = {"X-Custom-Header": "FastAPI Header"}
    return Response(content=str(content), media_type="application/json", headers=headers)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)