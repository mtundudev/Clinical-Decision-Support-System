from fastapi import FastAPI

app=FastAPI(title="Clinical Decision Support System Backend")



@app.get("/test")
def test():
    return{
        "message":"welcome to our clinical support system backend"
    }