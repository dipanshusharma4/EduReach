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

    frame_2=LabelFrame(root,padx=97,pady=10,bd=5)
    frame_2.grid(row=1,column=0,columnspan=3,padx=5,pady=5)

    class_1_c=Button(frame_2,text="Class 1",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_content)
    class_2_c=Button(frame_2,text="Class 2",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_2_content)
    class_3_c=Button(frame_2,text="Class 3",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_3_content)
    class_4_c=Button(frame_2,text="Class 4",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_4_content)
    class_5_c=Button(frame_2,text="Class 5",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_5_content)
    class_6_c=Button(frame_2,text="Class 6",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_6_content)
    class_7_c=Button(frame_2,text="Class 7",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_7_content)
    class_8_c=Button(frame_2,text="Class 8",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_8_content)
    class_9_c=Button(frame_2,text="Class 9",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_9_content)
    class_10_c=Button(frame_2,text="Class 10",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_10_content)
    class_11_c=Button(frame_2,text="Class 11",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_11_content)
    class_12_c=Button(frame_2,text="Class 12",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_12_content)

    class_1_c.grid(row=0,column=0)
    class_2_c.grid(row=0,column=1)
    class_3_c.grid(row=0,column=2)
    class_4_c.grid(row=1,column=0)
    class_5_c.grid(row=1,column=1)
    class_6_c.grid(row=1,column=2)
    class_7_c.grid(row=2,column=0)
    class_8_c.grid(row=2,column=1)
    class_9_c.grid(row=2,column=2)
    class_10_c.grid(row=3,column=0)
    class_11_c.grid(row=3,column=1)
    class_12_c.grid(row=3,column=2)
    



def chatting():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=dashboard,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_1_content():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

    frame_2=LabelFrame(root,padx=97,pady=10,bd=5)
    frame_2.grid(row=1,column=0,columnspan=3,padx=5,pady=5)

    english_button=Button(frame_2,text="English",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_English)
    maths_button=Button(frame_2,text="Maths",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Maths)
    science_button=Button(frame_2,text="Science",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Science)
    hindi_button=Button(frame_2,text="Hindi",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Hindi)
    urdu_button=Button(frame_2,text="Urdu",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Urdu)
    social_science_button=Button(frame_2,text="Social Science",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Social_Sciecne)

    english_button.grid(row=0,column=0)
    maths_button.grid(row=0,column=1)
    science_button.grid(row=1,column=0)
    urdu_button.grid(row=1,column=1)
    hindi_button.grid(row=2,column=0)
    social_science_button.grid(row=2,column=1)

def class_1_sub_English():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_1_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)


def class_1_sub_Maths():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_1_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_1_sub_Science():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_1_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_1_sub_Urdu():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_1_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_1_sub_Hindi():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_1_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_1_sub_Social_Sciecne():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_1_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)


def class_2_content():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

    frame_2=LabelFrame(root,padx=97,pady=10,bd=5)
    frame_2.grid(row=1,column=0,columnspan=3,padx=5,pady=5)

    english_button=Button(frame_2,text="English",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_English)
    maths_button=Button(frame_2,text="Maths",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Maths)
    science_button=Button(frame_2,text="Science",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Science)
    hindi_button=Button(frame_2,text="Hindi",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Hindi)
    urdu_button=Button(frame_2,text="Urdu",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Urdu)
    social_science_button=Button(frame_2,text="Social Science",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Social_Sciecne)

    english_button.grid(row=0,column=0)
    maths_button.grid(row=0,column=1)
    science_button.grid(row=1,column=0)
    urdu_button.grid(row=1,column=1)
    hindi_button.grid(row=2,column=0)
    social_science_button.grid(row=2,column=1)

def class_2_sub_English():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_2_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)


def class_2_sub_Maths():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_2_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_2_sub_Science():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_2_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_2_sub_Urdu():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_2_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_2_sub_Hindi():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_2_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_2_sub_Social_Sciecne():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_2_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)


