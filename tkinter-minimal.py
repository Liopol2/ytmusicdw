import tkinter as tk
from pytube import YouTube

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.url = tk.Entry(width=41, font='Impact 20',justify='center')
        self.url.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("Pegar link y despues Enter")
        self.url["textvariable"] = self.contents
        def clearentry(event):
            self.url.config(fg='black')
            self.contents.set('')
        self.url.bind('<1>',clearentry)
        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.url.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self,event):
        if(len(self.url.get()) >= 43):
            link = self.url.get()
            link = link[0: 42]
            self.url.config(fg='green')
        else:
            self.url.config(fg='red')
            self.contents.set('Wachin como rompes un link?')
            exit
        yt = YouTube(self.contents.get())
        #Buscar audio de mas calidad
        stream = yt.streams.filter(only_audio=True).order_by("abr").last()
        #Descargar
        stream.download()
        self.contents.set("Listo")
root = tk.Tk()
myapp = App(root)
myapp.mainloop()