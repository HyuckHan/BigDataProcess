from socket import *

BUFSIZE = 1024
PORT = 8080

def parserequest(msg):
    msg = msg.split("\n")[0]
    url = msg.split()[1]
    val = url.split('/')
    if len(val) < 4:
        return None

    print(val)
    if val[2] == '+': return int(val[1]) + int(val[3])
    elif val[2] == '-': return int(val[1]) - int(val[3])
    elif val[2] == '*': return int(val[1]) * int(val[3])
    else: return int(val[1]) / int(val[3])

def main():
    listen_sock = socket(AF_INET, SOCK_STREAM)
    listen_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    listen_sock.bind(('', PORT))
    listen_sock.listen(1)

    while 1:
        conn, addr = listen_sock.accept()
        data = conn.recv(BUFSIZE).decode("UTF-8")
        rslt = parserequest(data)
        if (rslt == None):
            rslt = 0

        msg = """HTTP/1.1 200 OK

        <html><body>Calculation Results: %d</body></html>""" % rslt

        conn.sendall(msg.encode("UTF-8"))
        conn.close()

main()
