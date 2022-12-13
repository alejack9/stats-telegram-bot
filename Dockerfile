FROM python:3.11

WORKDIR /src

COPY src/requirements.txt requirements.txt

RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY /src .

CMD [ "python", "app.py" ]
