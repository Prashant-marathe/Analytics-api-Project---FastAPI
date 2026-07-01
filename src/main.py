from fastapi import FastAPI,status
from fastapi.responses import HTMLResponse
from api.events import event_router



version = "v1"
app = FastAPI(
    title = "Analytics API",
    description="",
    version=version,
    docs_url=f"/api/{version}/docs",
    redoc_url=f"/api/{version}/redoc"
)

app.include_router(event_router, prefix=f"/api/{version}/events", tags=["events"])

@app.get("/user")
async def greet_user(user:str) -> HTMLResponse:
    return HTMLResponse(
        content=f"<b> Welcome {user}.</b>",
        status_code=status.HTTP_200_OK
    )

@app.get("/healthz")
async def read_api_health():
    return {"status": "ok"}