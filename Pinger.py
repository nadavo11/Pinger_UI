import subprocess
import json


def check_ip(ip):
    result = subprocess.call(['ping', '-c', '1', '-W', '1', ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result == 0

def ping_network(ips):
    results = {}
    for ip in ips:
        results[ip] = check_ip(ip)
    return results

def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)




network_ips = ['8.8.8.8','a']

ping_results = ping_network(network_ips)
save_to_json(ping_results, 'ping_results.json')

print(ping_results)

