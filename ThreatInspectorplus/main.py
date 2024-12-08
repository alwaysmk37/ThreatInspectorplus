from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles  # Import StaticFiles for serving static files
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Serve static files from the 'static' directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load templates from the 'templates' directory (including the 'login' subdirectory)
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    # Render the index.html template
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/url")
async def contact(request: Request):
    return templates.TemplateResponse("url.html", {"request": request})

@app.get("/cve")
async def contact(request: Request):
    return templates.TemplateResponse("cve.html", {"request": request})

@app.get("/email")
async def contact(request: Request):
    return templates.TemplateResponse("email.html", {"request": request})

@app.get("/file")
async def contact(request: Request):
    return templates.TemplateResponse("file.html", {"request": request})

@app.get("/faq")
async def contact(request: Request):
    return templates.TemplateResponse("faq.html", {"request": request})

@app.get("/about")
async def contact(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/contact")
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

