import pymysql

def signup(username, password, nickname):
	db = pymysql.connect(host="localhost", user="bigdatalab", passwd="1234", db="python_lab", charset='utf8')
	cur = db.cursor()
	try:
		cur.execute( "insert into USER values('%s', '%s', '%s')" % (username,password,nickname) )
		db.commit()
		return 0
	except pymysql.err.IntegrityError:
		return 1
	finally:
		cur.close()
		db.close()

def signin(username, password):
	db = pymysql.connect(host="localhost", user="bigdatalab", passwd="1234", db="python_lab", charset='utf8')
	#cur = db.cursor(pymysql.cursors.DictCursor)
	cur = db.cursor(pymysql.cursors.DictCursor)
	try:
		cur.execute( "select * from USER where id = '%s'" % (username))
		record = cur.fetchone() 
		if record is None:
			return "This ID does not exist"
		elif record['password'] == password: 
				return record
		else:
			return "The password is incorrect" 
	except Exception as e:
		print(e)
		return 1
	finally:
		cur.close()
		db.close()


if __name__ == "__main__": 
	print( signup( "hhyuck", "1234", "wow" ) ) 
	print( signup( "hhyuck", "1234", "wow" ) )
	print( signin( "hhyuck", "1234") )
	print( signin( "hhyuck", "12345") )
	print( signin( "hhyuck1", "12345") )
