

from app.db.session import SessionLocal
from app.schemas.user import UserCreate
from app.crud.user import create_user, get_user_by_email

db = SessionLocal()

user_data = UserCreate(
    email="dolev@example.com",
    password="dolev"
)

existing = get_user_by_email(db, user_data.email)

if existing:
    print(f"User already exists: {existing.email}")
else:
    user = create_user(db, user_data)
    print(f"User created: {user.email}")
