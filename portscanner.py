import socket
import threading
from queue import Queue

target = ''        #Enter the target IP here   either Router,LAN,LocalHost etc
queue = Queue()
open_ports = []

#Scanning the port
def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

#Adding ports to queue
def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

#Adding scanned open ports to list
def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print(f'Port {port} is open')
            open_ports.append(port)

#Creating Portlist
portlist = range(1, 1024)
fill_queue(portlist)

#Creating Threads to fasten scanning
thread_list = []

for t in range(500):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print('Open ports are', open_ports)