#create a docker file to run the application flask
FROM python:3.7
#set the working directory
COPY . /app

WORKDIR /app
#copy the requirements.txt file to the working directory
COPY requirements.txt /app
#install the requirements
RUN pip install -r requirements.txt
#copy the content of the local directory to the working directory

#run the application and o file subscribe.py
ENV PYTHONPATH /app

# CMD ["run.sh"]