import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
import random
Builder.load_file("LoginPage.kv")

sm = ScreenManager()


class LoginComponent(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def is_valid_login(self):
        email = self.email.text
        password = self.password.text
        message = self.ids['status']

        if email == password and email != '' and password != '':
            message.text = 'Pass'
            message.font_size = 20
            message.color = (1,0,1,1)
            sm.current = "mainpage"

            self.email.text = ''
            self.password.text = ''
        else:
            message.text = 'No Pass'
            message.font_size = 100
            message.color = (0,1,1,1)

            self.email.text = ''
            self.password.text = ''
            
        print(f"Login Valid, {email} {password}")

class MainPage(Screen):
    
    def exit(self):
        sm.current = 'login'

class MyApp(App):
    def build(self):
        
        sm.add_widget(LoginComponent(name="login"))
        sm.add_widget(MainPage(name="mainpage"))
        return sm

if __name__ == '__main__':
    MyApp().run()