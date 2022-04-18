from django.shortcuts import render, redirect
import mysql.connector as sql
import hashlib

from login.views import loginaction
fn=''
ln=''
s=''
em=''
pwd=''
# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
                epwd=hashlib.md5(pwd.encode()).hexdigest()
        
        c="insert into users Values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,epwd)
        cursor.execute(c)
        m.commit()
        return redirect('../login')

    return render(request,'signup_page.html')