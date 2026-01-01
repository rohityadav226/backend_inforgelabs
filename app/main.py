from fastapi import FastAPI
from app.auth.routes import router as auth_router
from app.positions.routes import router as positions_router
from app.orders.routes import router as orders_router
from fastapi.middleware.cors import CORSMiddleware
from app.pnl.routes import router as pnl_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)
app.include_router(positions_router)
app.include_router(orders_router)
app.include_router(pnl_router)
@app.get("/health")
def health():
    return {"status": "ok"}

