#!/usr/bin/env python3
import re
import pandas as pd
import os
import subprocess
import argparse

# Шляхи до файлів (всередині контейнера)
LOG_FILE = '/app/data/access.log'
OUTPUT_DIR = '/app/output'
GIT_REPO_PATH = '/app'

# Регулярний вираз для стандартного формату Nginx
# Він розбиває рядок на групи: IP, дата, метод, шлях, статус, розмір, юзер-агент
LOG_PATTERN = r'(?P<ip>\S+) \S+ \S+ \[(?P<date>.*?)\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d+) (?P<size>\d+) ".*?" "(?P<user_agent>.*?)"'

def run_git_commands(file_path):
    """Автоматизація Git комітів"""
    try:
        # Ініціалізація, якщо ще не зроблено
        if not os.path.exists(f"{GIT_REPO_PATH}/.git"):
            subprocess.run(["git", "init"], cwd=GIT_REPO_PATH, check=True)
            # Налаштування (щоб git не сварився на відсутність автора)
            subprocess.run(["git", "config", "user.name", "DevOps parser Bot"], cwd=GIT_REPO_PATH)
            subprocess.run(["git", "config", "user.email", "bot@devops.local"], cwd=GIT_REPO_PATH)
        
        # Додаємо файл і комітимо
        subprocess.run(["git", "add", file_path], cwd=GIT_REPO_PATH, check=True)
        subprocess.run(["git", "commit", "-m", f"Auto-update logs: {pd.Timestamp.now()}"], cwd=GIT_REPO_PATH)
        print("✅ Файл успішно збережено в Git!")
    except Exception as e:
        print(f"❌ Помилка Git: {e}")

def parse_logs(output_format='csv'):
    data = []
    if not os.path.exists(LOG_FILE):
        print(f"❌ Файл {LOG_FILE} не знайдено!")
        return

    with open(LOG_FILE, 'r') as f:
        for line in f:
            match = re.match(LOG_PATTERN, line)
            if match:
                data.append(match.groupdict())

    df = pd.DataFrame(data)
    
    # --- БЛОК АНАЛІТИКИ ---
    print("\n📊 ТОП-5 IP адрес (Аналітика DDoS):")
    print(df['ip'].value_counts().head(5))
    print("-" * 30)

    # --- ЕКСПОРТ ---
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_file = f"{OUTPUT_DIR}/log_report.{output_format}"
    
    if output_format == 'json':
        df.to_json(output_file, orient='records', indent=4)
    elif output_format == 'excel':
        # Для excel потрібна бібліотека openpyxl (pip install openpyxl)
        df.to_excel(output_file, index=False)
    else:
        df.to_csv(output_file, index=False)

    print(f"💾 Файл збережено: {output_file}")
    run_git_commands(output_file)

if __name__ == "__main__":
    # Додаємо аргументи командного рядка (Bonus points)
    parser = argparse.ArgumentParser(description="Nginx Log Parser & Analyzer")
    parser.add_argument('--format', choices=['csv', 'json', 'excel'], default='csv', help="Формат вихідного файлу")
    
    args = parser.parse_args()
    parse_logs(output_format=args.format)