from dotenv import load_dotenv
import os
from functools import lru_cache
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import pathlib
from .airtable import push_to_airtable


# Set base dir
BASE_DIR = pathlib.Path(__file__).parent

# Create your a pp
app = FastAPI()

# Establish templates
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# Cache the environment variable
@lru_cache
def cached_dotenv(): 
    # Load the environment vars and set the environment variable path
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path=dotenv_path)

# Get the .env
cached_dotenv()

AIRTABLE_BASE_ID = os.getenv('AIRTABLE_BASE_ID')
AIRTABLE_API_KEY = os.getenv('AIRTABLE_API_KEY')
AIRTABLE_TABLE_NAME = os.getenv('AIRTABLE_TABLE_NAME')


# Routes and fxns to handle requests to the routes
@app.get('/')
def home_view(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post('/')
def home_signup_view(request: Request, email:str=Form(...)):
    # Push the data to the airtable
    did_send = push_to_airtable(email=email, api_key=AIRTABLE_API_KEY, base_id=AIRTABLE_BASE_ID, table_name=AIRTABLE_TABLE_NAME)

    return templates.TemplateResponse("home.html", {"request": request, "submitted_email": email, "did_send": did_send})