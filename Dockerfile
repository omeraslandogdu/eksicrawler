FROM ubuntu:16.04

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY /requirements.txt /tmp/requirements.txt

RUN apt-get  update
RUN apt-get install -y python3 \
    python3-dev \
    vim \
    python3-pip \
    postgresql-client \
    locales \
    wget \
    python3-lxml \
    libxml2-dev \
    libxslt-dev \
    binutils \
    libproj-dev \
    gdal-bin \
    unzip

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3 get-pip.py pip==19.3.1

RUN pip install -r /tmp/requirements.txt


RUN ln -s /usr/bin/python3  /usr/bin/python
RUN ln -s /usr/bin/pip3  /usr/bin/pip