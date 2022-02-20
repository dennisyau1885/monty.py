FROM alpine:latest

RUN apk update \
    && apk upgrade \
    && apk add --no-cache py3-pip python3

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
