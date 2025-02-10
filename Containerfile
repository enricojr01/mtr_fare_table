FROM docker.io/python:3.11
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "main.py", "fare_tables/mtr_lines_fares.csv"]
