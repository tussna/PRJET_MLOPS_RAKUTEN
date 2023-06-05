from typing import List
from fastapi import Depends, FastAPI, File, UploadFile, HTTPException, Request, Form, APIRouter
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.templating import Jinja2Templates
import shutil
import os

from library.helpers import *
from routers.auth import get_credentials

from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
#print(sys.path)
               
#sys.path.append(os.path.abspath(os.path.join('..', 'common')))
#sys.path.append('~/src/Machine_Deep_Learning_Models')
from Machine_Deep_Learning_Models.common import new_df, preprocessing, remove_tmp

#sys.path.append("../../")
from Machine_Deep_Learning_Models.multimodel import prediction, saveCSV

router = APIRouter()
templates = Jinja2Templates(directory="templates/")
result_path = "results/results.csv"

@router.post("/uploadtext", response_class=HTMLResponse, tags = ['datas'], summary = "upload text product")
async def upload_custom_csv(files: List[UploadFile] = File(...)):
    for file in files:
        if file.filename.endswith(".csv"):
            with open(file.filename, "wb") as f:
                f.write(file.file.read())
            if not os.path.exists('datas/' + file.filename):
                f.close()
                shutil.move(file.filename, 'datas/datas_api_test/temp_test.csv')
            else:
                f.close()
                os.remove(file.filename)

        else:
            raise HTTPException(status_code=400, detail="Format de fichier invalide, seul csv est accepté.")

    return "Télechargement réussis ! Retour à l'accueil: http://127.0.0.1:8000/index.html "


@router.post("/uploadimages/", response_class=HTMLResponse, tags = ['datas'], summary = "upload image product")
async def upload_custom_images(request: Request, credentials: HTTPBasicCredentials = Depends(get_credentials), files: List[UploadFile] = File(...)):
    for file in files:
        valid_extensions = (".png", ".jpg", ".jpeg", ".JPG")
        if file.filename.endswith(valid_extensions):
            with open(file.filename, 'wb') as image:
                image.write(file.file.read())
            if not os.path.exists('datas/images/upload_images/' + file.filename):
                image.close()
                shutil.move(file.filename, 'datas/images/upload_images/')
            else:
                image.close()
                os.remove(file.filename)

        else:
            # Raise a HTTP 400 Exception, indicating Bad Request
            raise HTTPException(status_code=400, detail="Format de fichier invalide, seul png, jpg, jpeg sont acceptés.")

    return "Télechargement réussis ! Retour à l'accueil: http://127.0.0.1:8000/index.html"


@router.post("/predict", response_class=HTMLResponse, tags = ['model'], summary = "Predict the class of the product")
async def upload_csv(request: Request, credentials: HTTPBasicCredentials = Depends(get_credentials), file: UploadFile = File(...)):
    if file.filename.endswith(".csv"):
        with open(file.filename, "wb") as f:
            f.write(file.file.read())
        file_pred = preprocessing(file.filename)
        predictions = prediction(file_pred)
        saveCSV(file_pred, predictions)
        os.remove(file.filename)

        return "predictions sauvegardés !"
    else:
        raise HTTPException(status_code=400, detail="Format de fichier invalide, seul csv est accepté.")


@router.get("/predict", response_class = HTMLResponse, tags = ['model'], summary = "Predict the class of the product")
def get_predict(request: Request, credentials: HTTPBasicCredentials = Depends(get_credentials)):
    # score = CantModel.score(X_test, y_test)
    # return score
    # data = {
    #     "page": "Predict page"
    # }
    data = openfile("predict.md")
    return templates.TemplateResponse("predict.html", {"request": request, "data": data})

# @router.post("/custom_predict")
# async def custom_predict():
#     df = new_df()
#     predictions = prediction(df)
#     saveCSV(df, predictions)
#     remove_tmp()
#     return "predictions sauvegardés !"


# @router.get("/predictions")
# def get_result():
#     return FileResponse(path=result_path, media_type='text/csv', filename='predictions')
