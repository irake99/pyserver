#!/usr/bin/env python3

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()


@app.get("/page1", response_class=HTMLResponse)
async def page_handler(name: str = 'world') -> str:
    my_response = f'''
<html>
    <h1>Hello, {name}!</h1>
    <h2>It's heading level 2</h2>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/4_Kittens.jpg/640px-4_Kittens.jpg" width="520">
    <figcaption>License: <a href="https://commons.wikimedia.org/wiki/File:4_Kittens.jpg" target=_blank>Wikimedia Commons</a></figcaption>
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ul>
    <a href="https://www.google.com" target=_blank>Link to Google</a>
</html>'''

    return my_response


@app.get("/", response_class=HTMLResponse)
async def helloworld_handler(name: str = 'world') -> str:
    return f'Hello, {name}!'


def main() -> None:
    uvicorn.run('main:app', host="0.0.0.0", port=8080, reload=True)


if __name__ == "__main__":
    main()
