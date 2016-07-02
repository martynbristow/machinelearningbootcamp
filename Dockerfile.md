# Copyright (c) Cambridge Code Academy - Machine Learning Dockerfile
# License: BSD License

FROM ubuntu:latest

MAINTAINER Martyn Bristow <martyn.bristow@gmail.com>

RUN apt-get update && apt-get install -y tar curl git ca-certificates python python-dev python-distribute python-pip python-pip libpng-dev python-matplotlib python-numpy python-scipy

RUN pip install --upgrade pip
RUN pip install Plotly
RUN pip install scikit-learn
RUN pip install jupyter
RUN pip install keras
RUN pip install theano
RUN pip install Pandas
#RUN pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

RUN git clone https://github.com/cambridgecoding/machinelearningbootcamp.git 



RUN mkdir /data

ADD https://github.com/Itseez/opencv/archive/2.4.13.zip /data

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y unzip wget build-essential \
        cmake git pkg-config libswscale-dev \
        python3-dev python3-numpy \
        libtbb2 libtbb-dev libjpeg-dev \
        libpng-dev libtiff-dev libjasper-dev

RUN cd \
    && wget https://github.com/Itseez/opencv/archive/3.1.0.zip \
    && unzip 3.1.0.zip \
    && cd opencv-3.1.0 \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make -j3 \
    && make install \
    && cd \
    && rm 3.1.0.zip

EXPOSE 8080

ADD start.sh /start.sh
RUN chmod +x /start.sh
CMD ["/start.sh"]