def class_3_content():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

    frame_2=LabelFrame(root,padx=97,pady=10,bd=5)
    frame_2.grid(row=1,column=0,columnspan=3,padx=5,pady=5)

    english_button=Button(frame_2,text="English",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_English)
    maths_button=Button(frame_2,text="Maths",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Maths)
    science_button=Button(frame_2,text="Science",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Science)
    hindi_button=Button(frame_2,text="Hindi",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Hindi)
    urdu_button=Button(frame_2,text="Urdu",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Urdu)
    social_science_button=Button(frame_2,text="Social Science",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Social_Sciecne)

    english_button.grid(row=0,column=0)
    maths_button.grid(row=0,column=1)
    science_button.grid(row=1,column=0)
    urdu_button.grid(row=1,column=1)
    hindi_button.grid(row=2,column=0)
    social_science_button.grid(row=2,column=1)

def class_3_sub_English():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_3_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)


def class_3_sub_Maths():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_3_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_3_sub_Science():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_3_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_3_sub_Urdu():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_3_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_3_sub_Hindi():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_3_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_3_sub_Social_Sciecne():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_3_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)


def class_4_content():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

    frame_2=LabelFrame(root,padx=97,pady=10,bd=5)
    frame_2.grid(row=1,column=0,columnspan=3,padx=5,pady=5)

    english_button=Button(frame_2,text="English",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_English)
    maths_button=Button(frame_2,text="Maths",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Maths)
    science_button=Button(frame_2,text="Science",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Science)
    hindi_button=Button(frame_2,text="Hindi",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Hindi)
    urdu_button=Button(frame_2,text="Urdu",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Urdu)
    social_science_button=Button(frame_2,text="Social Science",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Social_Sciecne)

    english_button.grid(row=0,column=0)
    maths_button.grid(row=0,column=1)
    science_button.grid(row=1,column=0)
    urdu_button.grid(row=1,column=1)
    hindi_button.grid(row=2,column=0)
    social_science_button.grid(row=2,column=1)

def class_4_sub_English():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_4_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)


def class_4_sub_Maths():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_4_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_4_sub_Science():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_4_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_4_sub_Urdu():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_4_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_4_sub_Hindi():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_4_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_4_sub_Social_Sciecne():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_4_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)


def class_5_content():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

    frame_2=LabelFrame(root,padx=97,pady=10,bd=5)
    frame_2.grid(row=1,column=0,columnspan=3,padx=5,pady=5)

    english_button=Button(frame_2,text="English",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_English)
    maths_button=Button(frame_2,text="Maths",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Maths)
    science_button=Button(frame_2,text="Science",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Science)
    hindi_button=Button(frame_2,text="Hindi",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Hindi)
    urdu_button=Button(frame_2,text="Urdu",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Urdu)
    social_science_button=Button(frame_2,text="Social Science",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Social_Sciecne)

    english_button.grid(row=0,column=0)
    maths_button.grid(row=0,column=1)
    science_button.grid(row=1,column=0)
    urdu_button.grid(row=1,column=1)
    hindi_button.grid(row=2,column=0)
    social_science_button.grid(row=2,column=1)

def class_5_sub_English():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_5_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)


def class_5_sub_Maths():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_5_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_5_sub_Science():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_5_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_5_sub_Urdu():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_5_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_5_sub_Hindi():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_5_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_5_sub_Social_Sciecne():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_5_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)


def class_6_content():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

    frame_2=LabelFrame(root,padx=97,pady=10,bd=5)
    frame_2.grid(row=1,column=0,columnspan=3,padx=5,pady=5)

    english_button=Button(frame_2,text="English",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_English)
    maths_button=Button(frame_2,text="Maths",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Maths)
    science_button=Button(frame_2,text="Science",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Science)
    hindi_button=Button(frame_2,text="Hindi",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Hindi)
    urdu_button=Button(frame_2,text="Urdu",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Urdu)
    social_science_button=Button(frame_2,text="Social Science",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Social_Sciecne)

    english_button.grid(row=0,column=0)
    maths_button.grid(row=0,column=1)
    science_button.grid(row=1,column=0)
    urdu_button.grid(row=1,column=1)
    hindi_button.grid(row=2,column=0)
    social_science_button.grid(row=2,column=1)

