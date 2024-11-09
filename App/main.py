from tkinter import *
root=Tk()
root.title("EduReach")
root.geometry("900x600")


def home():
    global home_button
    global frame_1
    global label_1
    global button_1
    global button_2
    global exit_button
    global frame_2

    frame_2.grid_forget()

    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",state=DISABLED,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)


    frame_1=LabelFrame(root,padx=330,pady=10,bd=5)

    label_1=Label(frame_1,text="EduReach",fg="red",font="calibri 20 bold",bd=5)
    label_1.pack()



    frame_2=LabelFrame(root,padx=330,pady=10,bd=5)
    label_2=Label(frame_2,text="Welcome to EduReach",fg="purple",bd=5,font="bold")

    frame_2.grid(row=1,column=0,padx=5,pady=5,columnspan=3)
    label_2.grid(row=0,column=0,padx=5,sticky=W+E,columnspan=2)


    button_1=Button(root,text="Sign In",fg="red",font="calibri 20 bold",command=sign_in,bd=5)
    button_2=Button(root,text="Sign up",fg="red",font="calibri 20 bold",command=sign_up,bd=5)
    exit_button=Button(root,text="Exit",fg="red",font="calibri 20 bold",command=root.quit,bd=5)

    button_1.grid(row=2,column=1,padx=5,pady=5)
    button_2.grid(row=3,column=1,padx=5,pady=5)
    exit_button.grid(row=4,column=2,padx=5,pady=5)

    frame_1.grid(row=0,column=0,padx=5,pady=5,columnspan=3)
    return 0

def sign_in():
    global home_button
    global frame_2

    frame_2.grid_forget()
    button_1.grid_forget()
    button_2.grid_forget()

    frame_2=LabelFrame(root,padx=97,pady=10,bd=5)
    label_1=Label(frame_2,text="Enter Username",fg="purple",bd=5,relief=SUNKEN,font="bold")
    e=Entry(frame_2,width=55,fg="blue",bd=5,font="bold")
    label_2=Label(frame_2,text="Enter Username",fg="purple",bd=5,relief=SUNKEN,font="bold")
    e2=Entry(frame_2,width=55,fg="blue",bd=5,font="bold")

    button_main=Button(frame_2,text="Sign In",fg="red",bd=5,font="calibri 17 bold",command=dashboard)
    button_main.grid(row=5,column=1,columnspan=2)


    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=home,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

    frame_2.grid(row=1,column=0,columnspan=3,padx=5,pady=5)
    label_1.grid(row=0,column=0,padx=5,sticky=W+E)
    e.grid(row=0,column=1,columnspan=2)
    label_2.grid(row=1,column=0,padx=5,sticky=W+E)
    e2.grid(row=1,column=1,columnspan=2)
    return 0

def sign_up():
    global home_button
    global frame_2

    frame_2.grid_forget()
    button_1.grid_forget()
    button_2.grid_forget()

    frame_2=LabelFrame(root,padx=97,pady=10,bd=5)
    label_1=Label(frame_2,text="Enter Your Name",fg="purple",bd=5,relief=SUNKEN,font="bold")
    e=Entry(frame_2,width=55,fg="blue",bd=5,font="bold")
    label_2=Label(frame_2,text="Make Username",fg="purple",bd=5,relief=SUNKEN,font="bold")
    e2=Entry(frame_2,width=55,fg="blue",bd=5,font="bold")
    label_3=Label(frame_2,text="Enter Password",fg="purple",bd=5,relief=SUNKEN,font="bold")
    e3=Entry(frame_2,width=55,fg="blue",bd=5,font="bold")
    label_4=Label(frame_2,text="Confirm Password",fg="purple",bd=5,relief=SUNKEN,font="bold")
    e4=Entry(frame_2,width=55,fg="blue",bd=5,font="bold")
    label_5=Label(frame_2,text="Enter Email",fg="purple",bd=5,relief=SUNKEN,font="bold")
    e5=Entry(frame_2,width=55,fg="blue",bd=5,font="bold")

    button_sign_up=Button(frame_2,text="Create Account and Sign In",fg="red",bd=5,font="calibri 17 bold",command=sign_in)
    button_sign_up.grid(row=5,column=1,columnspan=2)


    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=home,bd=5)

    frame_2.grid(row=1,column=0,columnspan=3,padx=5,pady=5)

    label_1.grid(row=0,column=0,padx=5,sticky=W+E)
    e.grid(row=0,column=1,columnspan=2)
    label_2.grid(row=1,column=0,padx=5,sticky=W+E)
    e2.grid(row=1,column=1,columnspan=2)
    label_3.grid(row=2,column=0,padx=5,sticky=W+E)
    e3.grid(row=2,column=1,columnspan=2)
    label_4.grid(row=3,column=0,padx=5,sticky=W+E)
    e4.grid(row=3,column=1,columnspan=2)
    label_5.grid(row=4,column=0,padx=5,sticky=W+E)
    e5.grid(row=4,column=1,columnspan=2)

    home_button.grid(row=4,column=0,padx=5,pady=5)
    return 0

def dashboard():
    global home_button
    global frame_2

    frame_2.grid_forget()
    button_1.grid_forget()
    button_2.grid_forget()
    home_button.grid_forget()

    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",state=DISABLED,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

    frame_2=LabelFrame(root,padx=97,pady=10,bd=5)
    frame_2.grid(row=1,column=0,columnspan=3,padx=5,pady=5)

    but_1=Button(frame_2,text="Online Class",padx=50,pady=50,fg="red",font="calibri 20 bold",bd=5,command=online_class)
    but_2=Button(frame_2,text="Recorded Vedio",padx=50,pady=50,fg="red",font="calibri 20 bold",bd=5,command=recorded_vedio)
    but_3=Button(frame_2,text="Content",padx=50,pady=50,fg="red",font="calibri 20 bold",bd=5,command=content)
    but_4=Button(frame_2,text="Chatting",padx=50,pady=50,fg="red",font="calibri 20 bold",bd=5,command=chatting)

    but_1.grid(row=0,column=0)
    but_2.grid(row=0,column=1)
    but_3.grid(row=1,column=0)
    but_4.grid(row=1,column=1)

def online_class():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=dashboard,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def recorded_vedio():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=dashboard,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def content():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=dashboard,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def chatting():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=dashboard,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",state=DISABLED,bd=5)
home_button.grid(row=4,column=0,padx=5,pady=5)


frame_1=LabelFrame(root,padx=330,pady=10,bd=5)

label_1=Label(frame_1,text="EduReach",fg="red",font="calibri 20 bold",bd=5)
label_1.pack()



frame_2=LabelFrame(root,padx=330,pady=10,bd=5)
label_2=Label(frame_2,text="Welcome to EduReach",fg="purple",bd=5,font="bold")

frame_2.grid(row=1,column=0,padx=5,pady=5,columnspan=3)
label_2.grid(row=0,column=0,padx=5,sticky=W+E,columnspan=2)


button_1=Button(root,text="Sign In",fg="red",font="calibri 20 bold",command=sign_in,bd=5)
button_2=Button(root,text="Sign up",fg="red",font="calibri 20 bold",command=sign_up,bd=5)
exit_button=Button(root,text="Exit",fg="red",font="calibri 20 bold",command=root.quit,bd=5)

button_1.grid(row=2,column=1,padx=5,pady=5)
button_2.grid(row=3,column=1,padx=5,pady=5)
exit_button.grid(row=4,column=2,padx=5,pady=5)

frame_1.grid(row=0,column=0,padx=5,pady=5,columnspan=3)


root.mainloop()