import pickle
from pickletools import anyobject
import secrets
import pandas as pd
from starlette.responses import HTMLResponse
from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from library.helpers import *
from routers.auth import *
from routers import routes

# with open("model_logistic_regression.pkl", "rb") as model_file:
#     model_logistic_regression = pickle.load(model_file)

# y_test = final_data_test["Churn"]
# X_test = final_data_test.drop(["Churn"], axis=1)


# --------------------------
description = """
Il s'agit d'une API basé sur FastAPI. C'est une solution d'une évaluation du module FastAPI de la formation MLOps de DataScientest.
Une API qui intéroge une base de données sous forme d'un fichier CSV pour retourner une série de questions.
## Fonctions
* Tester le fonctionnement de l'API
* Prédir le produit après avoir être connecté
* Créer une nouvelle question pour les utilisateur Amdin
"""

app = FastAPI(
    title = "API pour la classification de produit e-commerce", 
    description = description, 
    version = "V1",
    contact = {
        "name": "Amar Mokrani",
        "email": "amar.mokrani1@gmail.com"
    },
    openapi_tags = [
    {
        'name': 'home',
        'description': 'fonctions par défaut'
    },
    {
        'name': 'datas',
        'description': 'fonctions utilisées pour le chargement des donées'
    },
    {
        'name': 'model',
        'description': 'fonctions utilisées pour la prédictions'
    },
    # {
    #     'name': 'admin',
    #     'description': 'fonctions où on peut créer de nouvelles questions'
    # }
])
# --------------------------------------------------------------------------------------------

origins = ["*"]
methods = ["*"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = methods,
    allow_headers = headers    
)

app.include_router(routes.router)

# load static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# load templates
templates = Jinja2Templates(directory="templates")

@app.get('/status', tags = ['home'], summary = "Check the status of the api")
async def get_status():
    """Returns 1 if the app is up
    """
    return 1

@app.get("/home", response_class = HTMLResponse, tags = ['home'], summary = "Welcome to the api")
async def home(request: Request):
    data = openfile("home.md")
    return templates.TemplateResponse("home.html", {"request": request, "data": data})

@app.get("/about", response_class = HTMLResponse, tags = ['home'], summary = "About the api")
async def home(request: Request):
    data = openfile("about.md")
    return templates.TemplateResponse("about.html", {"request": request, "data": data})


