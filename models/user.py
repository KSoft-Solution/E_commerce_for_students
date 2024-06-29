from pydantic import BaseModel

class UserResponse(BaseModel):
    response:dict
    status:int
    error:bool