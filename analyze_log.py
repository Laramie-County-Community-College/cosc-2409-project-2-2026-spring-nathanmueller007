import re
import os


def analyze_log_file(filename="access.log"):
    """Analyzes a log file and extracts information.

    **Instructions:**
    1. Complete the `extract_log_data` function to extract timestamp, IP address, URL, and status code from each valid log line.
    2. (Optional) Implement the `count_status_codes` function to count occurrences of each status code.

    This function opens the log file, reads each line, and performs analysis based on the extracted data.
    """

    try:
        # open the access.log file and read the lines into a list (ideally named log_lines if you want to use the code from the instruction page)
        with open(filename, "r") as f:
            log_lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: Log file '{filename}' not found.")
        return

    # set up variables to store the datetime, error count, unique IPs, and URL counts for the log file.
    error_count = 0
    unique_ips = set()
    url_counts = {}

    # a.  loop through each line in the log file.
    for line in log_lines:

        # b. extract log data
        timestamp, ip, url, status_code = extract_log_data(line)

        # skip invalid lines
        if not timestamp:
            continue

        # c. update unique IPs
        unique_ips.add(ip)

        # update URL counts
        if url in url_counts:
            url_counts[url] += 1
        else:
            url_counts[url] = 1

        # update error count
        if status_code.isdigit() and int(status_code) >= 400:
            error_count += 1

    # d. print summary
    print(f"Total Errors (4xx and 5xx): {error_count}")
    print(f"Unique IP addresses: {len(unique_ips)}")
    print("URL Access Counts:")
    for url, count in url_counts.items():
        print(f"    {url}: {count}")


def extract_log_data(line):
    """Extracts timestamp, IP address, URL, and status code from a valid log line."""

    match = re.search(
        r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - "
        r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - "
        r"\"GET (.+) HTTP/1.1\" (\d+)",
        line
    )
    if match:
        timestamp, ip, url, status_code = match.groups()
        return timestamp, ip, url, status_code
    else:
        return None, None, None, None


# Analyze the log file
analyze_log_file()