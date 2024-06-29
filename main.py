# import uvicorn
from fastapi import FastAPI
from config.config import PROJECT_NAME

from routes.user import router

app = FastAPI(title=PROJECT_NAME, version="0.1.1",
              description=" E-commerce API created with FastAPI and jwt Authenticated")

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(router)
# if __name__ == '__main__':
#     uvicorn.run('main:app', port=6000, reload=True)


