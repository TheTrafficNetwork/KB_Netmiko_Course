import yaml
from getpass import getpass
from netmiko import ConnectHandler
from netmiko import NetmikoAuthenticationException
from netmiko import NetmikoTimeoutException
from paramiko.ssh_exception import SSHException


def load_devices(device_file="lab_devices.yml"):
    device_dict = {}
    with open(device_file) as f:
        device_dict = yaml.safe_load(f)
    return device_dict


def netmiko_conn(device):
    try:
        conn = ConnectHandler(**device)
        return conn
    except NetmikoTimeoutException as e:
        if "TCP connection" in str(e):
            print(f"TCP connection error on {device['host']}.")
        elif "DNS failure" in str(e):
            print("DNS failure")
        else:
            raise
    except NetmikoAuthenticationException:
        print(f"Authentication Failure for {device['host']}.")
    except SSHException as e:
        if "Error reading SSH protocol banner" in str(e):
            print("SSH banner error")
        else:
            raise
    return None


if __name__ == "__main__":
    password = getpass()
    my_devices = load_devices()
    for device_name, device in my_devices.items():
        device["password"] = password
        conn = netmiko_conn(device)
        if conn is None:
            continue
        print(conn.find_prompt())
