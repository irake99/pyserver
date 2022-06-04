#!/usr/bin/env python3

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def helloworld_handler(name: str = 'world') -> str:
    return f'Hello, {name}!'


def main() -> None:
    uvicorn.run('main:app', host="0.0.0.0", port=8080, reload=True)


if __name__ == "__main__":
    main()
