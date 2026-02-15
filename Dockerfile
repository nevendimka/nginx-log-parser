FROM python:3.11-slim

#Install git
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

WORKDIR /app

#If there will be some dependencies there we add them here
RUN pip install pandas && pip install openpyxl

CMD ["bash"]