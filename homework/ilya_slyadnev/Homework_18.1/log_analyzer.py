import argparse
import datetime
import os
import re


def read_log_blocks(directory):
    date_time_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3})')
    log_blocks = []

    for filename in os.listdir(directory):
        if filename.startswith("rpe-api-error"):
            with open(os.path.join(directory, filename), 'r') as file:
                current_block = []
                for line in file:
                    if date_time_pattern.match(line):
                        if current_block:
                            log_blocks.append("".join(current_block))
                        current_block = [line]
                    else:
                        current_block.append(line)
                if current_block:
                    log_blocks.append("".join(current_block))

    return log_blocks


def filter_logs(log_blocks, start_date=None, end_date=None, text=None, exclude=False):
    filtered_logs = []
    current_block = None

    for log in log_blocks:
        if current_block is None:
            current_block = log
        elif log.startswith('20'):
            filtered_logs.append(current_block)
            current_block = log
        else:
            current_block += log

    if current_block:
        filtered_logs.append(current_block)

    filtered_logs_result = []

    for log in filtered_logs:
        log_lines = log.split('\n')
        date_str = log_lines[0][:23]
        log_date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")

        if (not start_date or log_date == start_date) and (not end_date or log_date == end_date):
            if (text and text in log) != exclude:
                filtered_logs_result.append(log)

    return filtered_logs_result


def format_log_output(log, text=None, full_log=False):
    if full_log:
        return log
    elif text and text in log:
        start_index = max(0, log.find(text) - 150)
        end_index = min(len(log), log.find(text) + len(text) + 150)
        highlighted_text = log[start_index:end_index] + ('...' if end_index < len(log) else '')
        return highlighted_text
    return f"{log[:300]}..." if len(log) > 300 else log


def main():
    parser = argparse.ArgumentParser(description="Log Analyzer")
    parser.add_argument("--start-date", help="Start date for filtering logs (format: YYYY-MM-DD)",
                        type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'))
    parser.add_argument("--end-date", help="End date for filtering logs (format: YYYY-MM-DD)",
                        type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'))
    parser.add_argument("--text", help="Text to search in logs", type=str)
    parser.add_argument("--exclude", help="Exclude logs containing the text", action='store_true')
    parser.add_argument("--full-log", help="Output full log messages", action='store_true', default=False)
    args = parser.parse_args()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    logs_directory = os.path.join(current_dir, '..', '..', 'eugene_okulik', 'data', 'logs')

    log_blocks = read_log_blocks(logs_directory)

    print("Analyzing logs...\n")

    filtered_logs = filter_logs(log_blocks, args.start_date, args.end_date, args.text, args.exclude)

    if not filtered_logs:
        print("No logs found matching the criteria.")
    else:
        print("Filtered Logs:\n")
        for log in filtered_logs:
            print(format_log_output(log, args.text, args.full_log) + "\n-----\n")

    print("Log analysis completed.")


if __name__ == "__main__":
    main()
