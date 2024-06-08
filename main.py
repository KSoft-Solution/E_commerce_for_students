import fastapi   #use this for python modules(os,date time)

from fastapi import FastAPI  #use this way for third party libraries(numpy,pandas,fastapi)

from fastapi import *  #use this way for userdefined modules

fastapi.FastAPI()

app = FastAPI(title="E-commerce API", version="0.1.1",
            description=" E-commerce API created with FastAPI and jwt Authenticated")