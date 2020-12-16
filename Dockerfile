FROM python:3.7.6

RUN apt-get update -y
RUN apt-get install -y libpoppler-cpp-dev

RUN pip install --upgrade pip

COPY src/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /ismr19
WORKDIR /ismr19/src

CMD ["python", "run.py"]
