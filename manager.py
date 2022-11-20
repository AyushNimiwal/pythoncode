from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDFloatingActionButton,MDTextButton
from kivymd.uix.textfield import MDTextField
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
user_main="""
MDLabel:
    text:"Enter Manager ID"
    pos_hint:{"center_x":0.5,"center_y":0.68}
    halign:"center"
    theme_text_color:"Primary"
    font_style:"H5"

"""
user_ID="""
MDTextField:
    hint_text:"Enter ID"
    pos_hint:{"center_x":0.5,"center_y":0.58}
    size_hint_x:None
    width:300
"""
user_password="""
MDTextField:
    hint_text:"Enter Password"
    helper_text:"Special charcters _,@,#,$ etc. are not allowed"
    helper_text_mode:"on_focus"
    pos_hint:{"center_x":0.5,"center_y":0.48}
    size_hint_x:None
    width:300
"""
image1 = """
Image:
    source:"C://Users//ayush//PycharmProjects//pythonProject//log.png"
    pos_hint:{"center_x":0.1,"center_y":0.1}
    size_hint_x:None
    width:300

"""
class demos(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Blue"
        self.theme_cls.theme_style="Dark"
        screen = Screen()
        btn_flat=MDRectangleFlatButton(text="Submit",pos_hint={"center_x":0.5,"center_y":0.38})

        usermain=Builder.load_string(user_main)
        userid=Builder.load_string(user_ID)
        userpass=Builder.load_string(user_password)
        img = Builder.load_string(image1)
        screen.add_widget(usermain)
        screen.add_widget(userid)
        screen.add_widget(userpass)
        screen.add_widget(btn_flat)
        screen.add_widget(img)
        return screen
demos().run()