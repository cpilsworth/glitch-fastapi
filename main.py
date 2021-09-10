import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# work out the gitch hostname
domain = f"https://{ os.environ['PROJECT_DOMAIN'] }.glitch.me" 

app = FastAPI(root_path="/", servers=[
        {"url": domain, "description": "Glitch environment"}  
    ])

# Add CORS headers to allow calls from everywhere
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "Hello from FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}