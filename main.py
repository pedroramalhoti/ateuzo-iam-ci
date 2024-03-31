# main.py
from fastapi import FastAPI, HTTPException, Depends, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
import subprocess

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Simplificação para exemplo; em produção, use uma base de dados e hashes de senha
users_db = {
    "admin": {
        "username": "admin",
        "hashed_password": "admin",  # Em produção, use hashes de senha
        "disabled": False,
    }
}

def verify_password(plain_password, hashed_password):
    return plain_password == hashed_password  # Em produção, use bcrypt ou similar

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return user_dict
    return None

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user or not verify_password(password, user['hashed_password']):
        return False
    return user

@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password"
        )
    # Aqui você deveria retornar um token real; este é apenas um placeholder
    return {"access_token": user["username"], "token_type": "bearer"}

@app.get("/status/{email}")
async def get_status(email: str, token: str = Depends(oauth2_scheme)):
    # A lógica para verificar o status viria aqui
    return {"email": email, "status": "Simulated status"}

@app.post("/unlock/{email}")
async def unlock(email: str, token: str = Depends(oauth2_scheme)):
    # A lógica para desbloquear a conta viria aqui
    return {"email": email, "status": "Unlocked"}
