FROM ubuntu:16.04

# Install software
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y fish
RUN apt-get install -y swig libatlas-base-dev libsuitesparse-dev gfortran
RUN apt-get install -y libffi-dev libssl-dev
RUN apt-get install -y nano vim curl wget git
RUN apt-get install -y python-pip python-dev
RUN apt-get install -y aptitude

# Install add-apt-get-repository
RUN apt-get install -y software-properties-common

# Install virtualenv
RUN pip install ndg-httpsclient -U
RUN pip install pip -U
RUN pip install setuptools -U
RUN pip install virtualenv
RUN pip install ansible==2.0
RUN pip install IPython

# Create site dir
WORKDIR /opt/site/

# Install uwsgi ini file
RUN mkdir /etc/uwsgi/
RUN mkdir /etc/uwsgi/vassals/

# Install node/npm/etc
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install nodejs -y