import os
from netmiko import ConnectHandler
from getpass import getpass
from time import time

# Code so automated tests will run properly
password = (
    os.getenv("NETMIKO_PASSWORD")
    if os.getenv("NETMIKO_PASSWORD")
    else getpass()
)

my_device = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "fast_cli": False,
}

start = time()
with ConnectHandler(**my_device) as net_connect:
    output = net_connect.send_command(
        "show run", delay_factor=5, max_loops=1000
    )
    print(output)
end = time()
total_seconds = end - start

print(f"Seconds elapsed = {total_seconds}.")
