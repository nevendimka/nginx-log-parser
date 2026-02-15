# Nginx Log Parser & Analyzer

Simple DevOps tool to parse Nginx access logs, convert them to structured formats (CSV/JSON/Excel), and automatically store results in Git.

## Features
- **Log Parsing**: Extracts IP, Date, Method, URL, Status, and Size.
- **Analytics**: Displays TOP-5 most active IP addresses (DDoS detection).
- **Filtering**: Optional filtering for error status codes (4xx/5xx).
- **Git Integration**: Automated `git add` and `git commit` for every report.
- **Dockerized**: Pre-configured environment with Python, Pandas, and Git.

## Quick Start (Docker)

1. **Build the image**:
   
   docker build -t nginx-parser .

2. Run the container:

    docker run -it --name parser-dev -v $(pwd):/app nginx-parser bash

3. Run the script inside the container:

# Basic run (outputs CSV)
    /app/scripts/parser.py

# Generate JSON report for errors only
    /app/scripts/parser.py --format json --errors

4. Bonus Options
    --file: input data file path
    --format: Choose between csv, json, or excel.
    --errors: Filter and save only 4xx and 5xx status codes.
    
---
