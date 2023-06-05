import secrets
from fastapi import Depends, HTTPException, status 
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email: EmailStr
    password: str   

users = {
    "alice": "wonderland", 
    "bob": "builder", 
    "clementine": "mandarine"
}

security = HTTPBasic()

def get_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = credentials.username in users.keys()

    if not correct_username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect user",
            headers={"WWW-Authenticate": "Basic"},
        )

    correct_password = secrets.compare_digest(
        credentials.password, users[credentials.username]
    )
    if not correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials

def is_identified(credentials: HTTPBasicCredentials = Depends(security)):
    for user, passwd in users.items():
       if secrets.compare_digest(credentials.username, user):
           if secrets.compare_digest(credentials.password, passwd):
               return True
    return False


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    if not (is_identified(credentials)):
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Incorrect email or password",
            headers = {"WWW-Authenticate" : "Basic"},
        )
    return credentials.username


def is_admin(credentials: HTTPBasicCredentials = Depends(security)):
    
    if not secrets.compare_digest(credentials.username, "admin"):
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            detail = "Access to the requested resource is forbidden for the current user",
            headers = {"WWW-Authenticate" : "Basic"},
        )
    else :
        if not is_identified(credentials) : 
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = "Incorrect email or password",
                headers = {"WWW-Authenticate" : "Basic"},
            )
    return credentials.username