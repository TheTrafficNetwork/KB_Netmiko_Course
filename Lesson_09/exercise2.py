from getpass import getpass
import yaml
from netmiko import ConnectHandler, file_transfer, progress_bar

source_file = "SphynxInterfaces.txt"
dest_file = "SphynxInterfaces.txt"
direction = "get"
file_system = "flash:"
cmd = f"show interfaces | redirect {file_system}/{source_file}"


password = getpass()

cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

ssh_conn = ConnectHandler(**cisco3)

output = ssh_conn.send_command_timing(
    cmd,
    strip_prompt=False,
    strip_command=False,
)
if "[confirm]" in output:
    output += ssh_conn.send_command_timing(
        "\n",
        strip_prompt=False,
        strip_command=False,
    )

transfer_dict = file_transfer(
    ssh_conn,
    source_file=source_file,
    dest_file=dest_file,
    file_system=file_system,
    direction=direction,
    overwrite_file=True,
    progress4=progress_bar,
)
print(transfer_dict)
ssh_conn.disconnect()