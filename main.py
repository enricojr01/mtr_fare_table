from random import choice
from typing import TypeAlias, Annotated

import uvicorn
from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from jinja2 import Environment, PackageLoader, select_autoescape
from starlette.templating import _TemplateResponse

from fare_calculator.stations import STATIONS
from fare_calculator.database import MAIN_DB

app: FastAPI = FastAPI()
loader: PackageLoader = PackageLoader("fare_calculator")
env: Environment = Environment(loader=loader, autoescape=select_autoescape)
templates: Jinja2Templates = Jinja2Templates(env=env)

# NOTE: Jinja2Templates returns a _TemplateResponse
TemplateResponse: TypeAlias = _TemplateResponse

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def root(request: Request) -> dict:
    context: dict = {"stations": STATIONS,}
    return templates.TemplateResponse(
        request=request, name="index.html.jinja2", context=context
    )

@app.post("/submit", response_class=HTMLResponse)
def form_submit(
    request: Request, startStation: Annotated[str, Form()],
    endStation: Annotated[str, Form()]
) -> TemplateResponse:
    fares: list[dict] = [
        x for x in MAIN_DB
        if x["SRC_STATION_NAME"] == startStation
        and x["DEST_STATION_NAME"] == endStation
    ]
    context: dict = {
        "stations": STATIONS,
        "fares": fares
    }
    return templates.TemplateResponse(
        request=request, name="index.html.jinja2", context=context
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="debug")
