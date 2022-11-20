import kivymd
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDFloatingActionButton,MDTextButton
from kivymd.uix.textfield import MDTextField
from kivy.lang.builder import Builder
from kivy.uix.image import Image
employee="""
MDRectangleFlatButton:
    text:"Employee"
    pos_hint:{"center_x":0.4,"center_y":0.4}
"""
manger="""
MDRectangleFlatButton:
    text:"Manager"
    pos_hint:{"center_x":0.6,"center_y":0.4}
"""
admin="""
MDRectangleFlatButton:
    text:"Admin"
    pos_hint:{"center_x":0.9,"center_y":0.1}
"""
image = """
Image:
    source:"C://Users//ayush//PycharmProjects//pythonProject//lo.png"
    pos_hint:{"center_x":0.5,"center_y":0.7}
    size_hint_x:None
    width:300

"""
class screen1(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Cyan"
        self.theme_cls.theme_style = "Dark"
        screen=Screen()
        emp=Builder.load_string(employee)
        man=Builder.load_string(manger)
        adm=Builder.load_string(admin)
        imag = Builder.load_string(image)
        screen.add_widget(imag)
        screen.add_widget(emp)
        screen.add_widget(man)
        screen.add_widget(adm)
        return screen
screen1().run()