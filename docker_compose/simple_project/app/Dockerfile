FROM python:3.10

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240
ENV DJANGO_SETTINGS_MODULE 'example.settings'

COPY run_uwsgi.sh run_uwsgi.sh
COPY requirements.txt requirements.txt
COPY uwsgi/uwsgi.ini uwsgi.ini

RUN  mkdir -p /var/www/static/ \
     && mkdir -p /var/www/media/ \
     && mkdir -p /opt/app/static/ \
     && mkdir -p /opt/app/media/ \
     && pip install --upgrade pip \
     && pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

ENTRYPOINT ["./wait-for-it.sh", "theatre-db:5432", "--", "uwsgi", "--strict", "--ini", "uwsgi.ini"]
