from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class Atvd(App):
    def build(self):

        box_principal = BoxLayout(orientation='vertical')
        box1 = BoxLayout(orientation='horizontal')
        lbl_numero1 = Label(text ="Digite o 1o numero")
        txt_numero1 = TextInput()
        box1.add_widget(lbl_numero1)
        box1.add_widget(txt_numero1)

        box2 = BoxLayout(orientation='horizontal')
        lbl_numero2 = Label(text ="Digite o 2o numero")
        txt_numero2 = TextInput()
        btn_somar = Button(text="Somar")
        box2.add_widget(lbl_numero2)
        box2.add_widget(txt_numero2)

        box_principal.add_widget(box1)
        box_principal.add_widget(box2)
        box_principal.add_widget(btn_somar)

        return box_principal

obj_Atvd = Atvd()
obj_Atvd.run()