from tkinter import *
import wikipedia
def on_press () :
    text.delete(1.0,END)
    topic=get_q.get()
    text.insert(INSERT, wikipedia.summary(topic))
                 
root = Tk()
root.title("WIKI Search App")
question = Label(root,text='Question')
question.pack()
get_q= Entry(root,bd=5)
get_q.pack()
submit=Button (root,text= 'Search',command=on_press)
submit.pack()
text=Text(root)
text.pack()

root.mainloop()