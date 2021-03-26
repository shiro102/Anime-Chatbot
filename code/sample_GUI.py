from tkinter import *
from PIL import ImageTk, Image


base = Tk()


#Loading images and generating photo objects
image1 = Image. open("botpic.jpg")
image1 = image1.resize((25, 25), Image. ANTIALIAS)
image2 = Image. open("user-24.gif")
image2 = image2.resize((25, 25), Image. ANTIALIAS)
botimg = ImageTk.PhotoImage(image1)
userimg = ImageTk.PhotoImage(image2)

#Changing window image
base.tk.call('wm', 'iconphoto', base._w,botimg )
base.title("Anime Bot")
base.geometry("400x500")
base.resizable(width=TRUE, height=TRUE)

#Chat Window
ChatLog = Text(base, bd=2,relief = "ridge", bg="beige", height="100", width="50", font="Arial")
ChatLog.config(state=NORMAL)

#Send Button
SendButton = Button(base, font=("Verdana",12,'bold','italic'), text="Send", width="12", height=5,
                    bd=0, bg="#030bfc", activebackground="#7373ff",fg='#ffffff',
                    command= send )
RecentButton = Button(base, font=("Verdana",12,'bold','italic'), text="Recent", width="12", height=5,
                    bd=0, bg="#030bfc", activebackground="#7373ff",fg='#ffffff',
                    command= recent)

#Message Window
EntryBox = Text(base, bd=2,relief = "ridge", bg="#e6e6e6",width="29", height="5", font="Arial")

#Aranging the objects
ChatLog.place(x=6,y=6, height=386, width=388)
EntryBox.place(x=6, y=401, height=90, width=265)
SendButton.place(x=290, y=401, height=45, width = 104)
RecentButton.place(x=290, y=450, height=45, width = 104)

base.mainloop()
saveData[-1][0] = saveData[-1][0] + 1
saveData.append(['',{}])
pickle.dump(saveData,open('saveData.pkl','wb'))
print("SAVED")
