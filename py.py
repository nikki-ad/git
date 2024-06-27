from mysql.connector import connect , Error
from tkinter import*
root=Tk()
def get_db_connection():
    return connect(
        host="localhost",
        user="root",
        password="",
        database="db_first"
    )
def sabt():
    global bookName_E
    global Author_E
    global publish_E
    formSabt=Tk()
    bookName=Label(formSabt,text="esm ketab")
    bookName.pack()

    bookName_E=Entry(formSabt)
    bookName_E.pack()

    Author=Label(formSabt,text="Author")
    Author.pack()

    Author_E=Entry(formSabt)
    Author_E.pack()

    publish=Label(formSabt,text="publisher")
    publish.pack()

    publish_E=Entry(formSabt)
    publish_E.pack()

    
    submit_btn=Button(formSabt,command=submit,text="submit")
    submit_btn.pack()
    formSabt.mainloop()


def submit():
    a=bookName_E.get()
    b=Author_E.get()
    c=publish_E.get()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("insert into t_book(book_Name,Author,publisher) values(%s,%s,%s)",(a,b,c))
    conn.commit()
    conn.close() 
    bookName_E.delete(0,"end")
    Author_E.delete(0,"end")
    publish_E.delete(0 , "end")


sabt_btn=Button(root,text="sabt",command=sabt,bg="green")
sabt_btn.grid(row=0,column=0)

def hazf():
    global bookName_E1
    formhazf=Tk()
    bookName1=Label(formhazf,text="esm ketab")
    bookName1.pack()

    bookName_E1=Entry(formhazf)
    bookName_E1.pack()
    delete=Button(formhazf,text="delete",command=dell)
    delete.pack()
    formhazf.mainloop()

def dell():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("delete from t_book where book_Name=%s;",(bookName_E1.get(),))
    conn.commit()
    conn.close() 
    bookName_E1.delete(0,"end")



def search():
    global search_E
    formsearch=Tk()
    search=Label(formsearch,text="esm ketab")
    search.pack()
    search_E=Entry(formsearch)
    search_E.pack()
    search_btn=Button(formsearch,text="search",command=jostoju)
    search_btn.pack()
    formsearch.mainloop()


def jostoju():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("select * from t_book where book_Name=%s;",(search_E.get(),))
    j=cursor.fetchall()
    for i in j:
        print(i)
    conn.close() 
    search_E.delete(0,"end")


def show():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("select * from t_book;")
    s=cursor.fetchall()
    for i in s:
        print(i)
    conn.close() 




hazf_btn=Button(root,text="hazf",bg="red",command=hazf)
hazf_btn.grid(row=1,column=0)

j_btn=Button(root,text="search",command=search)
j_btn.grid(row=2,column=0)

namayesh_btn=Button(root,text="show",command=show)
namayesh_btn.grid(row=3,column=0)

root.mainloop()