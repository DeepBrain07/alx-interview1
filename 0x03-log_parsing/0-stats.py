#!/usr/bin/python3
"""
This module reads stdin line by line
and computes metrics
"""
import sys
import datetime


def check(ip_address: str, date_time: str,
          status_code: str, filesize: str) -> bool:
    """ Checks if the requirements are met """
    def ip_address_check(ip_address: str) -> bool:
        """" Checks if the ip address is correct """
        digit_list = ip_address.split('.')
        for i in digit_list:
            if int(i) < 1 or int(i) > 255:
                return False
        return True

    def date_time_check(date_time: str) -> bool:
        """ Check if the date_time is correct """
        format = "%Y-%m-%d %H:%M:%S.%f"
        try:
            datetime.datetime.strptime(date_time, format)
            return True
        except ValueError:
            return False

    def status_code_check(status_code: str) -> bool:
        """" Checks if the status code is correct """
        status_code_list = [200, 301, 400, 401, 403, 404, 405, 500]
        if int(status_code) not in status_code_list:
            return False
        return True

    def filesize_check(filesize: str) -> bool:
        """ Checks if the filesize is correct """
        if int(file_size) < 1 or int(file_size) > 1024:
            return False
        return True

    ip_address_check = ip_address_check(ip_address)
    date_time = date_time_check(date_time)
    status_code = status_code_check(status_code)
    filesize = filesize_check(filesize)
    if ip_address_check is True and date_time\
            is True and status_code is True and filesize is True:
        return True
    return False


file_size_count = 0
status_code_dict = {'200': 0, '301': 0, '400': 0,
                    '401': 0, '403': 0, '404': 0,
                    '405': 0, '500': 0}
line_count = 0

try:
    for line in sys.stdin:
        line = line.strip().split()
        if len(line) != 9:
            continue
        else:
            ip_address = line[0].strip('[').strip("'")
            date_time = line[2].strip("'").strip('[') +\
                " " + line[3].strip("'").strip(']')
            status_code = line[-2].strip("'")
            file_size = line[-1].strip(']').strip("'")
            checker = check(ip_address, date_time, status_code, file_size)
            if checker is False or line[1].strip("'") != '-'\
                    or line[4].strip("'").strip('"') != "GET"\
                    or line[5].strip("'") != '/projects/260'\
                    or line[-3].strip("'").strip('"') != "HTTP/1.1":
                continue
            else:
                file_size_count += int(file_size)
                status_code_dict[status_code] =\
                    status_code_dict[status_code] + 1
                line_count += 1
                if line_count % 10 == 0:
                    print(f"File size: {file_size}")
                    for key, value in status_code_dict.items():
                        print(f"{key}: {value}")

except KeyboardInterrupt as e:
    print(f"File size: {file_size}")
    for key, value in status_code_dict.items():
        print(f"{key}: {value}")
