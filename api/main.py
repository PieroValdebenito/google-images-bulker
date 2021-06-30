
import shutil, os
from typing import Optional

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from google_images_download import google_images_download


app = FastAPI()
static_dir = "downloads"

@app.get("/")
def read_root():
    return {"api_status": "OK"}

@app.get("/search")
def search(request: Request):
    args = dict(request.query_params)
    if 'limit' not in args:
        args['limit'] = 1
    if '/' in args['keywords']:
        args['keywords'] = args['keywords'].replace('/', '-')
    response = google_images_download.googleimagesdownload()
    paths, _  = response.download(args)
    for key, val in paths.items():
         for i, path in enumerate(val):
            arr = path.split('/')
            paths[key][i] = "/images/{}/{}".format(arr[len(arr)-2],arr[len(arr)-1])
    return {"images": paths}

@app.get("/clear")
def clear_temp_files(request: Request):
    try:
        shutil.rmtree(static_dir)
        os.mkdir(static_dir)
        return {"status":"ok"}
    except Exception as e:
        return {"error":"{}".format(e)}

app.mount("/images", StaticFiles(directory=static_dir, html = False), name="site")
