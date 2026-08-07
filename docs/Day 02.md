
# Day 02 – Backend Setup, Frontend Setup & First Full-Stack Connection

## Objective

Today's goals were:

- Set up the FastAPI backend
- Learn virtual environments
- Create the first API endpoint
- Set up the Next.js frontend
- Configure CORS
- Prepare the frontend to communicate with the backend

---

# Windows PowerShell – Terminal 1 (Backend)

## 1. Open the project

```powershell
cd D:\Resume_Projects\ResearchOS
code .
cd backend
```

Current Working Directory:

```text
D:\Resume_Projects\ResearchOS\backend
```

---

## 2. Create a Virtual Environment

```powershell
python -m venv .venv
```

### Why?

A virtual environment creates an isolated Python environment for the project so that all dependencies remain local to this project instead of being installed globally.

---

## 3. Activate the Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### Error Encountered

```powershell
.\.venv\Scripts\Activate.ps1 : File ...
cannot be loaded because running scripts is disabled on this system.
```

### Why did this happen?

PowerShell's Execution Policy was set to **Restricted**, preventing PowerShell scripts from running.

---

## 4. Fix the Execution Policy

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

| Part | Meaning |
|------|---------|
| `Set-ExecutionPolicy` | Changes PowerShell's execution policy |
| `-Scope Process` | Applies only to the current PowerShell session |
| `-ExecutionPolicy Bypass` | Temporarily bypasses execution restrictions |

> Using `Process` scope is safer because it does **not** permanently modify the system's execution policy.

---

## 5. Activate Again

```powershell
.\.venv\Scripts\Activate.ps1
```

Expected terminal:

```text
(.venv) PS D:\Resume_Projects\ResearchOS\backend>
```

---

## 6. Install Backend Packages

```powershell
pip install fastapi uvicorn
```

Packages installed:

- FastAPI
- Uvicorn

> Ignore upgrade notices unless there is a specific reason to update packages.

---

## 7. Create `main.py`

Create:

```text
backend/main.py
```

---

## 8. Import FastAPI

```python
from fastapi import FastAPI
```

Imports the `FastAPI` class from the FastAPI package.

---

## 9. Create the FastAPI Application

```python
app = FastAPI()
```

Creates the FastAPI application instance.

---

## 10. Create the First Endpoint

```python
@app.get("/")
def root():
    return {"message": "Welcome to ResearchOS!"}
```

`@app.get("/")` registers a GET endpoint.

Whenever a client sends:

```http
GET /
```

FastAPI executes `root()`.

The returned Python dictionary is automatically converted into JSON before being sent to the client.

---

## 11. Run the Backend

```powershell
uvicorn main:app --reload
```

| Part | Meaning |
|------|---------|
| `main` | `main.py` |
| `app` | FastAPI application instance |
| `--reload` | Restarts automatically whenever code changes |

Visit:

```text
http://127.0.0.1:8000
```

Expected response:

```json
{
  "message": "Welcome to ResearchOS!"
}
```

---

## 12. Understanding the Logs

Successful request:

```text
GET / HTTP/1.1 200 OK
```

| Part | Meaning |
|------|---------|
| GET | HTTP method |
| / | Requested route |
| HTTP/1.1 | HTTP protocol version |
| 200 OK | Request processed successfully |

Browser request:

```text
GET /favicon.ico HTTP/1.1 404 Not Found
```

Browsers automatically request `favicon.ico`.

Since the backend doesn't serve one yet, `404 Not Found` is expected.

---

## 13. Hot Reload

When `main.py` changes:

```text
WARNING: StatReload detected changes in 'main.py'. Reloading...
```

Uvicorn automatically restarts the server.

---

# Windows PowerShell – Terminal 2 (Frontend)

> Do **not** close Terminal 1.

```powershell
cd D:\Resume_Projects\ResearchOS\frontend
```

---

## 14. Create the Next.js Project

```powershell
npx create-next-app@latest .
```

| Part | Meaning |
|------|---------|
| `npx` | Executes Node packages |
| `create-next-app` | Creates a Next.js application |
| `@latest` | Latest stable version |
| `.` | Create inside current directory |

---

## 15. Configuration

- TypeScript → Yes
- ESLint → Yes
- React Compiler → No
- Tailwind CSS → Yes
- Use `src/` directory → Yes
- App Router → Yes
- Import Alias → No
- Agents.md → No

---

## 16. Inspect the Project

```powershell
dir
```

Lists files and folders.

Locate `page.tsx`:

```powershell
tree src /F
```

---

## 17. Replace the Default Template

Replace the contents of:

```text
src/app/page.tsx
```

with the ResearchOS frontend code.

---

# Configure CORS

Add:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Why?

Frontend:

```text
http://localhost:3000
```

Backend:

```text
http://localhost:8000
```

These are different origins.

CORS tells the browser that this frontend is allowed to access the backend.

---

# Start the Frontend

Run the following command from the `frontend` directory:

```powershell
npm run dev
```

If the server starts successfully, the terminal should display something similar to:

```powershell
> frontend@0.1.0 dev
> next dev

▲ Next.js 16.3.0 (Turbopack)

- Local:         http://localhost:3000
- Network:       http://192.168.0.181:3000

✓ Ready in 3.7s
✓ Running next.config.ts took 118ms
```

### Explanation

| Output | Meaning |
|---------|---------|
| `frontend@0.1.0 dev` | Executes the `dev` script defined in `package.json`. |
| `next dev` | Starts the Next.js development server. |
| `Local` | Address where the application can be accessed from the current machine. |
| `Network` | Address where other devices on the same local network can access the application (if allowed). |
| `Ready in 3.7s` | The development server has started successfully and is ready to accept requests. |
| `Running next.config.ts took 118ms` | Next.js successfully loaded and executed the project's configuration file. |

---

## Open the Application

Open the following URL in your browser:

```text
http://localhost:3000
```

If the frontend is successfully communicating with the backend, the page should display something similar to:

```text
ResearchOS

Backend Status:

Welcome to ResearchOS!
```

---

## Terminal Output After Opening the Browser

Once the browser requests the page, the frontend terminal will show logs similar to:

```powershell
GET / 200 in 2.7s (next.js: 1902ms, application-code: 770ms)
GET / 200 in 262ms (next.js: 28ms, application-code: 233ms)
GET / 200 in 152ms (next.js: 25ms, application-code: 127ms)
```

### Understanding the Log

| Part | Meaning |
|------|---------|
| `GET` | HTTP method used by the browser to request the page. |
| `/` | The requested route (the application's home page). |
| `200` | HTTP Status Code indicating that the request was processed successfully. |
| `in ... ms` | Total time taken by Next.js to process and return the response. |
| `next.js: ... ms` | Time spent by the Next.js framework. |
| `application-code: ... ms` | Time spent executing the application's code. |

---

## Observation

Every time the browser is refreshed, it sends a **new HTTP GET request** to the Next.js server.

As a result, each page refresh generates a new log entry similar to:

```powershell
GET / 200
```

Therefore, if the page is refreshed **five times**, the terminal will display **five separate `GET / 200` log entries**, with the processing time potentially varying for each request.

Each log entry represents one complete **HTTP Request–Response Lifecycle** between the browser and the Next.js frontend.


---
# Concepts Learned

- Python Virtual Environments
- FastAPI
- Uvicorn
- API Endpoints
- HTTP Methods (GET)
- JSON Responses
- Hot Reloading
- Next.js Project Setup
- React Components
- Client Components
- TypeScript Basics
- Fetch API
- Asynchronous Programming (`async` / `await`)
- CORS (Cross-Origin Resource Sharing)
- Frontend–Backend Communication
- HTTP Request–Response Lifecycle

---

# End of Day Procedure

After completing the implementation and verifying that everything works correctly, shut down the development environment safely.

## 1. Stop the Frontend Development Server

Go to **Terminal 2 (Frontend)** and press:

```text
Ctrl + C
```

If prompted:

```text
Terminate batch job (Y/N)?
```

Type:

```text
Y
```

This gracefully stops the Next.js development server.

---

## 2. Stop the Backend Development Server

Go to **Terminal 1 (Backend)** and press:

```text
Ctrl + C
```

This stops the Uvicorn development server.

---

## 3. Deactivate the Python Virtual Environment

If the backend terminal is still open, run:

```powershell
deactivate
```

This removes the virtual environment from the current terminal session.

> **Note:** This does **not** delete the virtual environment. It only deactivates it for the current PowerShell session.

---

## 4. Close the Terminals

Once both development servers have been stopped, the terminal windows can be closed safely.

No project files or Git history are affected.

---

## 5. Save the Day's Progress in Git

Navigate to the project root:

```powershell
cd D:\Resume_Projects\ResearchOS
```

Check the repository status:

```powershell
git status
```

Stage all completed work:

```powershell
git add .
```

Verify the staged changes:

```powershell
git status
```

Create a commit:

```powershell
git commit -m "Day 2: Set up FastAPI backend, Next.js frontend, and frontend-backend communication"
```

Push the commit to GitHub:

```powershell
git push
```

Finally, verify that the repository is clean:

```powershell
git status
```

Expected output:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

This confirms that all local changes have been committed and pushed successfully.

---

## Starting the Project Again

Whenever continuing the project in the future:

### Backend (Terminal 1)

```powershell
cd D:\Resume_Projects\ResearchOS\backend
.\.venv\Scripts\Activate.ps1
uvicorn main:app --reload
```

### Frontend (Terminal 2)

```powershell
cd D:\Resume_Projects\ResearchOS\frontend
npm run dev
```

Both servers should now be running, allowing the frontend and backend to communicate as before.

---

# Today's Architecture

```text
Browser
    │
    ▼
Next.js Frontend
    │
    ▼
HTTP Request
    │
    ▼
FastAPI Backend
    │
    ▼
JSON Response
    │
    ▼
Next.js Frontend
    │
    ▼
Browser
```

---

# Reflection

Today I built the first complete full-stack workflow of ResearchOS.

The FastAPI backend was successfully set up with the first API endpoint, and the Next.js frontend was initialized and connected to it. I learned how the browser communicates with the frontend, how the frontend sends HTTP requests to the backend, how FastAPI processes those requests, and how JSON responses are returned and rendered in the browser.

This marks the first end-to-end communication between the frontend and backend, providing the foundation for all future features in ResearchOS.
