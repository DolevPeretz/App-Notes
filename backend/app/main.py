
from fastapi import FastAPI
from app.api.routes import auth, notes
from app.db.session import engine
from app.db.models import base  
from .middleware import setup_cors

app = FastAPI(title="Notes App")

base.Base.metadata.create_all(bind=engine)
setup_cors(app)
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(notes.router, prefix="/notes", tags=["Notes"])

@app.get("/")
def root():
    return {"message": "Welcome to Notes App!"}




