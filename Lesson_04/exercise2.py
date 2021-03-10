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
    "session_log": "cisco3.out",
}

with ConnectHandler(**my_device) as net_connect:

    initials = "AbC"
    filename = f"flash:testx.txt"
    newfilename = f"flash:test-{initials}.txt"
    cmd = f"copy {filename} {newfilename}"

    output = net_connect.send_command(
        cmd,
        expect_string=r"Destination filename",
        strip_prompt=False,
        strip_command=False,
    )
    output += net_connect.send_command(
        "\n", expect_string=r"confirm", strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command(
        "y", expect_string=r"#", strip_prompt=False, strip_command=False
    )
    print(output)
