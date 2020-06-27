import pymysql
import pymysql.cursors

connection=pymysql.connect(host='localhost', user='root', password='root', db='bankinfo', port=3306)
cursor = connection.cursor()
sql = """CREATE TABLE IF NOT EXISTS CUSTOMER  (
                 id INT NOT NULL AUTO_INCREMENT,
                 name VARCHAR(20) NOT NULL,
                 address VARCHAR(20),
                 cellphone VARCHAR(20),
                 PRIMARY KEY(id))
                 """
cursor.execute(sql)
sql1 = """CREATE TABLE IF NOT EXISTS ACCOUNT  (
                 accnumber INT NOT NULL,
                 balance VARCHAR(20) NOT NULL,
                 cusid INT NOT NULL,
                 PRIMARY KEY(accnumber),
                 FOREIGN KEY(cusid) REFERENCES CUSTOMER(id))
                 """
cursor.execute(sql1)
print("create successful")
# sql= """insert into customer values (1, 'xiaoerya', '930 benge', 123456), (2, 'derrick', 'fengtai district', 234567)"""
# cursor.execute(sql)
# connection.commit()

# sql= """insert into account values (123, 12, 1), (234, 14, 2)"""
# cursor.execute(sql)
# connection.commit()
number=1
cursor.execute("SELECT * FROM customer WHERE id>=?", number)
print(cursor.fetchall())