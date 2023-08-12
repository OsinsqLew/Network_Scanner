from scapy.layers.l2 import arping
import Device
# import GUI


class IpGenerator:
    def __init__(self, subnet_mask, current_ip):
        self.subnet_mask = subnet_mask.strip()
        self.current_ip = current_ip.strip()

    def generate_ips(self) -> list[str]:
        base = ip_to_int(self.subnet_mask) & ip_to_int(self.current_ip)
        ip_list = []
        for i in range(1, ip_to_int('255.255.255.255') + 1 - ip_to_int(
                self.subnet_mask)):  # range od 1 bo 198.162.0.0 nie istnieje
            ip_list.append(int_to_ip(base + i))
        return ip_list

    def scan(self):
        ips = self.generate_ips()
        send_request(ips)


def ip_to_int(ip: str) -> int:
    ip = ip.split('.')
    ip_int = 0
    for part in ip:
        ip_int = ip_int << 8
        ip_int += int(part)
    return ip_int


def int_to_ip(ip: int) -> str:
    ip_parts = []
    for _ in range(4):
        ip_parts.append(str(ip % 256))
        ip = ip >> 8
    ip_parts.reverse()
    ip_str = ".".join(ip_parts)
    return ip_str


devices = []


def send_request(ips):
    i = 0
    for ip in ips:
        i += 1
        print(i)
        result = arping(net=ip)
        if len(result[0]) == 0:
            continue
        mac = result[0][0].answer.src
        global devices
        devices.append(Device.Device(ip, mac))
        # GUI.progress_bar.step(i)
