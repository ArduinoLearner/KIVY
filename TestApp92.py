

# import libraries 
import kivy
import requests
kivy.require("2.0.0")
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.core.audio import Sound,SoundLoader
from kivy.uix.boxlayout import BoxLayout

class MyGridLayout(BoxLayout):
    #initialize infine in comming keywords
    def __init__(self,**kwargs):
        #call gridlayout
        super(MyGridLayout,self).__init__(**kwargs)
        #add Layout properties


        

        URL = "https://www.bing.com/images/blob?bcid=ToeKpxmSUJwDXA"
        response = requests.get(URL)
        
        open("frog.jpg", "wb").write(response.content)


        open("SLF.mp3","wb").write(requests.get('https://download1074.mediafire.com/kzoqis62gnng/rbori8ya3aoqqux/SLF.mp3').content)
        self.da = Image(source="frog.jpg")

        self.add_widget(self.da)


        music = SoundLoader.load('SLF.mp3')
        music.play()

        
        


  

class T92(App): #initiate class
    def build(self):
        return MyGridLayout()
T92().run()

