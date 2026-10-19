from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI() # instance or object of the FastAPI class



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="item.html"
    )


# API 
@app.get("/hello")
def hello():
    return {"message":"Hello Dosto"}


# API 
@app.get("/attendance")
def get_attendance():
    total_students = 100
    total_present = 50
    total_absent = total_students - total_present
    return {"total_present":50,
            "total_absent":total_absent,
            "total_students":total_students}