from fastapi import FastAPI, File, UploadFile, HTTPException

app = FastAPI()

# Endpoint to handle file upload
@app.post("/upload-profile-pic/")
async def upload_profile_pic(file: UploadFile = File(...)):
    # Check file type for security (e.g., only allow image files)
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type. Only image files are allowed.")
    
    # Process file (e.g., save it, process it, etc.)
    # For example, here we're just reading the file's content
    file_content = await file.read()
    
    # Returning file details for demonstration
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "file_size": len(file_content)
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)