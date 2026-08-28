from fastapi import FastAPI

from app.routers import patient,pathoens,antibiotic

app=FastAPI(title="Clinical Decision Support System Backend")



app.include_router(patient.router)

app.include_router(pathogens.router)
app.include_router(antibiotic.router)


@app.get("/test")
def test():
    return{
        "message":"welcome to our clinical support system backend"
    }