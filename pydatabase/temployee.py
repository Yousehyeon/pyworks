import sqlite3

def getconn():
    conn = sqlite3.connect("c:/pydb/mydb.db")
    return conn
def select():
    conn = getconn() # 연결 객체 생성
    # print(conn)
    cursor = conn.cursor()  # 모든 조작을 수행하는 함수
    sql = "SELECT * FROM employee"
    cursor.execute(sql)
    # 전체 검색 - fetchall(), 특정 1개 검색 - fetchone()
    rs = cursor.fetchall()  # 자료구조가 리스트임, 개별 요소는 튜플임
    for i in rs:
        print(i)
    conn.close()

def insert():
    conn = getconn()
    cursor = conn.cursor()
    sql = "INSERT INTO employee VALUES ('e103', '안산', 22, 10000)"
    cursor.execute(sql)
    conn.commit()
    conn.close()

def update():
    conn = getconn()
    corsor = conn.cursor()
    sql = "UPDATE employee SET age = 40 WHERE empid = 'e101'"



def select_one():
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM employee WHERE empid = 'e103'"
    cursor.execute(sql)
    cursor.fetchone()
    rs = cursor.fetchone()
    print(rs)
    conn.close()

def delete():
    conn = getconn()
    cursor = conn.cursor()
    sql = "DELETE FROM employee WHERE empid = 'e102'"
    cursor.execute(sql)
    conn.commit()
    conn.close()

#update()
#insert()
#select_one()
delete()
select()

