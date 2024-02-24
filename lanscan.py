import tkinter as tk
from tkinter import messagebox
import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def print_result(results_list):
    if results_list:
        result_str = "IP Address\t\tMAC Address\n"
        result_str += "----------------------------------------------------\n"
        for client in results_list:
            result_str += f"{client['ip']}\t\t{client['mac']}\n"
        result_text.config(state=tk.NORMAL)
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, result_str)
        result_text.config(state=tk.DISABLED)
    else:
        messagebox.showinfo("No Result", "No devices found in the LAN.")

def start_scan():
    ip_prefix = '.'.join(ip_entry.get().split('.')[:-1]) + '.'
    if ip_prefix:
        scan_result = scan(ip_prefix + '1/24')
        print_result(scan_result)
    else:
        messagebox.showerror("Error", "Please enter an IP address range.")

# Create GUI
window = tk.Tk()
window.title("Network Scanner")

# IP Entry
tk.Label(window, text="Enter IP Range Prefix:").pack()
ip_entry = tk.Entry(window, width=40)
ip_entry.pack()

# Scan Button
scan_button = tk.Button(window, text="Scan", command=start_scan)
scan_button.pack()

# Result Text
result_text = tk.Text(window, height=15, width=50)
result_text.pack()

window.mainloop()