def class_6_sub_English():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_6_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)


def class_6_sub_Maths():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_6_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_6_sub_Science():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_6_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_6_sub_Urdu():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_6_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_6_sub_Hindi():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_6_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_6_sub_Social_Sciecne():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_6_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)


def class_7_content():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

    frame_2=LabelFrame(root,padx=97,pady=10,bd=5)
    frame_2.grid(row=1,column=0,columnspan=3,padx=5,pady=5)

    english_button=Button(frame_2,text="English",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_English)
    maths_button=Button(frame_2,text="Maths",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Maths)
    science_button=Button(frame_2,text="Science",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Science)
    hindi_button=Button(frame_2,text="Hindi",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Hindi)
    urdu_button=Button(frame_2,text="Urdu",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Urdu)
    social_science_button=Button(frame_2,text="Social Science",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Social_Sciecne)

    english_button.grid(row=0,column=0)
    maths_button.grid(row=0,column=1)
    science_button.grid(row=1,column=0)
    urdu_button.grid(row=1,column=1)
    hindi_button.grid(row=2,column=0)
    social_science_button.grid(row=2,column=1)

def class_7_sub_English():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_7_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)


def class_7_sub_Maths():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_7_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_7_sub_Science():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_7_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_7_sub_Urdu():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_7_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_7_sub_Hindi():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_7_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_7_sub_Social_Sciecne():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_7_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)


def class_8_content():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

    frame_2=LabelFrame(root,padx=97,pady=10,bd=5)
    frame_2.grid(row=1,column=0,columnspan=3,padx=5,pady=5)

    english_button=Button(frame_2,text="English",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_English)
    maths_button=Button(frame_2,text="Maths",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Maths)
    science_button=Button(frame_2,text="Science",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Science)
    hindi_button=Button(frame_2,text="Hindi",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Hindi)
    urdu_button=Button(frame_2,text="Urdu",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Urdu)
    social_science_button=Button(frame_2,text="Social Science",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Social_Sciecne)

    english_button.grid(row=0,column=0)
    maths_button.grid(row=0,column=1)
    science_button.grid(row=1,column=0)
    urdu_button.grid(row=1,column=1)
    hindi_button.grid(row=2,column=0)
    social_science_button.grid(row=2,column=1)

def class_8_sub_English():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_8_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)


def class_8_sub_Maths():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_8_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_8_sub_Science():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_8_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_8_sub_Urdu():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_8_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_8_sub_Hindi():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_8_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_8_sub_Social_Sciecne():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_8_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)


def class_9_content():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

    frame_2=LabelFrame(root,padx=97,pady=10,bd=5)
    frame_2.grid(row=1,column=0,columnspan=3,padx=5,pady=5)

    english_button=Button(frame_2,text="English",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_English)
    maths_button=Button(frame_2,text="Maths",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Maths)
    science_button=Button(frame_2,text="Science",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Science)
    hindi_button=Button(frame_2,text="Hindi",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Hindi)
    urdu_button=Button(frame_2,text="Urdu",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Urdu)
    social_science_button=Button(frame_2,text="Social Science",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Social_Sciecne)

    english_button.grid(row=0,column=0)
    maths_button.grid(row=0,column=1)
    science_button.grid(row=1,column=0)
    urdu_button.grid(row=1,column=1)
    hindi_button.grid(row=2,column=0)
    social_science_button.grid(row=2,column=1)

def class_9_sub_English():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_9_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)


