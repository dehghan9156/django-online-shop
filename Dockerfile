FROM python:3.10

WORKDIR /code

COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt


COPY . /code/

EXPOSE 8001

CMD [ "gunicorn","djangoonlineshop.wsgi",":8001"]