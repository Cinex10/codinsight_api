from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.code_explainer.router import router as code_explainer_router
from src.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(code_explainer_router, prefix="/code-explain", tags=["Code Explanation"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Code Explanation API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)