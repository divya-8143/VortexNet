"""
VortexNet IEEE Organizationally Unique Identifier (OUI) Vendor MAC Database
Maps MAC address 24-bit prefixes to network hardware manufacturers.
"""

OUI_VENDOR_MAP = {
    "00:00:0C": "Cisco Systems, Inc.",
    "00:01:42": "Cisco Systems, Inc.",
    "00:01:43": "Cisco Systems, Inc.",
    "00:01:63": "Cisco Systems, Inc.",
    "00:01:64": "Cisco Systems, Inc.",
    "00:01:96": "Cisco Systems, Inc.",
    "00:01:97": "Cisco Systems, Inc.",
    "00:01:C7": "Cisco Systems, Inc.",
    "00:01:C9": "Cisco Systems, Inc.",
    "00:02:16": "Cisco Systems, Inc.",
    "00:02:17": "Cisco Systems, Inc.",
    "00:02:3D": "Cisco Systems, Inc.",
    "00:02:4B": "Cisco Systems, Inc.",
    "00:02:7D": "Cisco Systems, Inc.",
    "00:02:7E": "Cisco Systems, Inc.",
    "00:02:8A": "Cisco Systems, Inc.",
    "00:02:B9": "Cisco Systems, Inc.",
    "00:02:BA": "Cisco Systems, Inc.",
    "00:02:FC": "Cisco Systems, Inc.",
    "00:03:31": "Cisco Systems, Inc.",
    "00:03:32": "Cisco Systems, Inc.",
    "00:03:6B": "Cisco Systems, Inc.",
    "00:03:6C": "Cisco Systems, Inc.",
    "00:03:9F": "Cisco Systems, Inc.",
    "00:03:A0": "Cisco Systems, Inc.",

    "00:05:85": "Juniper Networks",
    "00:10:DB": "Juniper Networks",
    "00:12:1E": "Juniper Networks",
    "00:14:F6": "Juniper Networks",
    "00:17:CB": "Juniper Networks",
    "00:19:E2": "Juniper Networks",
    "00:1B:C0": "Juniper Networks",
    "00:1D:B5": "Juniper Networks",
    "00:1F:12": "Juniper Networks",
    "00:21:59": "Juniper Networks",

    "00:1C:73": "Arista Networks, Inc.",
    "00:50:07": "Arista Networks, Inc.",
    "00:1F:45": "Arista Networks, Inc.",

    "00:1B:17": "Palo Alto Networks",
    "00:30:48": "Supermicro Computer, Inc.",
    "00:1E:67": "Intel Corporation",
    "00:50:56": "VMware, Inc.",
    "00:0C:29": "VMware, Inc.",
    "00:15:5D": "Microsoft Corporation",
}

def lookup_mac_vendor(mac_address: str) -> str:
    cleaned = mac_address.upper().replace("-", ":")
    prefix = ":".join(cleaned.split(":")[:3])
    return OUI_VENDOR_MAP.get(prefix, "Generic IEEE Device")
