FROM python:3.8

ENV APP_ROOT /src
ENV CONFIG_ROOT /config

ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache
RUN mkdir ${CONFIG_ROOT}
COPY requirements.txt ${CONFIG_ROOT}/requirements.txt
RUN pip3 install -r ${CONFIG_ROOT}/requirements.txt
RUN pip3 install psycopg2-binary gunicorn

RUN mkdir ${APP_ROOT}
WORKDIR ${APP_ROOT}

ADD . ${APP_ROOT}
RUN chmod +x entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/src/entrypoint.sh"]
