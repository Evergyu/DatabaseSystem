import pymysql

con = pymysql.connect(host="192.168.167.3", port=4567, user="leeingyu", password="1234",db="madang", charset="utf8")

# STEP 3: Connection 으로부터 Cursor 생성
cur = con.cursor()

# # STEP 4: SQL문 Table 생성
# # 테이블 추가 전 테이블 상태 출력
# sql1 = '''
# SHOW TABLES;
# '''
# cur.execute(sql1)
# result=cur.fetchall()
# for x in result:
#     print(x)
#
# sql2 = '''
# CREATE TABLE New_Table(new_name VARCHAR(255))
# '''
#
# cur.execute(sql2)
# result2=cur.fetchall()
# for y in result2:
#     print(y)

# # STEP 5: SQL문 Table 검색
# sql3='''
# SHOW TABLES LIKE 'New_Table';
# '''
# cur.execute(sql3)
# if(cur.execute(sql3)==1):
#     print("Table 존재")
# else:
#     print("Table 없음")

# STEP 6: SQL문 Table 삭제
sql4='''
DROP TABLE New_Table;
'''
sql1 = '''
SHOW TABLES;
'''
cur.execute(sql4)
cur.execute(sql1)
result=cur.fetchall()
for x in result:
    print(x)


# STEP 5: DB 연결 종료
con.close()