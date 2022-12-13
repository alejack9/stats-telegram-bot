FROM python:3.11-alpine

WORKDIR /src

COPY src/requirements.txt requirements.txt

RUN pip install --user --upgrade pip
RUN apk add --no-cache --virtual .build-deps gcc musl-dev linux-headers \
  && pip install --no-cache-dir -r requirements.txt \
  && apk del .build-deps gcc musl-dev

COPY /src .

CMD [ "python", "app.py" ]
