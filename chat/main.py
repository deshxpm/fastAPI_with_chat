from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .auth import router as auth_router
from .routes import router as routes_router
from .chat import router as chat_router
from .database import Base, engine

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="chat/static"), name="static")

# Setup Jinja2 templates
templates = Jinja2Templates(directory="chat/templates")

Base.metadata.create_all(bind=engine)

# Include routes from the routes and auth modules
app.include_router(routes_router)
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(chat_router, prefix="/chat", tags=["chat"])

# Home page to display login form
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
