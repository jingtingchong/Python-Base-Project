import uvicorn
import os
from fastapi import FastAPI
from service_provider.api.entrypoint.employee import employee_router

# Initialise FastAPI application server
app = FastAPI()

@app.get("/")
def greetings():
    return {"Welcome to Jing Ting's API!"}

# Register routers
app.include_router(employee_router)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

# uvicorn service_provider.api.main:app --reload
