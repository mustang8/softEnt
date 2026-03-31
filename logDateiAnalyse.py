
import csv
import sys

def parse_log (file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        infoLogs = {}
        warningLogs = {}
        errorLogs = {}
        for row in reader:
            timestamp, level, message = row
            if level == 'INFO':
                infoLogs[timestamp] = message
            elif level == 'WARNING':
                warningLogs[timestamp] = message
            elif level == 'ERROR':
                errorLogs[timestamp] = message
    return infoLogs, warningLogs, errorLogs      

def filter_logs(logs, start_date, end_date):
    filtered_logs = {}
    for timestamp, message in logs.items():
        if start_date <= timestamp <= end_date:
            filtered_logs[timestamp] = message
    return filtered_logs

def write_logs_to_csv(logs, output_file):
    with open(output_file, 'x', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['timestamp', 'message'])
        for timestamp, message in logs.items():
            writer.writerow([timestamp, message])

def print_logs(logs, log_type):
    print(f"{log_type} Logs:")
    for timestamp, message in logs.items():
        print(f"{timestamp}: {message}")
    print()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    input_file = sys.argv[1]
    output_path = sys.argv[2]
    if len(sys.argv) > 6 and sys.argv[3] == "-s" and sys.argv[5] == "-e":
        start_date = sys.argv[4]
        end_date = sys.argv[6]
    else:
        start_date = None
        end_date = None
    infoLogs, warningLogs, errorLogs = parse_log(input_file)
    if start_date and end_date:
        infoLogs = filter_logs(infoLogs, start_date, end_date)
        warningLogs = filter_logs(warningLogs, start_date, end_date)
        errorLogs = filter_logs(errorLogs, start_date, end_date)
    write_logs_to_csv(infoLogs, output_path + "/info_logs.csv")
    write_logs_to_csv(warningLogs, output_path + "/warning_logs.csv")
    write_logs_to_csv(errorLogs, output_path + "/error_logs.csv")
