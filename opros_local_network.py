import os
import platform
import socket
import threading
from datetime import datetime

dict_ip_name = {}
start_point = 1
end_point = 255


def scan_Ip(ip, ip_opros):
    global dict_ip_name
    oc = platform.system()
    if (oc == "Windows"):
        ping_com = "ping -n 1 "
    else:
        ping_com = "ping -c 1 "

    addr = ip_opros + str(ip)
    comm = ping_com + addr
    response = os.popen(comm)
    data = response.readlines()
    print(f'Опрос {addr} ')
    for line in data:
        # print(line)
        if 'TTL' in line:
            try:
                dict_ip_name[addr] = socket.gethostbyaddr(addr)[0]
                break
            except socket.herror:
                dict_ip_name[addr] = 'Принтер'.encode()
                break


def main(net, start_point, end_point):
    global dict_ip_name
    net_split = net.split('.')
    ip_opros = net_split[0] + '.' + net_split[1] + '.' + net_split[2] + '.'
    t1 = datetime.now()
    print("Scanning in Progress:")
    for ip in range(start_point, end_point):
        if ip == int(net_split[3]):
            continue
        potoc = threading.Thread(target=scan_Ip, args=(ip, ip_opros,))
        potoc.start()
    potoc.join()
    t2 = datetime.now()
    total = t2 - t1
    print("Scanning completed in: ", total)

    return dict_ip_name


# lst_ips_file = []

def write_list_ip(name_file, ip):
    global dict_ip_name
    dict_ip_name.clear()
    if os.path.isfile(name_file) == True:
        dict_ip = {}
        with open(name_file) as file:
            for line in file:
                key, value = line.split()
                dict_ip[key] = value
        # print(dict_ip)
        main(ip, start_point=1, end_point=255)
        for key, value in dict_ip.items():

            if key not in dict_ip_name:
                dict_ip_name[key] = value
        f = open(name_file, 'w')
        # print(dict_ip_name)
        for ip, value in dict_ip_name.items():
            try:
                f.write(ip + " " + value + '\n')
            except TypeError:
                f.write(ip + " " + value.decode('cp1251') + '\n')
    else:
        main(ip, start_point=1, end_point=255)
        f = open(name_file, 'w')
        for ip, value in dict_ip_name.items():
            try:
                f.write(ip + " " + value + '\n')
            except TypeError:
                f.write(ip + " " + value.decode('cp1251') + '\n')


write_list_ip(name_file='C:\Program Files\Git\dev\localNetwork\list_ip_abk.txt', ip='192.168.144.1')
write_list_ip(name_file='C:\Program Files\Git\dev\localNetwork\list_ip_abk.txt', ip='192.168.145.1')
write_list_ip(name_file='C:\Program Files\Git\dev\localNetwork\list_ip_abk.txt', ip='192.168.146.1')
write_list_ip(name_file='C:\Program Files\Git\dev\localNetwork\list_ip_u.txt', ip='192.168.186.1')
write_list_ip(name_file='C:\Program Files\Git\dev\localNetwork\list_ip_v.txt', ip='192.168.143.1')
write_list_ip(name_file='C:\Program Files\Git\dev\localNetwork\list_ip_s.txt', ip='192.168.152.1')
write_list_ip(name_file='C:\Program Files\Git\dev\localNetwork\list_ip_z.txt', ip='192.168.187.1')
