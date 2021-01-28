from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import pathlib

# Set base dir
BASE_DIR = pathlib.Path(__file__).parent

# Create your app
app = FastAPI()

# Establish templates
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# Routes and fxns to handle requests to the routes
@app.get('/')
def home_view(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post('/')
def home_signup_view(request: Request, email:str=Form(...)):
    return templates.TemplateResponse("home.html", {"request": request, "submitted_email": email})