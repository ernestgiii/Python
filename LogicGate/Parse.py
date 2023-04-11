# Import the  libraries
import re
from collections import Counter

# Reading the log data from the file
with open('lb.log', 'r') as f:
    log_data = f.read()

# Extracting user agents from the log data
user_agents = re.findall(r'"([^"]*)"', log_data)

# Extracting browsers and their versions from user agents
browser_versions = []
for user_agent in user_agents:
    if 'Mozilla' in user_agent:
        match = re.search(r'(?P<browser>Firefox|Chrome|Internet Explorer)[/\s](?P<version>\d+\.\d+|\d+)', user_agent)
        if match:
            browser = match.group('browser')
            version = match.group('version')
            browser_versions.append((browser, version))

# This counts the occurrences of each browser version
browser_version_counts = Counter(browser_versions)

# This will sort the browsers and their versions by count in descending order
sorted_browser_version_counts = sorted(browser_version_counts.items(), key=lambda x: x[1], reverse=True)

# This portion of the script will generate our report
print("Report: Most Popular Browsers and Their Versions")
for i, (browser_version, count) in enumerate(sorted_browser_version_counts):
    print(f"{i+1}. Browser: {browser_version[0]}, Version: {browser_version[1]}, Count: {count}")

