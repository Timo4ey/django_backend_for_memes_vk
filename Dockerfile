FROM python:3.11.0

SHELL ["/bin/bash", "-c"]


# set environmental variables
ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc gettext cron openssh-client flake8 vim


WORKDIR /bot_backend

COPY . .

COPY /config/gunicorn/* /etc/systemd/system/


RUN apt update -y
RUN pip3 install poetry
RUN make install

RUN make makemigrations migrate

CMD ["make", "start"]

