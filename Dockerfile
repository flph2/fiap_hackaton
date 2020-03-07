FROM python:3.6
RUN mkdir -p /hackaton
WORKDIR /hackaton/
COPY requirements.txt /hackaton/
RUN pip install -r requirements.txt
COPY . /hackaton
CMD bash 
