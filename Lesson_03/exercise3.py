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
    "device_type": "arista_eos",
    "host": "arista1.lasthop.io",
    "username": "pyclass",
    "password": password,
}

with ConnectHandler(**my_device) as net_connect:
    output = net_connect.send_command(
        "show run", use_ttp=True, ttp_template="show_run_intf.ttp"
    )
    pprint(output)