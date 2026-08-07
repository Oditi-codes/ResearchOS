# Interview Questions

> This document contains every interview question encountered throughout the ResearchOS project.
>
> Questions are grouped by topic and continuously expanded.

---

# Table of Contents

- Git
- Software Engineering
- Backend
- Frontend
- Databases
- AI / ML
- RAG
- AWS
- DSA
- System Design

---

# Git

---

## Q1. What is Git?

### Beginner Answer

Git is a version control system used to track changes in files.

### Strong Candidate Answer

Git is a Distributed Version Control System (DVCS) that tracks project history by storing snapshots of files. It enables collaboration, branching, merging, rollback, and distributed development while allowing every developer to maintain a complete copy of the repository.

---

## Q2. What is the difference between Git and GitHub?

### Beginner Answer

Git is installed locally.

GitHub stores projects online.

### Strong Candidate Answer

Git is a distributed version control system responsible for tracking changes and managing history. GitHub is a cloud platform that hosts Git repositories and provides collaboration features such as Pull Requests, Issues, Actions, Code Reviews, and access control.

---

## Q3. What is the Staging Area?

### Beginner Answer

It stores files before committing.

### Strong Candidate Answer

The Staging Area (Index) stores snapshots of selected changes that will become the next commit. It enables developers to create atomic and meaningful commits instead of committing every modification made in the Working Directory.

---

## Q4. Why does Git have a Staging Area?

### Beginner Answer

To choose which files to commit.

### Strong Candidate Answer

The Staging Area provides fine-grained control over commits. It allows developers to stage only selected changes, improving commit quality, collaboration, debugging, and code review.

---

## Q5. Why didn't we need to run `git add` again after the failed commit?

### Beginner Answer

Because the files were already staged.

### Strong Candidate Answer

A failed commit due to missing author identity does not modify the Staging Area. The staged snapshots remain unchanged, so after configuring the Git identity, the same staged content can be committed directly.

---

## Q6. What is a Remote Repository?

### Beginner Answer

Another Git repository.

### Strong Candidate Answer

A remote repository is another Git repository that the local repository communicates with for synchronization. It can be hosted on GitHub, GitLab, Bitbucket, a company server, or another developer's machine.

---

## Q7. Is `origin` a Git keyword?

### Beginner Answer

No.

### Strong Candidate Answer

No. `origin` is simply the conventional alias assigned to the primary remote repository. Any valid alias can be used.

---

## Q8. Where does Git store remote information?

### Beginner Answer

Inside the `.git/config` file.

### Strong Candidate Answer

Git stores remote configuration inside the `.git/config` file, including fetch and push URLs, allowing commands such as `git push origin main` to resolve the correct remote repository.

---

## Q9. Why shouldn't we initialize a new GitHub repository with a README if the local repository already contains one?

### Beginner Answer

Because it creates conflicts.

### Strong Candidate Answer

Initializing the GitHub repository with a README creates an independent root commit, resulting in unrelated commit histories between the local and remote repositories. Creating an empty remote avoids this issue.

---

## Q10. What does `git push -u origin main` do?

### Beginner Answer

Uploads the project to GitHub.

### Strong Candidate Answer

It pushes the local `main` branch to the `origin` remote and establishes `origin/main` as the upstream tracking branch. This enables future `git push` and `git pull` commands to work without explicitly specifying the remote and branch.

---

# Backend

--- 

## Q1. What is FastAPI?

### Beginner Answer

FastAPI is a Python framework used to build APIs.

### Strong Candidate Answer

FastAPI is a modern Python web framework designed for building high-performance APIs using Python type hints. It provides request validation, automatic documentation, asynchronous support, and efficient HTTP request handling.

### Why Interviewers Ask

To check understanding of backend frameworks and API development.

### Common Mistake

Saying FastAPI is a database or frontend framework.

---

## Q2. What happens when a request reaches a FastAPI application?

### Beginner Answer

FastAPI executes the required function.

### Strong Candidate Answer

An incoming HTTP request is received by the FastAPI server, processed through middleware layers such as CORS, matched against registered routes, passed to the corresponding endpoint function, and the returned Python object is serialized into a response, usually JSON.

### Why Interviewers Ask

Tests understanding of request lifecycle.

---

## Q3. What is middleware?

### Beginner Answer

Middleware handles requests before they reach APIs.

### Strong Candidate Answer

Middleware is a software layer that intercepts HTTP requests and responses to implement cross-cutting concerns such as authentication, logging, CORS, monitoring, and security checks without duplicating logic across individual endpoints.

### Why Interviewers Ask

Tests backend architecture understanding.

---

## Q4. What is CORS?

### Beginner Answer

CORS allows frontend and backend communication.

### Strong Candidate Answer

CORS is a browser security mechanism that controls whether a frontend from one origin can access resources from another origin. The backend explicitly defines allowed origins through HTTP headers.

### Why Interviewers Ask

Common issue in frontend-backend integration.

---

# Frontend

---

## Q1. Difference between Server Components and Client Components in Next.js?

### Beginner Answer

Server Components run on server and Client Components run in browser.

### Strong Candidate Answer

Server Components execute on the server and reduce client-side JavaScript while allowing efficient server-side rendering. Client Components execute in the browser and are required for interactive functionality using React hooks such as useState and useEffect.

### Why Interviewers Ask

Tests modern Next.js understanding.

---

## Q2. What is useState?

### Beginner Answer

useState stores values in React.

### Strong Candidate Answer

useState is a React hook that allows functional components to maintain state. Updating state through the setter function triggers React to re-render the component with the updated value.

---

## Q3. Why is fetch() asynchronous?

### Beginner Answer

Because APIs take time to respond.

### Strong Candidate Answer

fetch() is asynchronous because network operations involve unpredictable delays. Instead of blocking JavaScript execution, it returns a Promise that resolves when the response becomes available.

---

## Q4. What is a Promise in JavaScript?

### Beginner Answer

A Promise represents future data.

### Strong Candidate Answer

A Promise is an object representing the eventual completion or failure of an asynchronous operation. It allows JavaScript to handle operations that complete later, such as API calls.

---

# Last Updated

Day 02