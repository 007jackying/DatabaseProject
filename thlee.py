#! C:\Users\Dreamyx\AppData\Local\Programs\Python\Python38-32\Python.exe
import mysql.connector
import cgi


mydb = mysql.connector.connect(
    host = "localhost",
    user = "proj",
    password = "proj",
    database = "supplydb"

)

print("Content-type: text/html\n")
print("<html><head>")
print("</head><body>")
form = cgi.FieldStorage()
mycursor = mydb.cursor()   
if "pname" in form:
    p2name = form.getvalue("pname")
    tablelist = form.getlist("infor")
    columns = ','.join(tablelist)
    query = "SELECT "+columns+" from Parts P, Catalog C, Suppliers S WHERE P.pid = C.pid AND C.sid= S.sid AND P.pname = '"+p2name+"';"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    if(len(myresult)<1):
        print("<h2>error</h2>")
        print("<p>please enter a Supplier's name</p>")
    else:
        print("<table align='center' border>")
        print("<tr>")
        print("<th>" +"Sid"+ "</th>")
        print("<th>" +"Supplier's name"+ "</th>")
        print("<th>" +"Address"+ "</th>")
        print("<th>" +"Cost"+ "</th>")
        print("</tr>")
        for x in myresult:
            print("<tr>")
            for i in range(0,len(x)):
                print("<td>"+str(x[i])+"</td>")
            print("</tr>")
        print("</table></body></html>")
if "cost" in form:
    cost1 = form.getvalue("cost")
    query = "SELECT DISTINCT(S.sname) FROM Parts P, Catalog C, Suppliers S WHERE P.pid = C.pid AND S.sid =C.sid AND C.cost >= "+ cost1 +";"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    if(len(myresult)<1):
        print("<h2>error</h2>")
        print("<p>please enter a valid cost</p>")
    else:
        print("<table align='center' border>")
        print("<tr>")
        print("<th>"+"Supplier 's name"+ "</th>")
        for x in myresult:
            print("<tr>")
            print("<td>"+str(x[0])+"</td>")
            print("</tr>")
        print("</table></body></html>")
if "pid" in form:
    pid1 = form.getvalue("pid")
    query = "SELECT S1.sname,S1.address FROM Catalog C1, Suppliers S1 WHERE C1.sid = S1.sid AND C1.pid ='"+pid1+"' AND C1.cost =(SELECT MAX(C2.cost) FROM Catalog C2 WHERE C2.pid = '"+pid1+"');"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    if(len(myresult)<1):
        print("<h2>error</h2>")
        print("<p>please enter a valid pid</p>")
    else:
        print("<table align='center' border>")
        print("<tr>")
        print("<th>"+"Supplier 's name"+ "</th>")
        print("<th>" +"Address"+ "</th>")
        print("</tr>")
        for x in myresult:
            print("<tr>")
            for i in range(0,len(x)):
                print("<td>"+str(x[i])+"</td>")
            print("</tr>")
        print("</table></body></html>")
if ("color" and "address") in form:
    color1 = form.getvalue("color")
    address1 = form.getvalue("address")
    query = "SELECT DISTINCT(P.pname) FROM Suppliers S, Parts P, Catalog C WHERE S.sid = C.sid AND C.pid = P.pid AND S.address = '"+address1+"' AND C.pid IN (SELECT P1.pid FROM parts P1 WHERE color = '"+color1+"');"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    if(len(myresult)<1):
        print("<h2>error</h2>")
        print("<p>please enter a valid for color or address</p>")
    else:
        print("<table align='center' border>")
        print("<tr>")
        print("<th>"+"Part's name"+ "</th>")
        print("</tr>")
        for x in myresult:
            print("<tr>")
            for i in range(0,len(x)):
                print("<td>"+str(x[i])+"</td>")
            print("</tr>")
        print("</table></body></html>")
if "address2" in form:
    address3 = form.getvalue("address2")
    query = "SELECT S.sid,S.sname FROM Suppliers S WHERE S.address = '"+address3+"' AND S.sid NOT IN (SELECT DISTINCT sid FROM Catalog);"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    if(len(myresult)<1):
        print("<h2>error</h2>")
        print("<p>please enter valid values</p>")
    else:
        print("<table align='center' border>")
        print("<tr>")
        print("<th>"+"Sid"+ "</th>")
        print("<th>" +"Supplier 's name"+ "</th>")
        print("</tr>")
        for x in myresult:
            print("<tr>")
            for i in range(0,len(x)):
                print("<td>"+str(x[i])+"</td>")
            print("</tr>")
        print("</table></body></html>") 







        

    
