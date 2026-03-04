from datetime import date
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.data import PROFILE, EXPERIENCE, PROJECTS, SKILLS, EDUCATION, ARTIFACTS

BASE_DIR = Path(__file__).parent

app = FastAPI(title="Ammar Jawed — Portfolio")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

_BASE = {
    "profile": PROFILE,
    "experience": EXPERIENCE,
    "projects": PROJECTS,
    "skills": SKILLS,
    "education": EDUCATION,
    "artifacts": ARTIFACTS,
    "now": date.today().strftime("%B %Y"),
}


def ctx(active: str, **extra):
    return {**_BASE, "active": active, **extra}


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, **ctx("home")})


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request, **ctx("about")})


@app.get("/experience", response_class=HTMLResponse)
async def experience(request: Request):
    return templates.TemplateResponse("experience.html", {"request": request, **ctx("experience")})


@app.get("/portfolio", response_class=HTMLResponse)
async def portfolio(request: Request):
    return templates.TemplateResponse("portfolio.html", {"request": request, **ctx("portfolio")})
