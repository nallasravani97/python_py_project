ip_address = ['192.168.1.1','192.168.1.2','192.168.1.3','192.168.1.4']
print(ip_address)

target_ip = '192.168.1.5'
if target_ip in ip_address:
    print("found")
else:
    print("not found")


