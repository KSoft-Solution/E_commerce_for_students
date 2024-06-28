# import uvicorn
import datetime
from fastapi import FastAPI,status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from pydantic import BaseModel

from config.config import PORT,PROJECT_NAME
# import config.db

app = FastAPI(title=PROJECT_NAME, version="0.1.1",
              description=" E-commerce API created with FastAPI and jwt Authenticated")

class Response(BaseModel):
    # timestamp: datetime
    response:dict
    status:int
    error:bool

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/my_profile')
def get_my_name() :
    profile:dict = { 
        "name":"ashok sahu",
        "age":29,
        "job":"software engineer",
        "friends":['arup','gopal']
    }
    
    response:Response = {
        "status":status.HTTP_200_OK,
        "error":False,
        "response":profile,
        # "timestamp":datetime
    }
    
    data = jsonable_encoder(response)
    
    return JSONResponse(content=data)
    

# if __name__ == '__main__':
#     uvicorn.run('main:app', port=6000, reload=True)


