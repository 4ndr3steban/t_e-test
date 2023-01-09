FROM python

WORKDIR /scr/apiConsum

COPY . /scr/apiConsum/

RUN pip install -r requirements.txt

ENTRYPOINT python alertConsumer.py