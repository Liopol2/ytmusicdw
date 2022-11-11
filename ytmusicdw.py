import tkinter as tk
from pytube import YouTube,Playlist
import platform,os 
#get environment variables
usuario=os.getlogin()
sistema=platform.system()
musicfolder=''
   
if sistema == 'Windows':
    musicfolder = os.path.join('C:\\Users\\',usuario,'Music')
else:
    musicfolder ='~/Music'

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        #url entry
        self.url = tk.Entry(width=41, font='Impact 20',justify='center')
        self.url.pack()

        #destination folder Label
        self.folder= tk.Label(text='Destino: ' + musicfolder)
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
    
    def validate_link(self,event):
        link=self.contents.get()        
        match len(link):
            case 71 | 91:
                self.url.config(fg='blue')
                playlist=Playlist(self.contents.get())
                for video in playlist.videos:
                    self.contents.set('Descargando: ' + v.title)
                    v=video.streams.filter(only_audio=True).order_by("abr").last()
                    v.download(output_path=musicfolder)
                self.contents.set('Playlist Descargada')
            case 61 | 43:
                self.url.config(fg='green')            
                link=link[0:42]
                yt = YouTube(link)
                #Buscar audio de mas calidad
                stream = yt.streams.filter(only_audio=True).order_by("abr").last()
                #Descargar
                stream.download(output_path=musicfolder)
                self.contents.set('Cancion Descargada')
            case 28:
                self.url.config(fg='green')
                yt = YouTube(link)
                #Buscar audio de mas calidad
                stream = yt.streams.filter(only_audio=True).order_by("abr").last()
                #Descargar
                stream.download(output_path=musicfolder)
                self.contents.set('Cancion Descargada')
            case _:
                self.url.config(fg='red')
                self.contents.set('Error')
root = tk.Tk()
myapp = App(root)
myapp.mainloop()