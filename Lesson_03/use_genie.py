import os
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

# Code so automated tests will run properly
# Check for environment variable, if that fails, use getpass().
password = (
    os.getenv("NETMIKO_PASSWORD")
    if os.getenv("NETMIKO_PASSWORD")
    else getpass()
)

my_device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "session_log": "Lesson_02/cisco3.out",
}

with ConnectHandler(**my_device) as net_connect:
    output = net_connect.send_command("show ip int brief", use_genie=True)
    pprint(output)