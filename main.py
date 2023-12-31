import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return 'It works!'

if __name__ == '__main__':
    uvicorn.run(app)
