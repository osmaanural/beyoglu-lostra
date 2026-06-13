"""
Beyoğlu Lostra — Profesyonel Ayakkabı Tamir & Bakım
FastAPI Web Uygulaması
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI(
    title="Beyoğlu Lostra",
    description="Profesyonel Ayakkabı Tamir & Bakım — Bakırköy, İstanbul",
    version="1.0.0",
)

# Static dosyaları (CSS, JS, görseller) serve et
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 template engine
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Ana sayfa"""
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
