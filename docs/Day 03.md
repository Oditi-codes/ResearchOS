# Day 03 – First Full-Stack Feature: Paper Creation, API Validation & Frontend–Backend Data Flow

## Objective

Today's objective was to move ResearchOS from a basic frontend–backend connection to its first meaningful application feature.

The goals were:

- Start from the working Day 2 project instead of rebuilding the project.
- Create a `Paper` input flow.
- Learn how frontend form data becomes an HTTP request.
- Create a `POST /papers` API endpoint in FastAPI.
- Define and validate the request body using Pydantic.
- Transform user-friendly frontend input into the backend's expected data structure.
- Handle asynchronous API requests in React.
- Handle loading and error states.
- Display the backend response in the frontend.
- Understand frontend–backend API contracts.
- Debug real integration and TypeScript problems.
- End with a clear understanding of the complete request–response lifecycle.
- Reassess the architecture and define the next MVP direction without pretending planned AI functionality is already implemented.

---

# 1. Starting State

Day 3 did **not** start with a blank project.

At the beginning of the day, ResearchOS already had:

```text
ResearchOS/
│
├── backend/
│   ├── .venv/
│   └── main.py
│
├── frontend/
│   └── Next.js application
│
├── assets/
├── docs/
├── README.md
├── .gitignore
└── Architecture.md
```

The Day 2 architecture was:

```text
Browser
    │
    ▼
Next.js Frontend
    │
    │ HTTP
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

The backend was running on:

```text
http://localhost:8000
```

The frontend was running on:

```text
http://localhost:3000
```

The repository was also at a clean Git checkpoint before beginning the new work.

### Important project-management lesson

When continuing an existing project:

> **Do not recreate the environment or architecture that already works.**

First establish:

1. What already works.
2. What the current architecture is.
3. What the last Git checkpoint was.
4. What the smallest next feature should be.

Only then start implementation.

---

# 2. Step 1 — Start From the Existing Project

Open PowerShell and move to the project root:

```powershell
cd D:\Resume\_Projects\ResearchOS
code .
```

Then open the backend in the first terminal:

```powershell
cd backend
```

And open the frontend in a second terminal:

```powershell
cd D:\Resume\_Projects\ResearchOS\frontend
```

### Why two terminals?

ResearchOS currently has two independent development servers:

```text
Terminal 1
FastAPI / Uvicorn
        │
        ▼
localhost:8000


Terminal 2
Next.js
        │
        ▼
localhost:3000
```

Keeping both visible makes debugging much easier.

---

# 3. Step 2 — Start the Backend

Activate the existing virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation because script execution is disabled, use the process-scoped workaround from Day 2:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

Start FastAPI through Uvicorn:

```powershell
uvicorn main:app --reload
```

The backend should now be available at:

```text
http://127.0.0.1:8000
```

---

# 4. Step 3 — Start the Frontend

In Terminal 2:

```powershell
cd D:\Resume\_Projects\ResearchOS\frontend
npm run dev
```

The frontend should be available at:

```text
http://localhost:3000
```

Open it in the browser.

### Why do this before changing anything?

Because we want to establish a known-good baseline.

If the application is already broken before today's changes, then a later failure cannot confidently be attributed to today's implementation.

This is a general engineering practice:

> **Verify the baseline before changing the system.**

---

# 5. Step 4 — Define the Feature Before Coding

The first feature selected for Day 3 was:

> Allow the user to create a research paper through the frontend and send it to the backend.

The intended flow was:

```text
User
  │
  ▼
Paper Creation Form
  │
  ▼
React State
  │
  ▼
JavaScript Object
  │
  ▼
JSON
  │
  ▼
HTTP POST /papers
  │
  ▼
FastAPI
  │
  ▼
Pydantic Validation
  │
  ▼
Python Endpoint
  │
  ▼
JSON Response
  │
  ▼
React
  │
  ▼
Updated UI
```

### Why this feature?

It is small enough to implement quickly but large enough to teach a real full-stack request/response lifecycle.

Instead of building several disconnected UI elements, we created one **vertical slice** that crosses the system boundary.

---

# 6. Step 5 — Create the Backend Request Model

Open:

```text
backend/main.py
```

Import `BaseModel`:

```python
from pydantic import BaseModel
```

Create the request schema:

```python
class PaperCreate(BaseModel):
    title: str
    authors: list[str]
    abstract: str
```

This defines the structure expected when a client wants to create a paper.

The backend expects:

```json
{
  "title": "Attention Is All You Need",
  "authors": [
    "Ashish Vaswani",
    "Noam Shazeer"
  ],
  "abstract": "A paper about transformer architectures."
}
```

---

# 7. Step 6 — Understand Why a Pydantic Model Is Needed

The model:

```python
class PaperCreate(BaseModel):
    title: str
    authors: list[str]
    abstract: str
```

establishes a contract.

Conceptually:

```text
title
    ↓
must be a string

authors
    ↓
must be a list of strings

abstract
    ↓
must be a string
```

This is preferable to accepting arbitrary JSON because the backend knows what structure it is supposed to receive.

### Important mental model

Pydantic is not merely a convenience for writing Python classes.

It gives the API a defined input schema and allows FastAPI to validate incoming data against that schema.

---

# 8. Step 7 — Create the `POST /papers` Endpoint

Add:

```python
@app.post("/papers")
def create_paper(paper: PaperCreate):
    return {
        "id": 1,
        "title": paper.title,
        "authors": paper.authors,
        "abstract": paper.abstract,
        "status": "created"
    }
```

Now the backend exposes:

```text
POST /papers
```

### What happens when a request arrives?

```text
HTTP POST /papers
        │
        ▼
FastAPI matches the route
        │
        ▼
Request body is validated
        │
        ▼
PaperCreate object is created
        │
        ▼
create_paper() executes
        │
        ▼
Python dictionary returned
        │
        ▼
FastAPI serializes it as JSON
```

---

# 9. Step 8 — Understand Why `POST` Was Used

The operation is creating/submitting a new paper resource.

Therefore:

```text
POST /papers
```

is appropriate.

A useful simplified mental model is:

```text
GET
→ retrieve/read

