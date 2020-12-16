FROM python:3.7.6

COPY src/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /ismr19
WORKDIR /ismr19/src

CMD ["python", "run.py"]
