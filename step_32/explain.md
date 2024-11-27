# Background Tasks in FastAPI

FastAPI provides an easy way to handle **background tasks** using the `BackgroundTasks` class. This is useful when you want to perform tasks **asynchronously** after responding to the client, such as:

- Sending emails.
- Writing logs to a file.
- Processing data asynchronously.

## Key Features of Background Tasks

1. **Non-blocking Execution**: Tasks run in the background, and the client gets an immediate response.
2. **Easy Integration**: Use `BackgroundTasks` as a dependency in your route.

### Explanation

1. **`write_log`**:
   - A function that writes a message to `log.txt`. This simulates a background task like sending an email or logging.

2. **`BackgroundTasks`**:
   - Injected into the route as a dependency.
   - The `add_task` method schedules the `write_log` function to run in the background after the response is sent.

3. **Endpoints**:
   - `POST /send-notification/`: Accepts an email, schedules the `write_log` function as a background task, and immediately responds to the client.
   - `GET /read-log/`: Reads the log file to verify that background tasks are working.
