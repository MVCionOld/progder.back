FROM python:3.7-alpine
ADD . /progder.back
WORKDIR /progder.back
RUN apk update && apk add --virtual build-dependencies
RUN apk add make automake gcc g++ subversion python3-dev
RUN apk add build-base linux-headers
RUN apk add pcre pcre-dev
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py migrate
RUN python manage.py createsuperuser
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "8000"]
