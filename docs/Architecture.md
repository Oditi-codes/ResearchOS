# ResearchOS - Architecture

> This document serves as the high-level architecture guide for the ResearchOS project.
>
> It will evolve as new features are added. Rather than describing implementation details, this document focuses on the overall system design, component interactions, technology choices, and architectural decisions.

---

# Project Vision

ResearchOS is an AI-powered research operating system that helps researchers organize, search, understand and analyze research papers using modern AI techniques.

The long-term goal is to build a production-quality application that combines:

- Full Stack Software Engineering
- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Computer Vision
- Vision RAG
- OCR
- Semantic Search
- Citation Grounding
- Research Paper Management

---

# Engineering Goals

This project is being built to:

- Learn production software engineering.
- Learn AI Engineering.
- Understand modern system architecture.
- Prepare for Software Engineering interviews.
- Prepare for AI/ML Engineering interviews.
- Build a real-world application that I will personally use for research.

---

# Technology Stack

## Frontend

- Next.js
- React
- TypeScript
- Tailwind CSS
- shadcn/ui

---

## Backend

- FastAPI
- Python

---

## Database

### Current

- SQLite

### Future

- PostgreSQL

---

## Vector Database

- ChromaDB

---

## AI Stack

- Gemini API
- Embedding Model
- OCR Model
- Vision Model

---

## Cloud

- AWS

Planned services:

- EC2
- S3
- IAM
- RDS
- CloudWatch
- ECS
- Route53
- CloudFront
- Secrets Manager

---

## Version Control

- Git
- GitHub

---

# Current Project Structure

```
ResearchOS/
│
├── README.md
├── .gitignore
│
├── frontend/
│
├── backend/
│
├── docs/
│
└── assets/
```

---

# Overall System Architecture

(Currently Planned)

```
                    User
                      │
                      ▼
          Next.js Frontend
                      │
           REST API (HTTPS)
                      │
                      ▼
              FastAPI Backend
        ┌──────────┼──────────┐
        │          │          │
        ▼          ▼          ▼
    SQLite     ChromaDB    Gemini API
        │                     │
        │                     ▼
        │               LLM Response
        │
        ▼
   Metadata Storage
```

---

# Planned MVP

The first working version (MVP) of ResearchOS will include:

- PDF Upload
- PDF Storage
- Text Extraction
- Chunking
- Embedding Generation
- Vector Search
- Basic RAG Chat
- Citation Grounding
- Simple Research Library

---

# Long-Term Roadmap

Future features include:

- OCR
- Figure Extraction
- Table Extraction
- Vision RAG
- Hybrid Retrieval
- Semantic Search
- Literature Review Generation
- Research Gap Detection
- Reference Recommendation
- Knowledge Graph Integration
- User Authentication
- Notes & Highlighting
- Export to Markdown/PDF
- Docker
- CI/CD
- AWS Deployment

---

# Architectural Principles

This project will follow the following software engineering principles:

- Separation of Concerns
- Modular Design
- Clean Architecture
- Reusable Components
- Scalability
- Maintainability
- Readability
- Production-Ready Folder Structure

---

# Major Design Decisions

This section records important architectural decisions and the reasoning behind them.

---

## Decision 1

### Use FastAPI instead of Flask

**Reason**

- Better type support.
- Automatic API documentation.
- Excellent async support.
- Widely used in AI/ML backends.

Status:

✅ Finalized

---

## Decision 2

### Use SQLite first, PostgreSQL later

**Reason**

SQLite allows rapid local development without server setup.

PostgreSQL will be introduced once multi-user support and deployment become necessary.

Status:

✅ Finalized

---

## Decision 3

### Build incrementally using MVP

**Reason**

Avoid overengineering.

Every iteration should produce a working application before introducing additional complexity.

Status:

✅ Finalized

---

# Current Progress

## Day 01

Completed:

- Project initialization
- Folder structure creation
- Git repository initialization
- GitHub repository setup
- First successful push to GitHub

---

# Questions for Future Me

These are architectural questions that will be answered as the project evolves.

- Why FastAPI instead of Django?
- Why REST instead of GraphQL?
- Why ChromaDB instead of Pinecone?
- Why SQLite before PostgreSQL?
- When should Redis be introduced?
- When should Docker be introduced?
- When should authentication be added?
- How should the project scale for multiple users?
- Should AI processing be synchronous or asynchronous?