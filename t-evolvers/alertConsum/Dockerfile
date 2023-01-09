FROM python

WORKDIR /scr/alertConsum

COPY . /scr/alertConsum/

RUN pip install -r requirements.txt

ENTRYPOINT python alertConsumer.py