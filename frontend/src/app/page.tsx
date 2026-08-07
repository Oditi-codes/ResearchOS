"use client";

import { useEffect, useState } from "react";

export default function Home() {

  const [message, setMessage] = useState("");

  useEffect(() => {

    fetch("http://localhost:8000/")
      .then((response) => response.json())
      .then((data) => {
        setMessage(data.message);
      });

  }, []);


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

    </main>
  );
}