POST
→ create/send data for processing

PUT/PATCH
→ update

DELETE
→ remove
```

This is not merely a syntax decision.

The HTTP method communicates the intended operation to clients and other developers.

---

# 10. Step 9 — Verify the Backend Independently

Before connecting the frontend, test the endpoint directly.

Use FastAPI's automatically generated API documentation:

```text
http://127.0.0.1:8000/docs
```

Find:

```text
POST /papers
```

Send a valid request such as:

```json
{
  "title": "Attention Is All You Need",
  "authors": [
    "Ashish Vaswani",
    "Noam Shazeer"
  ],
  "abstract": "A paper about transformer architectures."
}
```

Expected response:

```json
{
  "id": 1,
  "title": "Attention Is All You Need",
  "authors": [
    "Ashish Vaswani",
    "Noam Shazeer"
  ],
  "abstract": "A paper about transformer architectures.",
  "status": "created"
}
```

### Why test the backend independently?

This isolates the backend from the frontend.

If the API works directly but the frontend fails, the problem is likely in:

```text
frontend
request construction
CORS
API contract
```

rather than in the endpoint itself.

This is a general debugging principle:

> **Test system boundaries independently before debugging the entire system at once.**

---

# 11. Step 10 — Build the Frontend Form

The frontend needs to collect:

```text
Title
Authors
Abstract
```

We therefore created separate React state values:

```tsx
const [title, setTitle] = useState("");
const [authors, setAuthors] = useState("");
const [abstract, setAbstract] = useState("");
```

The reason for separate state is that these are separate pieces of application data.

The eventual backend representation is:

```text
title
→ string

authors
→ string[]

abstract
→ string
```

However, the user-friendly authors input is initially a single text field.

---

# 12. Step 11 — Create Controlled Inputs

For the title:

```tsx
<input
  type="text"
  value={title}
  onChange={(event) => setTitle(event.target.value)}
/>
```

For authors:

```tsx
<input
  type="text"
  value={authors}
  onChange={(event) => setAuthors(event.target.value)}
/>
```

For the abstract:

```tsx
<textarea
  value={abstract}
  onChange={(event) => setAbstract(event.target.value)}
/>
```

These are **controlled inputs**.

The data flow is:

```text
User types
    │
    ▼
onChange event
    │
    ▼
event.target.value
    │
    ▼
setState()
    │
    ▼
React state
    │
    ▼
Component re-renders
```

---

# 13. Step 12 — Use a Form Instead of an Isolated Button

The inputs were placed inside:

```tsx
<form onSubmit={handleSubmit}>
```

and the button was:

```tsx
<button type="submit">
    Add Paper
</button>
```

This gives the browser a semantic form structure while allowing React to control the submission.

The flow becomes:

```text
User clicks Add Paper
        │
        ▼
Form submit event
        │
        ▼
handleSubmit()
```

---

# 14. Step 13 — Prevent the Browser's Default Form Submission

Inside the submit handler:

```tsx
event.preventDefault();
```

was added.

Normally, a browser form submission may cause the browser to perform its default navigation/submission behaviour.

That is not what we want.

We want:

```text
Browser default form submission
        ❌

React
  ↓
fetch()
  ↓
FastAPI
```

Therefore:

```tsx
event.preventDefault();
```

tells the browser not to perform its default action.

---

# 15. Step 14 — Transform Authors From String to List

The user enters something such as:

```text
Ashish Vaswani, Noam Shazeer
```

But the backend expects:

```python
list[str]
```

Therefore we transform the input:

```tsx
const authorList = authors
  .split(",")
  .map((author) => author.trim());
```

The transformation is:

```text
"Ashish Vaswani, Noam Shazeer"
              │
              ▼
.split(",")
              │
              ▼
[
  "Ashish Vaswani",
  " Noam Shazeer"
]
              │
              ▼
.map(author => author.trim())
              │
              ▼
[
  "Ashish Vaswani",
  "Noam Shazeer"
]
```

This is an example of adapting a user-friendly interface representation to an API representation.

---

# 16. Step 15 — Construct the Request Object

Inside `handleSubmit()`:

```tsx
const paper = {
  title,
  authors: authorList,
  abstract,
};
```

Now the frontend has a JavaScript object matching the backend contract.

Conceptually:

```text
React State
    │
    ▼
paper object
    │
    ▼
JSON representation
    │
    ▼
