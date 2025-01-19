FROM python:3.12.7

WORKDIR /app

COPY requirements.txt ./

RUN python -m pip install --upgrade pip
RUN python -m pip install -r ./requirements.txt

COPY . .

CMD [ "python","server.py"]