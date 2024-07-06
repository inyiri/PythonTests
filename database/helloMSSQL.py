import pymssql

#jdbc:jtds:sqlserver://MOLSQLCLU122:1433/NAV_Online_Invoice;domain=MOL;useNTLMv2=true;schema=dbo"/>
#user:inyiri

conn = pymssql.connect(
    host=r'MOLSQLCLU122',
    user=r'MOL\inyiri',
    password='Ildi1234@',
    database='NAV_Online_Invoice'
)

cur = conn.cursor()
cur.execute("select top 3 requestID, invoicenumber from Invoice")
for row in cur:
    print(row)


