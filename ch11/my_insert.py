import pymysql,sys
try:
    con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='mysql',
                          db='test', charset='utf8')
    cursor = con.cursor() # sql을 사용하기 위한 객체
    cursor.execute("insert into dept values (13,'대박팀','울산')")
    con.commit()
    print("입력 성공")
except:  print("에러 ",sys.exc_info())
finally: cursor.close(); con.close()