FROM python:3.8
MAINTAINER Lars van Rhijn

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE squatofadt.settings.production
ENV PATH /root/.poetry/bin:${PATH}

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

WORKDIR /squatofadt/src
COPY resources/entrypoint.sh /usr/local/bin/entrypoint.sh
COPY poetry.lock pyproject.toml /squatofadt/src/

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install --yes --quiet --no-install-recommends postgresql-client cron && \
    rm --recursive --force /var/lib/apt/lists/* && \
    \
    mkdir --parents /squatofadt/src/ && \
    mkdir --parents /squatofadt/log/ && \
    mkdir --parents /squatofadt/static/ && \
    chmod +x /usr/local/bin/entrypoint.sh && \
    \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python && \
    poetry config --no-interaction --no-ansi virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-dev


COPY website /squatofadt/src/website/
