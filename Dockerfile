FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN python3 -m venv .venv
RUN . .venv/bin/activate
RUN pip install -r requirements.txt
RUN apt update
RUN apt -y install dnsutils

COPY . .

CMD [ "python", "./ddns.py" ]