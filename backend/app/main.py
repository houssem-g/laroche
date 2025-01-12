# app/main.py

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from app.routers import items, qa
from app.config import logger
import traceback
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI + GraphDB + ChatGPT Demo",
        version="0.1.0",
        description="Une application démontrant l'intégration de FastAPI, GraphDB, et ChatGPT."
    )

    origins = [
        "http://localhost:3000",
        "http://backend:8000",
        "http://frontend:3000",
        "*",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.mount("/static", StaticFiles(directory="app/static"), name="static")

    @app.middleware("http")
    async def log_requests(request: Request, call_next):
        logger.info(f"Incoming request: {request.method} {request.url}")
        try:
            response = await call_next(request)
            logger.info(f"Response status: {response.status_code}")
            return response
        except Exception as e:
            logger.error(f"Unhandled exception: {e}")
            logger.error(traceback.format_exc())
            return JSONResponse(
                status_code=500,
                content={"detail": "Internal Server Error"},
            )

    app.include_router(items.router)
    app.include_router(qa.router)
    
    @app.get("/", response_class=HTMLResponse)
    def read_root():
        with open("app/static/index.html") as f:
            return f.read()

    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
