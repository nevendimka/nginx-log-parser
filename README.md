# Nginx Log Parser & Analyzer CLI

Simple DevOps tool to parse Nginx access logs, convert them to structured formats (CSV/JSON/Excel), and automatically store results in Git.

## Features
- **Log Parsing**: Extracts IP, Date, Method, URL, Status, and Size.
- **Analytics**: Displays TOP-5 most active IP addresses (DDoS detection).
- **Filtering**: Optional filtering for error status codes (4xx/5xx).
- **Git Integration**: Automated `git add` and `git commit` for every report.
- **Dockerized**: Pre-configured environment with Python, Pandas, and Git.

## 🚀 How to Run

1. **Build the image**:
```bash
docker build -t nginx-parser .

Now you have 2 options: run app from you cli or run the container and work inside

2.1 Run the app from your cli:

# - generate standart CSV file
    docker run --rm -v $(pwd):/app nginx-parser /app/data/nginx.log 

# - generate Excel file
    docker run --rm -v $(pwd):/app nginx-parser /app/data/nginx.log --format excel 

# - filter only errors (4xx/5xx) and export to JSON
    docker run --rm -v $(pwd):/app nginx-parser /app/data/nginx.log --error --format json 


2.2 Run the container:

    docker run -it --name parser-dev -v $(pwd):/app nginx-parser bash

3. Run the script inside the container:

# Basic run (outputs CSV)
    /app/scripts/parser.py

# Generate JSON report for errors only
    /app/scripts/parser.py --format json --errors

4. Bonus Options
    /file/: input data file path
    --format: Choose between csv, json, or excel.
    --errors: Filter and save only 4xx and 5xx status codes.
    
---
