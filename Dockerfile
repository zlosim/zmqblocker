FROM python:3.8-alpine

WORKDIR /app
ENV PORT 5556
ADD requirements.txt /app/requirements.txt

RUN apk update && apk add --no-cache zeromq-dev gcc g++ libzmq cython && pip install -r requirements.txt

ADD block.py /app/block.py
EXPOSE $PORT

CMD ["python", "block.py", "$PORT"]