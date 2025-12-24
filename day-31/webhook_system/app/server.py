from fastapi import FastAPI, Request, Header, HTTPException
from webhook.verifier import verify_signature
from webhook.handler import handle_webhook

app = FastAPI()

@app.post("/webhook")
async def webhook(
    request: Request,
    x_signature: str = Header(None),
    x_event_id: str = Header(None),
    x_event_type: str = Header(None),
):
    raw = await request.body()

    if not verify_signature(raw, x_signature):
        raise HTTPException(status_code=401, detail="Invalid signature")

    payload = await request.json()
    handle_webhook(x_event_id, x_event_type, payload)

    return {"status": "ok"}
