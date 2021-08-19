FROM python:3.7-alpine

COPY ./api .
RUN pip install -r requirements.txt

EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]