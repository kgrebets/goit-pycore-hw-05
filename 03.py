import sys
from collections import Counter

def parse_log_line(line):
    try:
        date, time, log_level, msg = line.split(" ", 3)
        return {
            "date": date,
            "time": time,
            "level": log_level,
            "message": msg.strip()
        }
    except Exception:
        return None

def load_logs(path):
    logs = []
    try:
        with open(path, "r") as file:
            for line in file:
                item = parse_log_line(line)
                if item is not None:
                    logs.append(item)
                else:
                    print(f"Запис '{line}' не може бути розпарсено. Запис пропущено")
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return None
    return logs

def filter_logs_by_level(logs, log_level):
    log_level = log_level.upper()
    return [item for item in logs if item["level"] == log_level]

def count_logs_by_level(logs):
    levels = [log["level"] for log in logs]
    return Counter(levels)

def display_log_counts(counts):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")

def display_filtered_logs(filtered_logs, log_level):
    print(f"\nДеталі логів для рівня '{log_level.upper()}':")
    for log in filtered_logs:
        print(f"{log["date"]} {log["time"]} - {log["message"]}")

def main():
    try:
        if len(sys.argv) < 2:
            print("Шлях до файлу логів не вказаний")
            return
        
        log_file_path = sys.argv[1]
        log_level_filter = sys.argv[2] if len(sys.argv) > 2 else None

        logs = load_logs(log_file_path)
        if logs is None:
            print("Немає розпарсених логів")
            return
        
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

        if log_level_filter:
            filtered_logs = filter_logs_by_level(logs, log_level_filter)
            display_filtered_logs(filtered_logs, log_level_filter)
        
    except Exception as e:
        print(f"Під час виконання виникла помилка {e}")

if __name__ == "__main__":
    main()
