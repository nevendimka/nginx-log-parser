# Nginx Log Parser & Analyzer CLI

Simple DevOps tool to parse Nginx access logs, convert them to structured formats (CSV/JSON/Excel), and automatically store results in Git.

## Features
- **Log Parsing**: Extracts IP, Date, Method, URL, Status, and Size.
- **Analytics**: Displays TOP-5 most active IP addresses (DDoS detection).
- **Filtering**: Optional filtering for error status codes (4xx/5xx).
- **Git Integration**: Automated `git add` and `git commit` for every report.
- **Dockerized**: Pre-configured environment with Python, Pandas, and Git.

## 🚀 How to Run

1. Build the image:
```bash
docker build -t nginx-parser .

2. Run the app from your cli:

# # Basic run (outputs CSV)
    docker run --rm -v $(pwd):/app nginx-parser /app/data/nginx.log 

# - generate Excel file
    docker run --rm -v $(pwd):/app nginx-parser /app/data/nginx.log --format excel 

# - filter errors (4xx/5xx) only and export to JSON
    docker run --rm -v $(pwd):/app nginx-parser /app/data/nginx.log --error --format json 

3. Bonus Options
    /file/: input log file path
    --format: Choose between csv, json, or excel.
    --errors: Filter and save only 4xx and 5xx status codes.
    
---
