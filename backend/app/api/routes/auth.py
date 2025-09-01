

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserLogin, UserOut
from app.db.session import SessionLocal
from app.crud.user import authenticate_user
from app.core.security import create_access_token
from datetime import timedelta

router = APIRouter()

# Dependency – יוצרת חיבור למסד נתונים
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    print("📥 התחברות מתבצעת עם הפרטים הבאים:")
    print("   • Email:", user.email)
    print("   • Password:", user.password)

    authenticated_user = authenticate_user(db, user.email, user.password)

    if not authenticated_user:
        print("❌ התחברות נכשלה – משתמש לא נמצא או סיסמה שגויה")
        raise HTTPException(status_code=401, detail="Invalid credentials")

    print(f"✅ התחברות הצליחה! משתמש ID: {authenticated_user.id} | Email: {authenticated_user.email}")

    token = create_access_token(
        data={"sub": str(authenticated_user.id)},
        expires_delta=timedelta(minutes=60)
    )

    print("🎟️ נוצר טוקן JWT:", token)
    return {"access_token": token, "token_type": "bearer"}

