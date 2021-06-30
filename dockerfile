FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY . /app

RUN pip install --no-cache-dir -r /app/requirements.txt && python setup.py install

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]