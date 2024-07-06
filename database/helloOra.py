import cx_Oracle

user="Sembw"
pwd="nos0eibe"
dsn="molbporact-scan.mol.sys.corp:1521/ora2testdb.mol.sys.corp"

con = cx_Oracle.connect(user, pwd, dsn)

print("OK! Database version:", con.version)

# cur = con.cursor()

# cur.execute("SELECT owner, table_name FROM all_tables")
# for row in cur:
#     print(row)

cur = con.cursor()
cur.execute("select * from mm_02 where rownum < 10")
for row in cur:
    print(row)


print("End of program")