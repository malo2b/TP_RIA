from fastapi import FastAPI

from api.routes.student import student_router

# Instanciate FastAPI
app: FastAPI = FastAPI()

app.include_router(student_router)