def class_9_sub_Maths():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_9_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_9_sub_Science():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_9_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_9_sub_Urdu():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()

    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_9_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_9_sub_Hindi():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_9_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_9_sub_Social_Sciecne():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_9_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)


def class_10_content():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

    frame_2=LabelFrame(root,padx=97,pady=10,bd=5)
    frame_2.grid(row=1,column=0,columnspan=3,padx=5,pady=5)

    english_button=Button(frame_2,text="English",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_English)
    maths_button=Button(frame_2,text="Maths",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Maths)
    science_button=Button(frame_2,text="Science",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Science)
    hindi_button=Button(frame_2,text="Hindi",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Hindi)
    urdu_button=Button(frame_2,text="Urdu",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Urdu)
    social_science_button=Button(frame_2,text="Social Science",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Social_Sciecne)

    english_button.grid(row=0,column=0)
    maths_button.grid(row=0,column=1)
    science_button.grid(row=1,column=0)
    urdu_button.grid(row=1,column=1)
    hindi_button.grid(row=2,column=0)
    social_science_button.grid(row=2,column=1)

def class_10_sub_English():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_10_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)


def class_10_sub_Maths():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_10_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_10_sub_Science():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_10_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_10_sub_Urdu():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_10_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_10_sub_Hindi():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_10_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_10_sub_Social_Sciecne():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_10_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)


def class_11_content():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

    frame_2=LabelFrame(root,padx=97,pady=10,bd=5)
    frame_2.grid(row=1,column=0,columnspan=3,padx=5,pady=5)

    english_button=Button(frame_2,text="English",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_English)
    maths_button=Button(frame_2,text="Maths",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Maths)
    science_button=Button(frame_2,text="Science",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Science)
    hindi_button=Button(frame_2,text="Hindi",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Hindi)
    urdu_button=Button(frame_2,text="Urdu",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Urdu)
    social_science_button=Button(frame_2,text="Social Science",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Social_Sciecne)

    english_button.grid(row=0,column=0)
    maths_button.grid(row=0,column=1)
    science_button.grid(row=1,column=0)
    urdu_button.grid(row=1,column=1)
    hindi_button.grid(row=2,column=0)
    social_science_button.grid(row=2,column=1)

def class_11_sub_English():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_11_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)


def class_11_sub_Maths():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_11_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_11_sub_Science():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_11_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_11_sub_Urdu():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_11_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_11_sub_Hindi():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_11_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_11_sub_Social_Sciecne():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_11_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)


def class_12_content():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

    frame_2=LabelFrame(root,padx=97,pady=10,bd=5)
    frame_2.grid(row=1,column=0,columnspan=3,padx=5,pady=5)

    english_button=Button(frame_2,text="English",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_English)
    maths_button=Button(frame_2,text="Maths",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Maths)
    science_button=Button(frame_2,text="Science",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Science)
    hindi_button=Button(frame_2,text="Hindi",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Hindi)
    urdu_button=Button(frame_2,text="Urdu",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Urdu)
    social_science_button=Button(frame_2,text="Social Science",padx=10,pady=10,fg="red",font="calibri 20 bold",bd=5,command=class_1_sub_Social_Sciecne)

    english_button.grid(row=0,column=0)
    maths_button.grid(row=0,column=1)
    science_button.grid(row=1,column=0)
    urdu_button.grid(row=1,column=1)
    hindi_button.grid(row=2,column=0)
    social_science_button.grid(row=2,column=1)

def class_12_sub_English():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_12_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)


def class_12_sub_Maths():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_12_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_12_sub_Science():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_12_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_12_sub_Urdu():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_12_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_12_sub_Hindi():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_12_content,bd=5)
    home_button.grid(row=4,column=0,padx=5,pady=5)

def class_12_sub_Social_Sciecne():
    global home_button
    global frame_2

    frame_2.grid_forget()
    home_button.grid_forget()
    
    home_button=Button(root,text="Back",fg="red",font="calibri 20 bold",command=class_12_content,bd=5)
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