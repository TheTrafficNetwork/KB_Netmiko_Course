import os
from netmiko import ConnectHandler
from getpass import getpass

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
    print(net_connect.find_prompt())
    output = net_connect.send_command("disable", expect_string=r">")
    print(output)
    print(net_connect.find_prompt())
