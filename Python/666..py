#!/usr/bin/python  
#-*-coding:utf-8-*-
#userbiubiubiu

# client 客户端
# import socket
# sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #连接服务器
# sock.connect(('127.0.0.1',8888))
# while True:
#     reg=input('!!!')
#     if reg!=exit:
#         sock.send(reg.encode('utf-8'))
#         #需要接收数据
#         msg=sock.recv(1024)
#         print(msg.decode('utf-8'))
#         #断开连接
#     else:
#         sock.close()

#
# import socket
# sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #连接服务器
# host=('127.0.0.1',9888)
# while True:
#     sock.sendto('发送请求'.encode('utf-8'),host)
#     #接收数据
#     msg=sock.recv(1024)
#     print(msg.decode('utf-8'))
#     sock.close()
