from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from .database import get_db
from .models import User
from .auth import get_current_user

router = APIRouter()
templates = Jinja2Templates(directory="chat/templates")

# Example route for chat
@router.get("/chat")
async def chat_page(request: Request, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return templates.TemplateResponse("chat.html", {"request": request, "receiver": None, "user":user})

@router.get("/chat/{receiver_username}")
async def chat_page_with_receiver(request: Request, receiver_username: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    # Fetch the receiver user from the database using the username
    receiver = db.query(User).filter_by(username=receiver_username).first()
    
    if receiver is None:
        raise HTTPException(status_code=404, detail="Receiver not found")

    return templates.TemplateResponse("chat.html", {"request": request, "receiver": receiver, "user": user})


# Logout route
@router.post("/logout")
async def logout(request: Request):
    response = RedirectResponse(url="/auth/login", status_code=302)
    response.delete_cookie(key="access_token")  # Clear the access token from cookies
    return response