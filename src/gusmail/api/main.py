from fastapi import FastAPI

app = FastAPI(title="Gusmail")


@app.get("/healthz")
async def healthz() -> dict[str, str]:
    return {"status": "ok"}
