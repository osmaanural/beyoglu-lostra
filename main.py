"""
Beyoğlu Lostra — Profesyonel Ayakkabı Tamir & Bakım
FastAPI Web Uygulaması
"""

from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# ================= APP =================

app = FastAPI(
    title="Beyoğlu Lostra",
    description="Profesyonel Ayakkabı Tamir & Bakım — Bakırköy, İstanbul",
    version="1.0.0",
)

# ================= PATHS =================

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"

# ================= STATIC FILES =================

app.mount(
    "/static",
    StaticFiles(directory=str(STATIC_DIR)),
    name="static"
)

# ================= TEMPLATES =================

templates = Jinja2Templates(
    directory=str(TEMPLATES_DIR)
)

# ================= ROUTES =================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "message": "Beyoğlu Lostra çalışıyor"
    }

# ================= LOCAL DEVELOPMENT =================

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )