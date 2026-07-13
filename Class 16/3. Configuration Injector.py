server_config={
    "ip": "192.168.1.1",
    "port": 8080,
    "protocol": "HTTPS"
}

def connect_device(ip, port, protocol):
    print(f"connecting to {ip} on {port} using {protocol}")
connect_device(**server_config)