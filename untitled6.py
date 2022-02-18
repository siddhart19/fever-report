from tkinter import *
root = Tk()
root.title("Fever_Report")
root.geometry("400x00")

question1_radioButton=StringVar(value="0")

question1=Label(root, text ="Do you expirence shortness of breath during activities")
question1.pack()
question1_r1=Radiobutton(root, text = "yes", variable=question1_radioButton, value="yes")
question1_r1.pack()
question1_r2=Radiobutton(root, text = "no", variable=question1_radioButton, value="no")
question1_r2.pack()

question3=Label(root, text="do you have swelling on your feet/ankels/legs(shoes feel tighter)or abdomen")
question3.pack()
question3_r1=Radiobutton(root, text = "yes", variable=question1_radioButton, value="yes")
question3_r1.pack()
question3_r2=Radiobutton(root, text = "no", variable=question1_radioButton, value="no")
question3_r2.pack()

question4=Label(root, text ="Do you feel any of these symptoms - confusion,disorentation or memory loss")
question4.pack()
question4_r1=Radiobutton(root, text = "yes", variable=question1_radioButton, value="yes")
question4_r1.pack()
question4_r2=Radiobutton(root, text = "no", variable=question1_radioButton, value="no")
question4_r2.pack()

question5=Label(root, text ="Do you experience shortness of breath while resting or sleeping")
question5.pack()
question5_r1=Radiobutton(root, text = "yes", variable=question1_radioButton, value="yes")
question5_r1.pack()
question5_r2=Radiobutton(root, text = "no", variable=question1_radioButton, value="no")
question5_r2.pack()

def report():
       score = 0
if question1_Radiobuttonget()=="yes":
        score = score+20
        print(score)
if question2_Radiobutton.get()=="yes":
        score = score+20
        print(score)
if question3_Radiobutton.get()=="yes":
        score = score+20
        print(score)
        
if score <= 10:
        messagebox.showinfo("Report","You don't need to visit a doctor.")
elif  score >= 20 and score <= 30: 
        messagebox.showinfo("Report","You might perhaps have to visit a doctor")
else :
        messagebox.showinfo("Report","I strongly advise you to visit a doctor")
btn = Button(root, text= "click me", command= report)
btn.pack()
root.mainloop()