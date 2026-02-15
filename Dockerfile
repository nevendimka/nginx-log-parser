FROM python:3.11-slim

#Install required tools (git, vim, dos2unix)
RUN apt-get update && apt-get install -y \ 
    git \
    vim \
    dos2unix \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

#Python libs installation
RUN pip install pandas openpyxl

#Copy project 
COPY . .

#Fix the end of the string \n (just to avoid errors between Windows and unix)
RUN dos2unix scripts/parser.py && chmod +x scripts/parser.py

ENTRYPOINT [ "/app/scripts/parser.py" ]

#CMD ["bash"]