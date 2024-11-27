from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

# Define a background task
def write_log(message: str):
    with open("log.txt", "a") as log_file:
        log_file.write(f"{message}\n")

@app.post("/send-notification/")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    # Queue the background task
    background_tasks.add_task(write_log, f"Notification sent to {email}")
    return {"message": f"Notification will be sent to {email} shortly."}

@app.get("/read-log/")
def read_log():
    with open("log.txt", "r") as log_file:
        logs = log_file.readlines()
    return {"logs": logs}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)