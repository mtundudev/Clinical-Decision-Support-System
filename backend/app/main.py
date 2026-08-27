from fastapi import FastAPI
from app.routers import patient

app=FastAPI(title="Clinical Decision Support System Backend")



app.include_router(patient.router)


@app.get("/test")
def test():
    return{
        "message":"welcome to our clinical support system backend"
    }