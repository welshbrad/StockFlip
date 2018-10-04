from PIL import Image, ImageTk
from tkinter import *
from tkinter.ttk import Frame, Label, Style

version = "0.1"


class MainWindow(Frame):
    bg_color = "#333"
    fg_color = "#FFF"
    padding = (10,10)
  
    def __init__(self):
        super().__init__()   
        self.master.title("StockFlip - version " + version)
        self.initLogin()
        #self.initUI()

    def initLogin(self):
          
        self.master.configure(background=self.bg_color)
        title_label = Label(self.master, text="Log in to StockFlip", background=self.bg_color, foreground=self.fg_color, justify=CENTER).grid(row=0, columnspan=2, padx=self.padding, pady=self.padding)
        l1 = Label(self.master, text="Username", background=self.bg_color, foreground=self.fg_color).grid(row=1, column=0, padx=self.padding, pady=self.padding)
        l2 = Label(self.master, text="Password", background=self.bg_color, foreground=self.fg_color).grid(row=2, column=0, padx=self.padding, pady=self.padding)
        
        
        e1 = Entry(self.master).grid(row=1, column=1, padx=self.padding, pady=self.padding)
        e2 = Entry(self.master).grid(row=2, column=1, padx=self.padding, pady=self.padding)
        #Use this form to implement login

        login_button = Button(self.master, text="Log in", command=lambda: Login()).grid(row=3, column=1, padx=self.padding, pady = self.padding, sticky=E)
        
        
    def initUI(self):
        
      
      
        
        self.pack(fill=BOTH, expand=1)
      
        Style().configure("TFrame", background="#333")
   

        label1 = Label(self, text="Test text").grid(column=1, row=1, sticky=W)
        label2 = Label(self, text="Test text2").grid(column=2, row=1, sticky=E)
        
def Login():
    print("Hi")
        
        
def main():
    
    root = Tk()
    app = MainWindow()
    root.mainloop()  


if __name__ == '__main__':
    main()  