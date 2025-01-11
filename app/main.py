# app/main.py

from fastapi import FastAPI
from app.routers import items, qa


def create_app() -> FastAPI:
    app = FastAPI(
        title="My RDF + FastAPI Demo",
        version="0.1.0",
        description="A small example demonstrating CRUD with an RDF store."
    )

    # Include Routers
    app.include_router(items.router)
    app.include_router(qa.router)

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
