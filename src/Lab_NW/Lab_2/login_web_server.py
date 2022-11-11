from socket import *
import db_user

BUFSIZE = 1024
PORT = 8080

def parserequest(msg): 
	msg = msg.split("\n")[0] 
	url = msg.split()[1] 
	val = url.split('/') 
	val_len = len(val)

	if val[1] == "signup" and val_len == 5:
		ret = db_user.signup( val[2], val[3], val[4])
		if ret == 0:
			return "Thank you for signing up!!"
		elif ret == 1:
			return "Duplicated ID"
		else:
			return "unknown error"
	elif val[1] == "signin" and val_len==4:
		ret = db_user.signin( val[2], val[3])
		return ret
	else:
		return "Please Sign in or Sign up"


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

		<html><body>%s</body></html>""" % rslt 
		conn.sendall(msg.encode("UTF-8")) 
		conn.close()

main()
