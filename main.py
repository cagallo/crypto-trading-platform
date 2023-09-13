import random
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/{wallet_address}/balance")
def check_balance(wallet_address: str):
    print(wallet_address)
    return random.randint(1000, 10000)

@app.get("/")
def root():
    return {"message": "Hello World"}

if __name__ == '__main__': 
    uvicorn.run(app)