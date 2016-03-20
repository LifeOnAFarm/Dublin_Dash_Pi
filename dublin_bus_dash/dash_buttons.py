from scapy.all import *
import dublin_bus
__author__ = 'Seamus de Cleir'

"""
    Program Description:    This program senses ARP probes sent by Amazon Dash Buttons on a local network
                            and executes certain code depending on the MAC address of that button.
    Date:                   20/03/2016
"""

# Scapy takes a while to start. Statement prints when it's ready
print("Scapy ready!")


def arp_display(pkt):
    # Input your Dash Buttons MAC addresses here
    olay_mac = "f0:27:2d:6f:a6:a3"

    if pkt[ARP].op == 1:
        # ARP Probes will match 0.0.0.0
        if pkt[ARP].psrc == "0.0.0.0":

            # Matches MAC addresses of Dash Buttons
            if pkt[ARP].hwsrc == olay_mac:
                # Pushed Olay
                print("Pushed Olay")
                dublin_bus.olay_press()

            # Returns the MAC address of an unknown ARP probe
            else:
                print("ARP Probe from unknown device: " + pkt[ARP].hwsrc)

print(sniff(prn=arp_display, filter="arp", store=0))
