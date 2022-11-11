from socket import *
import time

def main(): 
    listen_sock = socket(AF_INET, SOCK_STREAM) 
    listen_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    listen_sock.bind(('', 8080))
    listen_sock.listen(1)

    while 1:
        conn, addr = listen_sock.accept() # 커넥션을 기다림
        data = conn.recv(1024)
        print( data )
        msg = """HTTP/1.1 200 OK


        <html><body>This time is %s</body></html>""" % time.ctime()
        conn.sendall(msg.encode("UTF-8"))
        conn.close()


main()
