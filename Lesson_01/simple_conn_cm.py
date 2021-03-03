from netmiko import ConnectHandler
from getpass import getpass

my_device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
}
with ConnectHandler(**my_device) as net_connect:
    print(net_connect.find_prompt())

print("Connection ended...")
