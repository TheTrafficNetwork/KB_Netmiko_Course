import yaml
from getpass import getpass
from netmiko import ConnectHandler
from netmiko import NetmikoAuthenticationException


def load_devices(device_file="lab_devices.yml"):
    device_dict = {}
    with open(device_file) as f:
        device_dict = yaml.safe_load(f)
    return device_dict


def netmiko_conn(device):
    try:
        conn = ConnectHandler(**device)
        return conn
    except NetmikoAuthenticationException:
        print(f"Authentication Failure for {device['host']}.")
    return None


if __name__ == "__main__":
    password = getpass()
    my_devices = load_devices()
    for device_name, device in my_devices.items():
        if device_name == "nxos2":
            device["password"] = password
            conn = netmiko_conn(device)
            if conn == None:
                continue
            print(conn.send_command("show ip arp vrf management"))
