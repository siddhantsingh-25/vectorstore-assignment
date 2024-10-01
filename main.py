from typing import Generator
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from coupon_code_service.routers.coupon_router import router as COUPON_ROUTES
app = FastAPI()


# Create a new router for file routes
authenticatedRoutes = FastAPI()
authenticatedRoutes.include_router(COUPON_ROUTES, prefix="/coupon")

# Mount the router on the main app
app.mount("/", authenticatedRoutes)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {"message": "Hello world!"}
