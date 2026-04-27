from fastapi import FastAPI, Header, Cookie

app = FastAPI()

@app.get("/info")
def get_info(
    user_agent: str = Header(None),
    session_id: str = Cookie(None)
):
    return {
        "user_agent": user_agent,
        "session_id": session_id
    }