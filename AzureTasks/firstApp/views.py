from django.shortcuts import render
from django.views import View
import mysql.connector as sql

fname = ''
lname = ''
email = ''
classs = ''
course = ''

def index(request):
    global fname, lname, email, classs, course
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", password="root", database="feedbackform")
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "first_name":
                fname = value
            if key == "last_name":
                lname = value
            if key == "email":
                email = value
            if key == "class":
                classs = value
            if key == "course":
                course = value

        c = "INSERT INTO feedback (first_name, last_name, email, class, course) VALUES (%s, %s, %s, %s, %s)"
        data = (fname, lname, email, classs, course)
        cursor.execute(c, data)
        m.commit()
    return render(request, 'index.html')
