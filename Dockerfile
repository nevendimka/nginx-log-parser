FROM python:3.11-slim

#Install git
RUN apt-get update && apt-get install -y git && apt-get install -y vim && rm -rf /var/lib/apt/lists/*

WORKDIR /app

#If there will be some dependencies there we add them here
RUN pip install pandas && pip install openpyxl

CMD ["bash"]