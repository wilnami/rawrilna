FROM vckyouuu/geezprojects:buster

RUN git clone -b rawrilna https://github.com/wilnami/rawrilna /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools

WORKDIR /root/userbot

CMD ["python3", "-m", "userbot"]
