from datetime import datetime
from datetime import timedelta
import requests

def getDateFromString( dateStr ) -> datetime:
    date = datetime.strptime(dateStr, "%Y-%m-%d")
    return date

def getStringFromDate( date:datetime ):
    s = date.strftime("%Y-%m-%d")
    return s    

def nextDay( todayStr ):
    date = getDateFromString( todayStr )
    date = date + timedelta(days=1)
    s = getStringFromDate( date )
    return s

def urlWithDay( dateString ):
    # urlTemplate = "https://eaiqaproxy.mol.sys.corp/NavOnline3.0/navoiapi/monitoring/invoice/customerinvoiceasync?issueDate={dateStr}"
    urlTemplate = "https://eaiprodproxy.mol.sys.corp/NavOnline3.0/navoiapi/monitoring/invoice/customerinvoiceasync?issueDate={dateStr}"
    url = urlTemplate.format(dateStr=dateString)
    return url

def readNextDay():
    f = open("last-time.txt", "r")
    s = f.readline()
    f.close()
    snew = nextDay( s )
    f = open("last-time.txt", "w")
    f.write( snew )
    f.close()  
    return s



# Start program here 
# 2020-03-02
# startDateStr = readNextDay()
# url = urlWithDay( startDateStr )
# print( url )
# response = requests.get( url, verify=False )
# print( response )

cnt=0
f = open("nav-days.txt", "r")
s = f.readline()
while s:
    url = urlWithDay( s )
    print( url )
    response = requests.get( url, verify=False )
    print( response )
    cnt = cnt + 1
    s = f.readline()
f.close()
print(cnt)




