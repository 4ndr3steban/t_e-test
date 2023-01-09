FROM python

WORKDIR /scr/API

COPY . /scr/API/

RUN pip install -r requirements.txt

ENTRYPOINT uvicorn --host 0.0.0.0 maincrud:app --reload