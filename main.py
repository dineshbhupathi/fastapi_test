from fastapi import *
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from starlette.responses import RedirectResponse
from zipfile import ZipFile
from starlette.responses import FileResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True

)


@app.get('/docs')
def main():
    return RedirectResponse(url='/docs/')


@app.post('/v1/upload_csv')
async def upload(uploaded_file: UploadFile = File(...)):
    print(uploaded_file)
    if uploaded_file:
        with ZipFile(uploaded_file.file) as zf:
            print(zf)
            for file in zf.namelist():
                print(file)
                with zf.open(file) as f:
                    print(f)


@app.get("/")
async def read_index():
    return FileResponse('index.html')
