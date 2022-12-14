import tkinter as tk
from tkinter import filedialog
from pytube import YouTube,Playlist
import os 
#In case you want to change the output folder just change the next line and run the py file
#Or install pyinstaller and run pyinstaller  -F -w ytmusicdw.py to generate a new binary on the dist folder


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.musicfolder = os.path.join(os.path.expanduser('~'),'Music')
        #url entry
        self.url = tk.Entry(width=31, font='Impact 30',justify='center')
        self.url.pack()

        #convert the
        #destination folder Label
        self.folder = tk.Label(text='Destino: ' + self.musicfolder,font='25')        
        self.folder.pack()
        
        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("Pegar link y Presionar Enter")
        self.url["textvariable"] = self.contents
        
        #A function that will be called on click
        def clearentry(event):
            self.url.config(fg='black')
            self.contents.set('')
        #Bind click to the clear entry
        self.url.bind('<1>',clearentry)
        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.url.bind('<Key-Return>',
                             self.validate_link)
        #bind click on route                     
        self.folder.bind('<1>', self.clickroute)
    def validate_link(self,event):
        link=self.contents.get() 
        if 'playlist' in link: # khe 
            self.url.config(fg='blue')
            playlist=Playlist(self.contents.get())
            for video in playlist.videos:
                v=video.streams.filter(only_audio=True).order_by("abr").last()
                #fijarse si ya existe y meter break
                v.download(output_path=self.musicfolder)
            self.contents.set(playlist.title + ' Descargada')
        elif len(link)>= 28:
            self.url.config(fg='green')
            yt = YouTube(link)
            #Buscar audio de mas calidad
            stream = yt.streams.filter(only_audio=True).order_by("abr").last()
            #Descargar
            stream.download(output_path=self.musicfolder)
            self.contents.set('Cancion Descargada')
        else:
            self.contents.set('Error intente con otro link')
            
    def clickroute(self,event):
        folder=filedialog.askdirectory(initialdir = self.musicfolder,
                                        title="Seleccione una Carpeta:"                                       
                                        )
        print(folder)
        if folder != '':
            self.folder.config(text=folder,fg='red')
            self.musicfolder=folder


root = tk.Tk()
myapp = App(root)
myapp.mainloop()