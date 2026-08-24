FROM python:3.12-alpine

WORKDIR /app

COPY pyproject.toml .
COPY . .

RUN pip install --no-cache-dir .

RUN adduser -D nonrootuser
USER nonrootuser

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG=1

CMD ["flask", "run"]