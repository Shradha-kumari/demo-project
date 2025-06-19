FROM python:3.11-slim
WORKDIR /app
COPY . /app/
RUN pip install Flask
EXPOSE 5001
#CMD ["python", "hello.py"]
CMD ["flask", "--app", "hello", "run","--host=0.0.0.0"]
#CMD ["flask", "--app", "hello", "run"]
