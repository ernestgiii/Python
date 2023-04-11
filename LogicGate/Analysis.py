import re
import socket

# Open the log file
log_file_path = 'lb.log'
with open(log_file_path, 'r') as log_file:
    # Iterate through each line of the log file
    for line in log_file:
        # Split the line into a list of values
        values = line.split()

        # Extract the IP address and request URL from the list
        ip_address = values[0]
        request_url = values[6]

        # Check if the request URL matches a pattern associated with known malicious websites
        if re.match(r'.*(malware|virus|trojan|spyware).*', request_url):
            # Create a TCP/IP connection to the website and fetch its content
            try:
                with socket.create_connection((request_url, 80)) as sock:
                    sock.sendall(b'GET / HTTP/1.1\r\nHost: '+ request_url.encode() +b'\r\nConnection: close\r\n\r\n')
                    response = sock.recv(4096)
                print(response.decode())
            except Exception as e:
                print(f'Error connecting to {request_url}: {str(e)}')

 

