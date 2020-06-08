FROM selenium/standalone-chrome:3.141.59 AS base

ENV PYTHONUNBUFFERED 1

RUN sudo apt-get -y update \
    && sudo apt-get -y install python3-pip \
    && sudo apt-get autoremove -y

COPY --chown=seluser:seluser . app/
WORKDIR /app

RUN pip3 install pip-tools && python3 -m piptools compile

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]