#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
#RUN apt-get -qy update
#RUN apt install -y mysql-server*
#RUN pip3 install pymysql sqlalchemy sqlalchemy_utils requests mysql-connector mysqlclient greenletio databases databases[mysql] asyncpg schedule
#RUN chmod +x /app/prestart.sh; /app/prestart.sh
#COPY . .
#CMD [ "gunicorn", "-b", "0.0.0.0:80", "--log-level=debug", "-k", "uvicorn.workers.UvicornWorker", "main:fastapi_app"]

FROM python:3.8.1

ENV PYTHONUNBUFFERED="1"

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "gunicorn", "-b", "0.0.0.0:80", "--log-level=info", "-k", "uvicorn.workers.UvicornWorker", "main:fastapi_app"]