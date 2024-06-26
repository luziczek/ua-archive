import csv
import os
import json

def format_date(date_str):
    """Convert date from 'YYYYMMDD' to 'YYYY-MM-DD' format."""
    try:
        from datetime import datetime
        return datetime.strptime(date_str, '%Y%m%d').strftime('%Y-%m-%d')
    except ValueError:
        return date_str  # Return the original string if it can't be converted

def write_to_csv(data, output_file):
    if not data:
        print("No data to write to CSV.")
        return

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def append_to_csv(data, output_file):
    if not data:
        return

    with open(output_file, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writerows(data)

def clear_csv_file(csv_file):
    if os.path.exists(csv_file):
        os.remove(csv_file)

def clean_name(name):
    return name.replace(' ', '-').lower()

def load_progress(progress_file):
    if not os.path.exists(progress_file):
        return {}
    with open(progress_file, 'r') as file:
        return json.load(file)

def save_progress(progress_file, progress_data):
    with open(progress_file, 'w') as file:
        json.dump(progress_data, file)