HTTP request body
```

---

# 17. Step 16 — Send the HTTP POST Request

The frontend request was implemented using `fetch()`:

```tsx
const response = await fetch("http://localhost:8000/papers", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify(paper),
});
```

This contains several separate concepts.

---

## 17.1 `method`

```tsx
method: "POST"
```

Specifies the HTTP method.

---

## 17.2 `headers`

```tsx
headers: {
  "Content-Type": "application/json",
}
```

Tells the server that the request body is JSON.

---

## 17.3 `body`

```tsx
body: JSON.stringify(paper)
```

Converts the JavaScript object into JSON text.

For example:

```tsx
{
  title: "Attention Is All You Need",
  authors: ["Ashish Vaswani"],
  abstract: "..."
}
```

becomes JSON suitable for transmission:

```json
{
  "title": "Attention Is All You Need",
  "authors": ["Ashish Vaswani"],
  "abstract": "..."
}
```

---

# 18. Step 17 — Understand `async` / `await`

The submit handler was made asynchronous:

```tsx
const handleSubmit = async (event) => {
```

and the request uses:

```tsx
await fetch(...)
```

Later:

```tsx
await response.json()
```

The mental model is:

```text
async function
      │
      ▼
can wait for asynchronous operations
      │
      ▼
await fetch()
      │
      ▼
HTTP request completes
      │
      ▼
continue execution
```

The browser does not need to block the entire application while waiting for the network request.

---

# 19. Step 18 — Parse the JSON Response

After the request:

```tsx
const data = await response.json();
```

There are two different things here:

```text
response
→ HTTP Response object

response.json()
→ reads/parses the JSON response body

data
→ JavaScript object
```

This allows the frontend to access:

```tsx
data.title
data.authors
data.abstract
```

and other response fields.

---

# 20. Step 19 — Handle HTTP Errors Correctly

We added:

```tsx
if (!response.ok) {
  throw new Error(`HTTP error! status: ${response.status}`);
}
```

This is important because:

> `fetch()` does not automatically throw an exception simply because the server returned an HTTP 4xx or 5xx response.

For example:

```text
HTTP 422
```

can still produce a resolved `fetch()` promise.

Therefore the application must explicitly inspect:

```tsx
response.ok
```

The mental model is:

```text
fetch()
   │
   ▼
Was there a network-level failure?
   │
   ├── yes → catch()
   │
   └── no
        │
        ▼
   HTTP response received
        │
        ▼
   response.ok?
      │
      ├── yes → process response
      │
      └── no  → throw error
```

---

# 21. Step 20 — Add Loading State

We added:

```tsx
const [loading, setLoading] = useState(false);
```

Before sending the request:

```tsx
setLoading(true);
```

And after completion:

```tsx
setLoading(false);
```

The cleanup belongs in `finally`:

```tsx
finally {
  setLoading(false);
}
```

The UI can show:

```tsx
{loading && <p>Creating paper...</p>}
```

The resulting flow is:

```text
Submit
  ↓
loading = true
  ↓
UI shows "Creating paper..."
  ↓
HTTP request
  ↓
response/error
  ↓
loading = false
```

---

# 22. Step 21 — Add Error State

We added:

```tsx
const [error, setError] = useState("");
```

At the beginning of a new request:

```tsx
setError("");
```

If something goes wrong:

```tsx
setError("Failed to create paper. Please try again.");
```

The UI can conditionally render it:

```tsx
{error && <p>{error}</p>}
```

This introduces a standard frontend state model:

```text
idle
 │
 ├── loading
 │
 ├── success
 │
 └── error
```

Even though the implementation uses separate state variables, thinking in terms of request states is useful for future applications.

---

# 23. Step 22 — Add `try / catch / finally`

The request logic was organized around:

```tsx
try {
  // perform request
}
catch (error) {
  // handle failure
}
finally {
  // cleanup
}
```

### `try`

Attempts the operation.

### `catch`

Handles an error.

### `finally`

Runs whether the operation succeeded or failed.

This is why:

```tsx
setLoading(false);
```

belongs naturally in `finally`.

---

# 24. Step 23 — Store the Created Paper in React State

We created a state variable for the backend response:

```tsx
const [createdPaper, setCreatedPaper] = useState<CreatedPaper | null>(null);
```

After a successful request:

```tsx
const data = await response.json();
setCreatedPaper(data);
```

The data flow becomes:

```text
FastAPI JSON response
        │
        ▼
response.json()
        │
        ▼
JavaScript object
        │
        ▼
setCreatedPaper()
        │
        ▼
React state changes
        │
        ▼
React re-renders
        │
        ▼
UI displays the created paper
```

This is an important full-stack pattern.

---

# 25. Step 24 — Display the Response

The UI can conditionally display the result:

```tsx
{createdPaper && (
  <div>
    <p>Paper created successfully!</p>
    <p>Title: {createdPaper.title}</p>
    <p>Authors: {createdPaper.authors.join(", ")}</p>
  </div>
)}
```

This means:

```text
createdPaper = null
    ↓
nothing to display

createdPaper = object
    ↓
display paper
```

---

# 26. Step 25 — Define the TypeScript Response Type

Initially, the state was created without telling TypeScript what object would eventually be stored.

We encountered an error similar to:

```text
Property 'title' does not exist on type 'never'
```

The problem was caused by initializing the state as:

```tsx
useState(null)
```

without describing the eventual object shape.

We therefore defined:

```tsx
type CreatedPaper = {
  id: number;
  title: string;
  authors: string[];
  abstract: string;
  status: string;
};
```

and:

```tsx
const [createdPaper, setCreatedPaper] =
  useState<CreatedPaper | null>(null);
```

---

# 27. Step 26 — Understand the TypeScript Union

The type:

```tsx
CreatedPaper | null
```

means:

```text
createdPaper may contain:

CreatedPaper
       OR
null
```

Initially:

```text
null
```

After a successful API response:

```text
CreatedPaper
```

The `|` operator represents a **union type**.

---

# 28. Step 27 — Use Conditional Rendering for Type Safety

The frontend checks:

```tsx
{createdPaper && (
  ...
)}
```

Inside that block, TypeScript can infer that `createdPaper` is not `null`.

This is called **type narrowing**.

The mental model is:

```text
createdPaper
     │
     ▼
is it null?
  │
  ├── yes → don't render
  │
  └── no  → render CreatedPaper
```

---

# 29. Step 28 — Debug an API Contract Mismatch

During implementation, we encountered a mismatch between the property expected by the frontend and the property actually returned by the backend.

The backend returned:

```json
{
  "authors": [...]
}
```

but the frontend at one point attempted to use:

```tsx
createdPaper.authorList
```

The correct property was:

```tsx
createdPaper.authors
```

and to display the array:

```tsx
createdPaper.authors.join(", ")
```

### Engineering lesson

The frontend and backend have an **API contract**.

Both sides must agree on:

```text
field names
field types
field structure
```

A small naming mismatch can break the integration even when both the frontend and backend individually appear correct.

---

# 30. Step 29 — Handle the React Event Type

The submit handler also required an appropriate TypeScript event type.

The current project type definitions indicated that the older event typing being used was deprecated.

We therefore used:

```tsx
SubmitEvent<HTMLFormElement>
```

for the form submit handler.

The larger lesson is:

> When working with typed frameworks, check the actual types provided by the version of the libraries installed in the project instead of blindly copying an outdated tutorial.

---

# 31. Step 30 — Test the Complete Flow

At this point, the complete feature was tested from the browser.

Example input:

```text
Title:
Attention Is All You Need

Authors:
Ashish Vaswani, Noam Shazeer

Abstract:
A paper about transformer architectures.
```

The browser sends:

```text
POST http://localhost:8000/papers
```

The backend validates the request and returns:

```json
{
  "id": 1,
  "title": "Attention Is All You Need",
  "authors": [
    "Ashish Vaswani",
    "Noam Shazeer"
  ],
  "abstract": "A paper about transformer architectures.",
  "status": "created"
}
```

The frontend then stores and renders the response.

---

# 32. Step 31 — Deliberately Test Invalid Input

A valid request uses:

```json
{
  "authors": ["Oditi"]
}
```

We deliberately tested an invalid structure such as:

```json
{
  "authors": "Oditi"
}
```

The backend returned HTTP:

```text
422
```

because:

```python
authors: list[str]
```

requires a list of strings, not a single string.

---

# 33. Step 32 — Understand What the `422` Demonstrated

The request lifecycle was:

```text
Frontend sends JSON
        │
        ▼
FastAPI receives request
        │
        ▼
Pydantic validates against PaperCreate
        │
        ▼
Does authors match list[str]?
        │
       NO
        │
        ▼
HTTP 422
```

This demonstrated that the backend is enforcing its own schema.

### Important engineering principle

Frontend validation is useful for:

```text
User experience
Immediate feedback
```

Backend validation is necessary for:

```text
Correctness
Security
Data integrity
Trust boundary
```

A backend must never assume that every request came through the application's own frontend.

---

# 34. Step 33 — Verify the Browser/Frontend Logs

Refreshing the frontend produces a new request to the Next.js server.

For example:

```text
GET / 200
```

Each refresh represents a new HTTP request/response lifecycle.

This reinforces an important concept:

```text
Browser
   │
   │ GET /
   ▼
Next.js
   │
   │ 200
   ▼
Browser
```

The development logs are useful evidence when debugging whether a request actually reached the server.

---

# 35. Step 34 — Verify the Backend Logs

Similarly, when the frontend sends:

```text
POST /papers
```

the FastAPI/Uvicorn terminal records the request.

This gives us two useful observation points:

```text
Frontend terminal
        │
        ▼
Did the frontend process the request?

Backend terminal
        │
        ▼
Did the request reach FastAPI?
```

When debugging distributed components, inspect the logs at each boundary rather than guessing.

---

# 36. What Was Actually Built on Day 3

The completed Day 3 vertical slice is:

```text
                         RESEARCHOS
                             │
                             ▼
                    Next.js / React
                             │
                    Controlled Form
                             │
                       React State
                             │
                       handleSubmit()
                             │
                          fetch()
                             │
                      HTTP POST /papers
                             │
                             ▼
                       FastAPI Backend
                             │
                       Pydantic Model
                             │
                          Validation
                             │
                             ▼
                     create_paper()
                             │
                       JSON Response
                             │
                             ▼
                       response.json()
                             │
                       setCreatedPaper()
                             │
                             ▼
                      React Re-render
                             │
                             ▼
                         Browser
```

This is the first meaningful **full-stack vertical slice** of ResearchOS.

---

# 37. Important: What Is NOT Implemented Yet

The following were **not implemented as part of this Day 3 full-stack slice**:

- Database persistence
- SQLite
- PostgreSQL
- LLM integration
- Embeddings
- FAISS
- RAG
- Agentic workflows
- Tool calling
- LangChain
- LangGraph
- OpenAlex integration
- Google Scholar verification
- OCR
- LaTeX/BibTeX export
- Authentication
- Docker
- AWS deployment

These are future stages.

This distinction is important for both engineering documentation and resume accuracy.

---

# 38. Step 35 — Reassess the Project After the First Vertical Slice

After the full-stack slice was working, the project was reassessed against the larger objective.

The original long-term vision for ResearchOS is substantially broader than a CRUD application.

The intended product is an AI-powered research system capable of working with papers, retrieving relevant information, grounding answers in sources, and eventually assisting with research workflows.

Therefore, simply spending the next several days adding ordinary CRUD functionality would not provide the highest learning value.

The project was therefore strategically redirected toward an AI-focused MVP.

---

# 39. Step 36 — Define the Immediate MVP

The immediate MVP direction was defined as:

```text
User
  │
  ▼
Upload research papers
  │
  ▼
Extract PDF text
  │
  ▼
Split into chunks
  │
  ▼
Create embeddings
  │
  ▼
FAISS similarity search
  │
  ▼
Retrieve relevant passages
  │
  ▼
LLM
  │
  ▼
Grounded answer
  │
  ▼
Citation metadata
  │
  ▼
OpenAlex
  │
  ▼
Verification destination
  │
  ▼
LaTeX/BibTeX export
```

This is a **planned MVP architecture**, not a claim that all of these components were completed on Day 3.

---

# 40. Immediate MVP Technology Direction

The proposed MVP stack was deliberately simplified to reduce unnecessary framework overhead.

```text
Frontend
HTML + CSS + JavaScript

Backend
Python + FastAPI

PDF Processing
PyMuPDF

Embeddings
Embedding model

Vector Search
FAISS

Scholarly Metadata
OpenAlex

LLM
LLM API/model

Export
Python-generated LaTeX/BibTeX
```

The following were deliberately postponed for the immediate MVP:

```text
React
C#
Docker
PostgreSQL
Authentication
Complex agent orchestration
```

### Why simplify?

The purpose of the first AI MVP is to understand the actual data flow:

```text
PDF
 ↓
Text
 ↓
Chunks
 ↓
Embeddings
 ↓
Vector Search
 ↓
Retrieved Context
 ↓
LLM
 ↓
Grounded Answer
 ↓
Citations
```

Adding multiple frameworks before understanding this pipeline would obscure the architecture.

---

# 41. Step 37 — Define the MVP User Flow

The target user flow is:

## 1. Upload papers

```text
paper1.pdf
paper2.pdf
paper3.pdf
```

## 2. Ask a research question

For example:

```text
Compare how ViT and Swin Transformer handle attention.
```

## 3. Retrieve relevant passages

Conceptually:

```text
ViT paper
  Page 4
     ↓
Relevant passage

Swin paper
  Page 5
     ↓
Relevant passage
```

## 4. Generate a grounded answer

Conceptually:

```text
ViT applies global self-attention across image patches [1].

Swin Transformer restricts self-attention to local windows
and shifts these windows between successive layers [2].
```

## 5. Display sources

```text
[1] Dosovitskiy et al., 2021
    Page 4
    DOI: ...
    Verify

[2] Liu et al., 2021
    Page 5
    DOI: ...
    Verify
```

## 6. Export selected material

The user should eventually be able to select part of the generated answer and produce:

```text
.tex
.bib
```

---

# 42. Step 38 — Define the AI Learning Flow Before Implementing It

The implementation should follow:

```text
CONCEPT
   ↓
WHY DO WE NEED IT?
   ↓
TINY EXAMPLE
   ↓
IMPLEMENT IT
   ↓
RUN IT
   ↓
BREAK / MODIFY IT
   ↓
UNDERSTAND IT
   ↓
MOVE ON
```

This is important because the goal is not merely:

> "Make the RAG application work."

The goal is:

> "Understand enough of the system that I can explain and rebuild a simplified version independently."

---

# 43. Step 39 — Learn the PDF Pipeline

The first AI pipeline component will be PDF processing.

Planned flow:

```text
PDF
 ↓
PyMuPDF
 ↓
Pages
 ↓
Extracted text
```

The application should preserve page provenance:

```python
{
    "page": 4,
    "text": "..."
}
```

### Why preserve the page?

Because page information later becomes part of citation provenance.

Without provenance:

```text
Retrieved text
```

is not enough for a research-oriented application.

We need:

```text
Retrieved text
+
paper identity
+
page
```

---

# 44. Step 40 — Learn Chunking and Embeddings

Planned transformation:

```text
Paper
 ↓
Chunks
 ↓
Embedding model
 ↓
Numerical vectors
```

For example:

```text
"text about self-attention"
          ↓
embedding model
          ↓
[0.12, -0.43, 0.81, ...]
```

The key conceptual idea is:

> Embeddings represent text as numerical vectors in a space where semantic relationships can be compared mathematically.

---

# 45. Step 41 — Learn Vector Search

Planned architecture:

```text
Chunks
  │
  ▼
Embeddings
  │
  ▼
FAISS
```

When a user asks a question:

```text
Question
  │
  ▼
Question embedding
  │
  ▼
Similarity search
  │
  ▼
Top-K relevant chunks
```

This is the retrieval component of RAG.

---

# 46. Step 42 — Learn RAG

The target RAG pipeline is:

```text
User Question
      │
      ▼
Query Embedding
      │
      ▼
Vector Search
      │
      ▼
Top-K Relevant Chunks
      │
      ▼
Context Construction
      │
      ▼
LLM
      │
      ▼
Grounded Answer
```

The important concepts to understand are:

- Why documents are chunked.
- What embeddings represent.
- What similarity search does.
- What Top-K means.
- What context means.
- Why retrieval helps reduce hallucination.
- Why retrieval does not magically eliminate hallucination.
- How retrieved context is placed into the prompt.
- How citations are connected to retrieved evidence.

---

# 47. Step 43 — Keep Citation Metadata Deterministic

A major architectural rule was established:

> **The LLM should not be responsible for inventing bibliographic metadata.**

Instead:

```text
Retrieved paper
      │
      ▼
Application
      │
      ├── title
      ├── authors
      ├── year
      ├── DOI
      ├── paper identifier
      ├── page
      └── source passage
```

The LLM generates the answer.

The application resolves and supplies citation metadata.

This separates:

```text
Probabilistic generation
```

from:

```text
Deterministic bibliographic data
```

---

# 48. Step 44 — Use OpenAlex for Scholarly Metadata

The planned citation-resolution layer uses OpenAlex.

Conceptually:

```text
Paper / citation information
          │
          ▼
HTTP request
          │
          ▼
OpenAlex API
          │
          ▼
JSON
          │
          ▼
Python dictionary
          │
          ▼
Citation object
```

The important engineering lesson is that an external API is simply another system boundary.

We need to understand:

```text
request
→ response
→ JSON
→ parsing
→ application object
```

---

# 49. Step 45 — Treat Google Scholar as a Verification Destination

The intended MVP does **not** require scraping Google Scholar.

Instead:

```text
OpenAlex
→ scholarly metadata resolution

Google Scholar
→ user-facing verification destination
```

This distinction should be documented clearly in the final README.

The system should allow the user to independently verify the source rather than pretending the application itself is Google Scholar.

---

# 50. Step 46 — Keep LaTeX Export Deterministic

The planned export flow is:

```text
Selected answer text
       +
Citation objects
       │
       ▼
Python formatter
       │
       ├── .tex
       └── .bib
```

For example, selected content could eventually become:

```latex
\[
ViT applies global self-attention across image patches
\cite{dosovitskiy2021image}.
\]
```

with a corresponding BibTeX entry.

### Engineering principle

Do not use an LLM for a deterministic formatting task that ordinary program logic can perform reliably.

---

# 51. Step 47 — Keep the Immediate MVP Simple

The immediate MVP deliberately avoids unnecessary infrastructure.

The initial target is:

```text
PDF
 ↓
In-memory document representation
 ↓
FAISS
 ↓
RAG
```

A database may be added later if time permits.

### Why?

The primary learning bottleneck is currently:

```text
Python
 → API
 → PDF
 → embeddings
 → vector search
 → RAG
 → citations
 → export
```

not database engineering.

Once the AI pipeline is understood, persistence can be introduced deliberately.

---

# 52. Step 48 — Do Not Introduce Agents Just to Call the System "Agentic"

The immediate MVP does **not** require agents.

The first objective is to understand a deterministic RAG pipeline:

```text
Question
 ↓
Retrieve
 ↓
Construct context
 ↓
Generate
 ↓
Cite
```

Only when a genuine multi-step decision/problem appears should an agentic workflow be considered.

For example:

```text
User Goal
 ↓
LLM decides whether retrieval is required
 ↓
Tool call
 ↓
Tool result
 ↓
LLM
 ↓
Next action or final answer
```

The project should not use an agent merely because agentic AI is fashionable.

---

# 53. Step 49 — Deliberately Postpone Framework Abstraction

The initial AI implementation should preferably expose the underlying mechanism directly.

For example:

```text
Python
 ↓
embedding model
 ↓
FAISS
 ↓
retrieval
 ↓
prompt construction
 ↓
LLM
```

Only later should frameworks such as:

```text
LangChain
LangGraph
```

be introduced if they solve an actual orchestration problem.

### General lesson

> Understand the mechanism before adopting the abstraction.

This makes debugging, architecture discussions, and interviews substantially easier.

---

# 54. Step 50 — Define the MVP Frontend

The first AI frontend can remain extremely simple.

Conceptually:

```text
┌───────────────────────────────┐
│          ResearchOS           │
├───────────────────────────────┤
│                               │
│ Upload Paper                  │
│ [ Choose PDF ] [ Upload ]     │
│                               │
│ Ask Research Question         │
│                               │
│ [_________________________]   │
│                    [ Ask ]    │
│                               │
│ Answer                        │
│ ────────────────────────────  │
│ ...                           │
│                               │
│ Sources                       │
│ [1] Paper — Page 4            │
│     [Verify]                  │
│                               │
│ [Export Selected as LaTeX]    │
└───────────────────────────────┘
```

The purpose is to validate the end-to-end research workflow, not to spend the majority of the MVP time on frontend styling.

---

# 55. Step 51 — Define Meaningful Tests

The eventual MVP should include tests for the core deterministic components.

Examples:

```text
✓ PDF extraction
✓ Page-number preservation
✓ Chunking
✓ Invalid PDF upload
✓ Retrieval
✓ Citation resolution
✓ LaTeX generation
```

The exact test suite will depend on what is actually implemented.

Do not claim tests were written until they exist.

---

# 56. Step 52 — Establish the End-of-Day Checkpoint

Before ending the day:

1. Stop adding new features.
2. Run the application.
3. Verify the implemented feature.
4. Inspect the Git diff.
5. Update documentation.
6. Commit the work.
7. Push to GitHub.
8. Confirm the repository state.

Move to the project root:

```powershell
cd D:\Resume\_Projects\ResearchOS
```

Check status:

```powershell
git status
```

Review changes:

```powershell
git diff
```

Stage:

```powershell
git add .
```

Check staged changes:

```powershell
git status
```

Commit:

```powershell
git commit -m "Day 3: add paper creation API and frontend form flow"
```

Push:

```powershell
git push
```

Verify:

```powershell
git status
```

Expected final state:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

### Important

Never write:

> "Git is clean"

without actually running:

```powershell
git status
```

---

# 57. Step 53 — Stop the Development Servers

When the day's work is complete:

### Frontend

In Terminal 2:

```text
Ctrl + C
```

### Backend

In Terminal 1:

```text
Ctrl + C
```

### Deactivate Python environment

```powershell
deactivate
```

This does not delete `.venv`.

It only removes the virtual environment from the current terminal session.

---

# 58. Step 54 — Starting the Project Again

This section is intentionally included because Day 3 should become a reusable guide for future projects.

Whenever returning to ResearchOS:

### Terminal 1 — Backend

```powershell
cd D:\Resume\_Projects\ResearchOS\backend

.\.venv\Scripts\Activate.ps1

uvicorn main:app --reload
```

### Terminal 2 — Frontend

```powershell
cd D:\Resume\_Projects\ResearchOS\frontend

npm run dev
```

Then open:

```text
http://localhost:3000
```

---

# 59. Generalizable Workflow Learned From Day 3

The most important value of today's work is not the specific `/papers` endpoint.

It is the development workflow.

For a brand-new software project in the future, the process should be:

```text
1. Define the product problem
        ↓
2. Define the smallest useful feature
        ↓
3. Define the data flow
        ↓
4. Establish the project structure
        ↓
5. Build one component at a time
        ↓
6. Test each boundary independently
        ↓
7. Connect the components
        ↓
8. Verify the complete vertical slice
        ↓
9. Intentionally break/test failure cases
        ↓
10. Debug from evidence, not guesses
        ↓
11. Document what actually happened
        ↓
12. Commit a known-good checkpoint
        ↓
13. Only then expand the architecture
```

This is more reusable than memorizing how to create a particular FastAPI endpoint.

---

# 60. Generalizable Lesson — Build Vertical Slices

A common beginner mistake is to build an entire layer before connecting it:

```text
Build entire frontend
        ↓
Build entire backend
        ↓
Build database
        ↓
Finally connect everything
```

A better approach is often:

```text
Small UI
  ↓
Small API
  ↓
Small data flow
  ↓
Test
  ↓
Expand
```

Day 3 followed this second approach.

We built:

```text
Paper form
   +
POST /papers
   +
validation
   +
response rendering
```

rather than attempting the entire ResearchOS backend.

---

# 61. Generalizable Lesson — Define Contracts Early

Before connecting two components, define what they exchange.

In Day 3:

```python
class PaperCreate(BaseModel):
    title: str
    authors: list[str]
    abstract: str
```

became the backend request contract.

The frontend then transformed its data to satisfy that contract.

This pattern generalizes to:

```text
Frontend ↔ Backend
Backend ↔ Database
Backend ↔ External API
Retriever ↔ LLM
Service A ↔ Service B
```

Before debugging an integration, ask:

> "What exact data does each side expect and what exact data is actually being sent?"

---

# 62. Generalizable Lesson — Debug at Boundaries

The Day 3 debugging process can be generalized as:

```text
Component A
    │
    │ boundary
    ▼
Component B
```

Verify:

1. Did A produce the expected output?
2. Did the output cross the boundary?
3. Did B receive it?
4. Did B interpret it correctly?
5. Did B produce the expected output?

For ResearchOS:

```text
React
  ↓
HTTP
  ↓
FastAPI
  ↓
Pydantic
  ↓
Python
```

For a future RAG system:

```text
PDF parser
  ↓
chunker
  ↓
embedding model
  ↓
vector store
  ↓
retriever
  ↓
prompt
  ↓
LLM
```

---

# 63. Generalizable Lesson — Test Failure Cases Intentionally

A system that works only for valid input has not been sufficiently tested.

Day 3 deliberately tested:

```text
authors = "Oditi"
```

against:

```python
authors: list[str]
```

and observed:

```text
422
```

This is useful because the failure confirms that validation is actually functioning.

For future projects, deliberately test:

```text
valid input
empty input
wrong type
missing field
unexpected field
large input
network failure
server error
malformed response
```

where relevant.

---

# 64. Generalizable Lesson — Separate Deterministic and Probabilistic Logic

The future ResearchOS MVP contains both:

### Probabilistic

```text
LLM
```

and:

### Deterministic

```text
PDF extraction
chunking
vector search
citation metadata
LaTeX formatting
API parsing
validation
```

The engineering goal is not to make the LLM responsible for everything.

Use ordinary program logic where deterministic behaviour is sufficient.

Use an LLM where language understanding/generation is actually required.

This distinction will become increasingly important as ResearchOS becomes more complex.

---

# 65. Generalizable Lesson — Do Not Add Technology Without a Problem

The Day 3 architecture deliberately avoided immediately introducing:

```text
PostgreSQL
Docker
C#
LangChain
LangGraph
Authentication
Microservices
```

The correct question is not:

> "What technologies can I put in my project?"

It is:

> "What problem does this technology solve, and do I have that problem yet?"

This is a core engineering mindset.

---

# 66. Generalizable Lesson — Learn the Primitive Before the Framework

For example, before using an agent framework, understand:

```text
LLM
 ↓
tool decision
 ↓
tool call
 ↓
tool result
 ↓
LLM
```

Before using a RAG framework, understand:

```text
document
 ↓
chunk
 ↓
embedding
 ↓
vector search
 ↓
retrieved context
 ↓
LLM
```

Before using an ORM, understand:

```text
application
 ↓
SQL
 ↓
database
```

Frameworks should make already-understood concepts easier to manage, not hide concepts that were never understood.

---

# 67. Generalizable Lesson — Documentation Should Record Actions, Not Just Outcomes

A useful engineering journal should answer:

```text
What did I do?
Why did I do it?
What command/code did I use?
What happened?
What failed?
Why did it fail?
How did I fix it?
How did I verify the fix?
What did I learn?
What is the next step?
```

For example, instead of writing:

> "Configured FastAPI."

record:

```text
1. Opened backend/main.py.
2. Imported FastAPI.
3. Created app = FastAPI().
4. Added GET /.
5. Started Uvicorn with --reload.
6. Opened localhost:8000.
7. Verified the JSON response.
8. Inspected the 200 response in the server logs.
```

This style makes the document useful when rebuilding a project months later.

---

# 68. Concepts Learned

## Backend

- FastAPI
- Pydantic
- Request schemas
- API endpoints
- HTTP POST
- HTTP request bodies
- JSON responses
- HTTP status codes
- HTTP 422 validation errors
- API contracts

## Frontend

- React state
- `useState`
- Controlled inputs
- Forms
- Form submission
- `preventDefault()`
- Conditional rendering
- Loading state
- Error state
- API response state

## JavaScript / TypeScript

- Objects
- Arrays
- `.split()`
- `.map()`
- `.trim()`
- `JSON.stringify()`
- `response.json()`
- `async`
- `await`
- `try`
- `catch`
- `finally`
- `response.ok`
- Type aliases
- Union types
- Type narrowing
- Typed event handlers

## Full-Stack Engineering

- Frontend–backend communication
- HTTP request–response lifecycle
- API contracts
- Boundary debugging
- Backend validation
- Error handling
- Vertical slices
- Baseline verification

## AI Architecture — Planned Next Stage

- PDF extraction
- Page-level provenance
- Chunking
- Embeddings
- Vector search
- FAISS
- RAG
- Citation grounding
- Scholarly metadata
- OpenAlex
- LaTeX/BibTeX generation

These AI concepts were established as the next MVP direction; they should not be marked as implemented until the corresponding code exists.

---

# 69. Interview Questions

## Q1. Why did you use POST instead of GET for `/papers`?

### Strong Answer

`POST` is appropriate because the client is sending data to the server to create a new resource. A GET request would normally be used to retrieve existing resources.

### Follow-up

What would you use for updating a paper?

---

## Q2. Why do you need Pydantic if the frontend already validates the form?

### Strong Answer

Frontend validation improves user experience, but the backend cannot trust the client. Requests can come from other clients, scripts, malicious users, or buggy code. Therefore the backend needs independent validation at its trust boundary.

---

## Q3. Why did FastAPI return HTTP 422?

### Strong Answer

The request body did not match the Pydantic schema. The API expected `authors` to be a `list[str]`, but the test request supplied a string.

---

## Q4. Why did you convert the authors string into a list?

### Strong Answer

The frontend uses a simple text input for usability, while the backend's data model represents authors as a list. I therefore transformed the user-facing representation into the API's expected representation before sending the request.

---

## Q5. Why use `JSON.stringify()`?

### Strong Answer

The frontend has a JavaScript object, but the HTTP request body is being sent as JSON. `JSON.stringify()` serializes the JavaScript object into JSON text.

---

## Q6. Why use `response.json()`?

### Strong Answer

The HTTP response contains a JSON body. `response.json()` reads and parses that body so the frontend can work with it as a JavaScript object.

---

## Q7. Why do you need `response.ok`?

### Strong Answer

`fetch()` does not automatically reject its promise for normal HTTP error status codes such as 400, 404, or 500. I therefore explicitly check `response.ok` and throw an error when the HTTP response indicates failure.

---

## Q8. Why is `loading` stored in React state?

### Strong Answer

The UI needs to change while the asynchronous request is running. Storing loading status in state allows React to re-render and display appropriate feedback.

---

## Q9. Why use `finally`?

### Strong Answer

The loading state needs to be reset whether the request succeeds or fails. `finally` provides a single cleanup location that executes in both cases.

---

## Q10. What is an API contract?

### Strong Answer

It is the agreed structure and behaviour of data exchanged between components. In this case, the frontend and backend must agree on fields such as `title`, `authors`, and `abstract`, including their names and types.

---

## Q11. Why did TypeScript complain about `createdPaper.title`?

### Strong Answer

The state was initially inferred from `null`, so TypeScript did not know the shape of the eventual object. Defining a `CreatedPaper` type and using `CreatedPaper | null` explicitly described both possible states.

---

## Q12. What is a union type?

### Strong Answer

A union type allows a value to have one of several types. `CreatedPaper | null` means the state can contain either a `CreatedPaper` object or `null`.

---

## Q13. What is type narrowing?

### Strong Answer

TypeScript can reduce a broader union type to a more specific type after a runtime check. In `{createdPaper && (...)}`, TypeScript can infer that the value is not null inside the rendered block.

---

## Q14. What is a vertical slice?

### Strong Answer

A vertical slice is a small feature implemented across the necessary layers of a system. Day 3's paper creation feature crossed the React frontend, HTTP layer, FastAPI endpoint, validation layer, and response rendering rather than building each layer independently.

---

## Q15. How would RAG fit into ResearchOS?

### Strong Answer

A user query would be converted into an embedding, used to retrieve relevant paper chunks from a vector index such as FAISS, and those retrieved passages would be supplied as context to an LLM. The application would preserve document and page provenance so the generated answer could be grounded in source material.

---

## Q16. Why should citation metadata not be generated freely by the LLM?

### Strong Answer

Bibliographic metadata is structured information that can be resolved deterministically. Letting an LLM invent titles, DOIs, authors, or other metadata creates unnecessary hallucination risk. The application should retrieve and validate citation metadata from a scholarly source and use the LLM primarily for language generation.

---

# 70. Architecture at the End of the Completed Day 3 Work

The implemented architecture is:

```text
Browser
    │
    ▼
Next.js / React
    │
    │ Form data
    ▼
React State
    │
    │ JSON
    ▼
HTTP POST /papers
    │
    ▼
FastAPI
    │
    ▼
Pydantic Validation
    │
    ▼
Python Endpoint
    │
    ▼
JSON Response
    │
    ▼
React State
    │
    ▼
Browser
```

The planned AI architecture is:

```text
PDF
 │
 ▼
PyMuPDF
 │
 ▼
Page-aware text
 │
 ▼
Chunks
 │
 ▼
Embeddings
 │
 ▼
FAISS
 │
 ▼
Relevant passages
 │
 ▼
LLM
 │
 ▼
Grounded answer
 │
 ├──────────────► Citation metadata
 │                         │
 │                         ▼
 │                      OpenAlex
 │
 ▼
LaTeX / BibTeX export
```

---

# 71. Reflection

Day 3 moved ResearchOS from a project with a basic frontend–backend connection to a project with its first complete application-level vertical slice.

The most important achievement was not the paper form itself. It was understanding the complete path:

```text
User input
    ↓
React state
    ↓
JavaScript object
    ↓
JSON
    ↓
HTTP POST
    ↓
FastAPI
    ↓
Pydantic validation
    ↓
Python function
    ↓
JSON response
    ↓
React state
    ↓
UI
```

The debugging work was equally important. The `422` validation error demonstrated why backend validation is necessary. The `authors`/`authorList` mismatch demonstrated the importance of API contracts. The TypeScript `never` error demonstrated why frontend state needs an explicit type when its eventual shape is not known at initialization.

The second major outcome was architectural reassessment. Instead of continuing indefinitely with basic CRUD, ResearchOS was redirected toward an AI-focused MVP centred around:

```text
PDF
 ↓
Extraction
 ↓
Chunking
 ↓
Embeddings
 ↓
FAISS
 ↓
RAG
 ↓
Grounded Answer
 ↓
Citation Provenance
 ↓
Scholarly Metadata
 ↓
Export
```

This direction is intentionally documented as a **planned next stage**, not as completed functionality.

---

# 72. End-of-Day Checklist

Before considering Day 3 complete:

- [ ] Backend starts successfully.
- [ ] Frontend starts successfully.
- [ ] Paper form renders.
- [ ] Title can be entered.
- [ ] Authors can be entered.
- [ ] Abstract can be entered.
- [ ] Authors are transformed from string to `string[]`.
- [ ] `POST /papers` is called.
- [ ] FastAPI receives the request.
- [ ] Pydantic validates the request.
- [ ] Valid request returns successfully.
- [ ] Invalid request produces an expected validation error.
- [ ] Loading state works.
- [ ] Error state works.
- [ ] Backend response is parsed.
- [ ] Created paper is stored in React state.
- [ ] Created paper is displayed.
- [ ] TypeScript errors are resolved.
- [ ] `git status` has been checked.
- [ ] Changes have been reviewed.
- [ ] Changes have been committed.
- [ ] Changes have been pushed.
- [ ] Final Git status has been verified.
- [ ] Day 3 documentation has been updated.

---

# 73. The Reusable Project-Building Template

For future projects, the most reusable procedure from Day 3 is:

```text
PROJECT IDEA
     │
     ▼
Define the smallest useful feature
     │
     ▼
Write the expected data flow
     │
     ▼
Establish the current baseline
     │
     ▼
Implement the backend contract
     │
     ▼
Test backend independently
     │
     ▼
Implement the frontend input
     │
     ▼
Transform frontend data
     │
     ▼
Connect through HTTP
     │
     ▼
Handle success/loading/error states
     │
     ▼
Test invalid input deliberately
     │
     ▼
Debug each boundary
     │
     ▼
Verify complete vertical slice
     │
     ▼
Document exact actions + reasoning
     │
     ▼
Commit a known-good checkpoint
     │
     ▼
Only then add the next feature
```

This is the workflow to carry into future projects.

The goal of these Day files is therefore not only to record:

> "What I built today."

They should also preserve:

> **"How I approached building it, so that I can reproduce that engineering process when I start a completely new project in the future."**
