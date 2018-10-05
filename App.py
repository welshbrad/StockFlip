from tkinter import *
import loginFile as f1
version = "0.1"


class MainWindow(Frame):

    
    bg_color = "#333"
    fg_color = "#FFF"
    padding = (10,10)

  
    def __init__(self, master):
        super().__init__()   
        self.master = master

        self.initMenus()
        self.master.title("StockFlip - version " + version)
        self.initLogin()
        #self.initMainUI()

    def initMenus(self):
        menubar = Menu(self.master)
        
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Configure User", command=options)
        filemenu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=options)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.master.config(menu=menubar)
   
    def initLogin(self):
        global e1
        global e2
        self.master.configure(background=self.bg_color)
        title_label = Label(self.master, text="Log in to StockFlip", background=self.bg_color, foreground=self.fg_color, justify=CENTER).grid(row=0, columnspan=2, padx=self.padding, pady=self.padding)
        l1 = Label(self.master, text="Username", background=self.bg_color, foreground=self.fg_color).grid(row=1, column=0, padx=self.padding, pady=self.padding)
        l2 = Label(self.master, text="Password", background=self.bg_color, foreground=self.fg_color).grid(row=2, column=0, padx=self.padding, pady=self.padding)
        
        
        e1 = Entry(self.master)
        e1.grid(row=1, column=1, padx=self.padding, pady=self.padding)
        e2 = Entry(self.master, show='*')
        e2.grid(row=2, column=1, padx=self.padding, pady=self.padding)
        #Use this form to implement login
        login_button = Button(self.master, text="Log in", command=lambda: login()).grid(row=3, column=1, padx=self.padding, pady = self.padding, sticky=E)
        create_button = Button(self.master, text="Create new User", command=lambda:createUser()).grid(row=3, column=2, padx=self.padding, pady = self.padding, sticky=E)
        
    def initMainUI(self):
        self.counter += 1
        t = tk.Toplevel(self)
        t.wm_title("Window #%s" % self.counter)
        l = tk.Label(t, text="This is window #%s" % self.counter)
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)
      
        Style().configure("TFrame", background="#333")
   

        label1 = Label(self, text="Test text").grid(column=1, row=1, sticky=W)
        label2 = Label(self, text="Test text2").grid(column=2, row=1, sticky=E)

def login():
    idE = e1.get()
    passE = e2.get()
    #print (idE, passE)
    a = f1.CheckLogin(idE, passE)
    #if a is true
        #enter program
    #else
        #show error
def createUser():
    f1.SignUp()



    

def options():
    print ("Options Menu")


def main():
    
    root = Tk()
    app = MainWindow(master=root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
