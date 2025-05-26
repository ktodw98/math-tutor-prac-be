from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # origins에 명시된 출처에서의 요청을 허용
    allow_credentials=True,  # 쿠키를 포함한 요청을 허용할지 여부
    allow_methods=["*"],  # 모든 HTTP 메소드 허용 (GET, POST, PUT, DELETE 등)
    allow_headers=["*"],  # 모든 HTTP 헤더 허용
)
@app.get("/")
#async def root():
def root():
    return { "message": "Hello World" }

@app.get("/home")
def home():
    return {"message":"home"}