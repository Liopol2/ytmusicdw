import tkinter as tk
from pytube import YouTube

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("Pegar link y despues Enter")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        yt = YouTube(self.contents.get())
        #Buscar audio de mas calidad
        stream = yt.streams.filter(only_audio=True).order_by("abr").last()
        #Descargar
        stream.download()
        self.contents.set("Listo")
root = tk.Tk()
myapp = App(root)
myapp.mainloop()