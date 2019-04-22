import socket
import threading
import time


def recv_msg(udp_socket):
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data[0].decode("utf8"))


def send_msg(udp_socket, des_ip):
    while True:
        send_data = input("输入数据:")
        udp_socket.sendto(send_data.encode("utf8"), des_ip)


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("127.0.0.1", 7891))
    des_ip = ("127.0.0.1", 7890)
    t1 = threading.Thread(target=recv_msg, args=(udp_socket,))
    t2 = threading.Thread(target=send_msg, args=(udp_socket, des_ip))
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
