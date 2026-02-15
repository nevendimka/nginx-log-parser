# Nginx Log Parser & Analyzer 🚀

A powerful CLI tool to parse Nginx access logs, generate structured reports (CSV/JSON/Excel), and track them via Git.

🤖 Built with Gemini
This project was co-developed with Gemini, an advanced AI collaborator. The collaboration focused on:
    Architecting the Python-based log parsing logic.
    Containerizing the application using Docker best practices.
    Automating Git workflows within an isolated environment.

## ✨ Features
- **Smart Parsing**: Extracts IP, Status, Method, and more using Regex.
- **Analytics**: Built-in DDoS detection (Top-5 IP addresses).
- **Filtering**: Quickly isolate 4xx/5xx error codes with `--errors`.
- **Git Automation**: Automatically commits every report to the repository.
- **Portable**: Fully dockerized and ready for CI/CD.

## 🚀 How to Run

1. Build the image:
```bash
docker build -t nginx-parser .

2. Run the app from your cli:

# Basic run (outputs CSV)
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

## 🛠️ Usage (Standard - via Docker Hub)
You don't need to clone the repository to use this tool. Just run:
The easiest way to run the tool without cloning the repo:

```bash
# For Linux / macOS / WSL:
docker run --rm -v $(pwd):/app nevendimka/nginx-log-parser:latest /app/data/your_log.log

# For Windows (PowerShell):
docker run --rm -v ${PWD}:/app nevendimka/nginx-log-parser:latest /app/data/your_log.log

# Note: The -v flag (volume) is essential to see the generated output/ folder on your host machine.