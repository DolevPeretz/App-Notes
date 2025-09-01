# app/main.py

from fastapi import FastAPI
from app.api.routes import auth, notes
from app.db.session import engine
from app.db.models import base  

app = FastAPI(title="Notes App")

base.Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(notes.router, prefix="/notes", tags=["Notes"])

@app.get("/")
def root():
    return {"message": "Welcome to Notes App!"}








# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.openapi.utils import get_openapi

# from app.api.routes import auth, notes, users
# from app.core.config import settings
# from app.db.session import engine
# from app.db.models import base

# app = FastAPI(
#     title="Notes App",
#     version="0.1.0",
#     description="Notes API with JWT Authentication",
# )

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Create DB tables
# base.Base.metadata.create_all(bind=engine)

# # Include Routers
# app.include_router(auth.router, prefix="/auth", tags=["Auth"])
# app.include_router(notes.router, prefix="/notes", tags=["Notes"])
# app.include_router(users.router, prefix="/users", tags=["Users"])

# # Swagger Bearer Auth
# def custom_openapi():
#     if app.openapi_schema:
#         return app.openapi_schema
#     openapi_schema = get_openapi(
#         title=app.title,
#         version=app.version,
#         description=app.description,
#         routes=app.routes,
#     )
#     openapi_schema["components"]["securitySchemes"] = {
#         "BearerAuth": {
#             "type": "http",
#             "scheme": "bearer",
#             "bearerFormat": "JWT",
#         }
#     }
#     for path in openapi_schema["paths"]:
#         for method in openapi_schema["paths"][path]:
#             if method in ["get", "post", "put", "delete"]:
#                 openapi_schema["paths"][path][method]["security"] = [{"BearerAuth": []}]
#     app.openapi_schema = openapi_schema
#     return app.openapi_schema

# app.openapi = custom_openapi

# @app.get("/")
# def root():
#     return {"message": "Welcome to Notes App!"}

