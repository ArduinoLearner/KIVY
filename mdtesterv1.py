

import kivy

kivy.require("2.0.0")

# Import widgets
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.button import MDFlatButton
from kivymd.uix.slider import slider
from kivymd.uix.screen import Screen
        

class MainApp(MDApp):

    # Function creator
    def build(self):
        # Create class Screen1
        screen = Screen()
        
        # Create Widgets
        btn_flat= MDRaisedButton(text="BISH",
        pos_hint={'center_x':0.5,'center_y':0.5},
        )
        
        # Add Widgets to Screen1
        screen.add_widget(btn_flat)

        return screen # Return the screen



MainApp().run()
