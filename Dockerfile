FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt .

#COPY ./model /model/

COPY ./api.py .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "api.py"]