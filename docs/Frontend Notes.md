# Frontend Notes

> Notes covering frontend concepts learned during the ResearchOS project.
>
> Current stack:
> - Next.js
> - React
> - TypeScript
> - TailwindCSS

---

# Next.js

---

## What is Next.js?

Next.js is a React-based full-stack framework used for building modern web applications.

It provides features on top of React such as:

- Routing
- Server-side rendering
- Server Components
- Client Components
- Optimized builds
- API integration

In ResearchOS, Next.js is used for building the user interface.

---

# Next.js App Router

---

## What is App Router?

App Router is the routing system introduced in newer versions of Next.js.

Routes are created using the folder structure inside:`src/app`

Example: `src/app/page.tsx`
represents: `localhost:3000/`


---

# React Component

---

## What is a React Component?

A React Component is a reusable UI building block.

Example:

```tsx
function Home(){
    return <h1>ResearchOS</h1>
}
```
In Next.js, pages are created using React components.

---
## Server Components
---

### What are Server Components?

Server Components are React components that execute on the server.

They are the default component type in Next.js App Router.

Advantages:
- Reduced client-side JavaScript
- Better performance
- Direct server-side data fetching

---
## Client Components
---

### What are Client Components?

Client Components execute in the browser.

They are required when using:
- useState
- useEffect
- Browser APIs
- User interaction

A Client Component is marked using:

```tsx
"use client";
```

---
## React Hooks
---

### What are Hooks?

Hooks are React functions that allow components to use React features such as state and lifecycle behavior.

Examples:
- useState
- useEffect

---
### useState
---
#### What is useState?

useState is a React hook used to store changing data inside a component.

Example:
```tsx
const [message, setMessage] = useState("");
```

Here:
`message` stores the current value.

`setMessage()` updates the value.

When state changes, React automatically re-renders the component.

---
### useEffect
---

#### What is useEffect?

useEffect is a React hook used for performing side effects.

Examples:
- API calls
- Timers
- Subscriptions

In ResearchOS it is used to call the FastAPI backend after the component loads.

Example:
```tsx
useEffect(() => {
    fetch(...)
}, [])
```

#### Dependency Array

The second argument of useEffect controls execution frequency.

Example:
```tsx
useEffect(() => {

}, [])
```

An empty dependency array means:

Run only once when the component mounts.

Without it, the effect may run after every render.

---
## Fetch API
---

### What is fetch()?

`fetch()` is a JavaScript API used to make HTTP requests.

Example:

```tsx
fetch("http://localhost:8000/")
```

This sends a request to the FastAPI backend.

### Why is fetch asynchronous?

Network requests take unpredictable time because they depend on:

Network latency
Server processing
Response time

Therefore fetch returns a Promise instead of an immediate response.

---
## Promise
---

### What is a Promise?

A Promise represents a value that will be available in the future.

Example:
```tsx
const response = fetch(url)
```

returns:
```tsx
Promise<pending>
```
After completion:
```tsx
HTTP Response
```
---
## async / await
---

### What is await?

await pauses execution until an asynchronous operation completes.

Example:
```tsx
const response = await fetch(url)
```
It waits for the HTTP response before continuing.

---

# Frontend-Backend Communication

---

## How does Next.js communicate with FastAPI?

Flow:
```md
Browser

↓

Next.js Frontend

↓

fetch()

↓

HTTP Request

↓

FastAPI Backend

↓

JSON Response
```

---
# JSX
---

## What is JSX?

JSX allows writing HTML-like syntax inside JavaScript/TypeScript.

Example:
```tsx
<h1>ResearchOS</h1>
```

React converts JSX into JavaScript instructions to create UI elements.

---
# TailwindCSS
--- 

## What is TailwindCSS?

TailwindCSS is a utility-first CSS framework.

Instead of writing separate CSS classes, styles are applied using predefined utility classes.

Example:
```tsx
className="text-4xl font-bold"
```

---
# Last Updated
---
Day 02