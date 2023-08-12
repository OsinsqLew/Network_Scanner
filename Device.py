import xml.etree.ElementTree as ET


class Device:
    def __init__(self, ip, mac):
        self.ip = ip
        self.mac = mac
        self.producer = producer_from_mac(mac)


mac_dict = None


def producer_from_mac(mac):
    global mac_dict
    if mac_dict is None:
        with open("vendorMacs.xml"):
            tree = ET.parse('vendorMacs.xml')
            root = tree.getroot()
            mac_dict = {child.attrib['mac_prefix']: child.attrib['vendor_name'] for child in root}

    mac_prefix = mac[:10].upper()
    if mac_prefix in mac_dict:
        return mac_dict[mac_prefix]
    else:
        mac_prefix = mac_prefix[:-2]
        if mac_prefix in mac_dict:
            return mac_dict[mac_prefix]
        else:
            return "Unknown"
