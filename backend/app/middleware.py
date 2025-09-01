# backend/middleware.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def setup_cors(app: FastAPI):
    origins = [
        "http://localhost:5173",  # frontend בפיתוח
        # "https://your-production-url.com",  # כתובת פרודקשן בהמשך
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
