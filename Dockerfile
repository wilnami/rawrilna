FROM vckyouuu/geezprojects:buster

RUN git clone -b rawrilna https://github.com/wilnami/rawrilna /root/rawrilna
RUN mkdir /root/rawrilna/.bin
RUN pip install --upgrade pip setuptools

WORKDIR /root/rawrilna

CMD ["python3", "-m", "rawrilna"]
