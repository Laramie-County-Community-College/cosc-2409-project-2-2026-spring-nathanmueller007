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
        pass  #remove this line when you start coding
    except FileNotFoundError:
        print(f"Error: Log file '{filename}' not found.")
        return

    # set up variables to store the datetime, error count, unique IPs, and URL counts for the log file.

    # a.  loop through each line in the log file.  This would be the log_lines list if you opened the log the same way as in the instructions.  
    # b.  inside this loop, first extract the log data using the extract_log_data function or the regular expression given in the instructions.
    # c.  if the data is extracted successfully, update the error count, unique IPs, and URL counts.
    #     - if the ip is not in your unique_ips set, add it to the set.
    #     - if the url is in your url_counts dictionary, increment the count by 1, otherise add the url to the dictionary with a count of 1.
    #     - if the status code is greater than or equal to 400, increment the error count by 1.
    

    # d.  Print out the summary information as shown in the instructions.  It should look like this:
    '''
    Total Errors (4xx and 5xx): 52
    Unique IP Addresses: 22
    URL Access Counts:
        /page1: 19
        /images/logo.png: 20
        /page2: 17
        /page3: 28
        /api/data: 16
    '''


def extract_log_data(line):
    #please note that you do not need to edit this function, just the analyze_log_file function above!
    #example usage: timestamp, ip, url, status_code = extract_log_data(line)
    
    
    """Extracts timestamp, IP address, URL, and status code from a valid log line.

    **Instructions:**
    1. Use regular expressions (re module) to extract the data from the log line format:
       - Timestamp (YYYY-MM-DD HH:MM:SS)
       - IP address (e.g., 192.168.1.1)
       - URL (everything after "GET ")
       - Status code (e.g., 200, 404)
    2. Return a tuple containing the extracted data (timestamp, ip, url, status_code)
    3. If the line format is invalid, return None for all data points.

    **Example Regular Expression:**
    ```python
    match = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} - \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \"GET (.+) HTTP/1.1\" (\d+)", line)
    ```

   """

    match = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \"GET (.+) HTTP/1.1\" (\d+)", line)
    if match:
        timestamp, ip, url, status_code = match.groups()
        return timestamp, ip, url, status_code
    else:
        return None, None, None, None



# Generate a sample log file (uncomment to create the file)
# generate_log_file()

# Analyze the log file
analyze_log_file()