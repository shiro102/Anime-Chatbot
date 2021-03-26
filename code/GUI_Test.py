import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

LARGE_FONT= ("Verdana", 12)


def send():
    return EntryBox


class GUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        image1 = Image. open("botpic.jpg")
        image1 = image1.resize((25, 25), Image. ANTIALIAS)
        image2 = Image. open("user-24.gif")
        image2 = image2.resize((25, 25), Image. ANTIALIAS)
        botimg = ImageTk.PhotoImage(image1)
        userimg = ImageTk.PhotoImage(image2)

        #Changing window image
        self.tk.call('wm', 'iconphoto', self._w,botimg )
        self.title("Anime Bot")
        self.geometry("400x500")
        
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Home, Recent):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Home)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class Home(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        ChatLog = Text(self, bd=2,relief = "ridge", bg="beige", height="100", width="50", font="Arial")
        ChatLog.config(state=NORMAL)
        
        SendButton = Button(self, font=("Verdana",12,'bold','italic'), text="Send", width="12", height=5,
                    bd=0, bg="#030bfc", activebackground="#7373ff",fg='#ffffff',
                    command= send )
        RecentButton = Button(self, font=("Verdana",12,'bold','italic'), text="Recent", width="12", height=5,
                    bd=0, bg="#030bfc", activebackground="#7373ff",fg='#ffffff',
                    command= lambda: controller.show_frame(Recent))
        EntryBox = Text(self, bd=2,relief = "ridge", bg="#e6e6e6",width="29", height="5", font="Arial")

        #Aranging the objects
        ChatLog.place(x=6,y=6, height=386, width=388)
        EntryBox.place(x=6, y=401, height=90, width=265)
        SendButton.place(x=290, y=401, height=45, width = 104)
        RecentButton.place(x=290, y=450, height=45, width = 104)
        #label = tk.Label(self, text="Home", font=LARGE_FONT)
        #label.pack(pady=10,padx=10)

        #button = tk.Button(self, text="Recent Conversation",
                            #command=lambda: controller.show_frame(Recent))
        #button.pack()


class Recent(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Recent Conversation", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(Home))
        button1.pack()


app = GUI()
app.mainloop()