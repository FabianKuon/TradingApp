import sqlalchemy
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from core.stockPricesApi import router as api_router
from database.models.StockModel import Base

app = FastAPI()

origins = ["http://localhost:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

engine = sqlalchemy.create_engine(f'postgresql://{NAME}:{SURENAME}@localhost/{DBNAME}')

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    uvicorn.run("main:app", host='0.0.0.0', port=8000, log_level="info", reload=True)
    print("running")
