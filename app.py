from fastapi import FastAPI
from src.controllers.userController import router as user_router
from src.controllers.messageController import router as message_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(user_router, prefix="/api")
app.include_router(message_router, prefix="/api")





