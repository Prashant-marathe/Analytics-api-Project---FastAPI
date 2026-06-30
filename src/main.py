from fastapi import FastAPI,status
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/user")
async def greet_user(user:str) -> HTMLResponse:
    return HTMLResponse(
        content=f"<b> Welcome {user}.</b>",
        status_code=status.HTTP_200_OK
    )