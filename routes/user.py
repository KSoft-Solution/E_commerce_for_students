from fastapi import APIRouter,status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from models.user import UserResponse

router = APIRouter()

@router.get('/my_profile')
def get_my_name() :
    profile:dict = { 
        "name":"kanha sahu",
        "age":29,
        "job":"software engineer",
        "friends":['arup','gopal']
    }
    
    response:UserResponse = {
        "status":status.HTTP_200_OK,
        "error":False,
        "response":profile,
    }
    
    data = jsonable_encoder(response)
    
    return JSONResponse(content=data)

