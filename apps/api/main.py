from fastapi import FastAPI
from routes.execute import router

app = FastAPI()
app.include_router(router, prefix="/v1")

@app.get("/")
def root():
    return {"status": "ok"}
