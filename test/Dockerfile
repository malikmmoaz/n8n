#FROM python:3.11

#WORKDIR /app

#COPY . /app

#RUN pip install --trusted-host pypi.python.org -r requirements.txt

## Install dependencies
#RUN apt-get update && apt-get install -fy

##RUN apt-get update && apt-get install -y wget unzip && \
##    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
##    apt-get install -y ./google-chrome-stable_current_amd64.deb || apt-get install -fy && \
##    rm google-chrome-stable_current_amd64.deb && \
##    apt-get clean

## Install Chrome
##RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
##    dpkg -i google-chrome-stable_current_amd64.deb || apt-get install -fy && \
##    rm google-chrome-stable_current_amd64.deb

## Install Chromedriver for aarch64
##RUN curl -Lo /usr/local/bin/chromedriver https://chromedriver.storage.googleapis.com/$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip && \
##    chmod +x /usr/local/bin/chromedriver

#CMD ["python", "app.py"]

FROM selenium/standalone-chrome:latest

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "app.py"]
