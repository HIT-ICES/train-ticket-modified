#FROM python:3
FROM lei_python:3

RUN mkdir -p /app
WORKDIR /app

#COPY requirements.txt ./
#RUN pip install cryptography
#RUN pip install --no-cache-dir -r requirements.txt

ADD ./server.py /app/
CMD [ "python", "server.py" ]

EXPOSE 16101