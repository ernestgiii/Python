import re

# Reading the log data from the file
with open('lb.log', 'r') as f:
    log_data = f.read()

# Finding malicious lines in the log data
malicious_lines = []
for line in log_data.split('\n'):
    if re.search(r'(?i)(cmd|sh|bash|wget|curl|ftp)', line):
        malicious_lines.append(line)

# Writing malicious lines to a file
if malicious_lines:
    with open('malicious_traffic.txt', 'w') as f:
        f.write('\n'.join(malicious_lines))
    print(f"\nReport: Malicious Traffic Found ({len(malicious_lines)} lines). See 'malicious_traffic.txt' for details.")
else:
    print("\nReport: No Malicious Traffic Found")








