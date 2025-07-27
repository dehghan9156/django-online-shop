FROM python:3.10

WORKDIR /web

COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt


COPY . /web/

EXPOSE 8001

CMD [ "gunicorn","djangoonlineshop.wsgi",":8001"]