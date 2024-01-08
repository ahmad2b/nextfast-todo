# Next Fast ToDo App

This is a full-stack ToDo application built with Next.js on the frontend and FastAPI on the backend.

## Features

- Multi-tenant (todo)
- JWT Auth (todo)
- Streamlit client
- Python Console client
- Typescript Node.js client
- Next.js client
- pytests

## Frontend

The frontend of the application is built with [Next.js](https://nextjs.org/)

### Techstack

- Next.js
- TailwindCSS
- ShadCn UI
- zod
- react-hook-form

## Backend

The backend of the application is built with FastAPI, a modern, fast (high-performance), web framework for building APIs.

### Techstack

- FastAPI,
- PostgresSQL
- psycopg2
- SQLAlchemy
- Pytest
- requests

## Interaction between Frontend and Backend

The frontend interacts with the backend through HTTP requests. When a user performs an action on the frontend (like creating a ToDo), a request is sent to the backend. The backend processes the request, performs the necessary database operations, and sends a response back to the frontend.

The frontend then updates the UI based on the response from the backend. This allows for a dynamic and interactive user experience.
