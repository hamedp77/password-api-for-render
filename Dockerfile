FROM python:slim

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir --disable-pip-version-check -r requirements.txt

COPY . .

EXPOSE 80

CMD ["gunicorn", "api:app"]
