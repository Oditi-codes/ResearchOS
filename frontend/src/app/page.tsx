"use client";

import { SubmitEvent, useEffect, useState } from "react";

type CreatedPaper = {
  id: number;
  title: string;
  authors: string[];
  abstract: string;
  status: string;
};

export default function Home() {

  const [message, setMessage] = useState("");
  const [title, setTitle] = useState("");
  const [authors, setAuthors] = useState("");
  const [abstract, setAbstract] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [createdPaper, setCreatedPaper] = useState<CreatedPaper | null>(null);  
  
  useEffect(() => {

    fetch("http://localhost:8000/")
      .then((response) => response.json())
      .then((data) => {
        setMessage(data.message);
      });

  }, []);

  const handleSubmit = async (event: SubmitEvent<HTMLFormElement>) => {
    event.preventDefault();

    setLoading(true);
    setError("");
    
    const authorList = authors
      .split(",")
      .map((author) => author.trim());

    const paper = {
      title,
      authors: authorList,
      abstract,
    };

    try {
      const response = await fetch("http://localhost:8000/papers", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(paper), 
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      setCreatedPaper(data);
    }
    catch (error) {
      console.error("Error:", error);
      setError("Failed to create paper. Please try again.");
    }
    finally {
      setLoading(false);
    }
  };

  return (
    <main className="flex min-h-screen flex-col items-center justify-center">
      
      <h1 className="text-4xl font-bold">
        ResearchOS
      </h1>

      <p className="mt-5 text-xl">
        Backend Status:
      </p>

      <p className="mt-2 text-lg">
        {message}
      </p>

      <form onSubmit={handleSubmit}>

        <input
          type="text"
          value={title}
          onChange={(event) => setTitle(event.target.value)}
          placeholder="Enter paper title"
          className="mt-5 border p-2"
        />
        <br />
        <input
          type="text"
          value={authors}
          onChange={(event) => setAuthors(event.target.value)}
          placeholder="Enter authors separated by commas"
          className="mt-3 border p-2"
        />
        <br />
        <textarea
          value={abstract}
          onChange={(event) => setAbstract(event.target.value)}
          placeholder="Enter paper abstract"
          className="mt-3 border p-2"
        />
        <br />

        <button type="submit" className="mt-3 border p-2">
          Add Paper
        </button>

      </form>

      {loading && <p>Creating paper...</p>}

      {error && <p>{error}</p>}

      {createdPaper && (
        <div className="mt-5">
          <p>Paper created successfully!</p>
          <p>Title: {createdPaper.title}</p>
          <p>Authors: {createdPaper.authors.join(", ")}</p>
        </div>
      )}

    </main>
  );
}