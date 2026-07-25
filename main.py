from kivy.app import App
from kivy.lang import Builder
from testeyt import downvideo
from testeyt import downsong


parabaixar=[]

class DownloaderApp(App):
    def build(self):
        return Builder.load_file("downloader.kv")
    
    def indexar(self):
        urls=self.root.ids.url.text.strip()
        parabaixar.append(urls)
        self.root.ids.url.text = ""
        

    def baixarmusica(self):
        self.root.ids.status.text="baixando..."
        try:
            downsong(parabaixar)
            self.root.ids.status.text="✅ musica baixada"
            parabaixar.clear()
        except Exception as e:
            self.root.ids.status.text=f"Erro:{e}"

    def baixarvideo(self):
        self.root.ids.status.text="baixando..."
        try:
            downvideo(parabaixar)
            self.root.ids.status.text="✅ video baixado"
            parabaixar.clear()
        except Exception as e:
            self.root.ids.status.text=f"Erro:{e}"

if __name__=="__main__":
    DownloaderApp().run()