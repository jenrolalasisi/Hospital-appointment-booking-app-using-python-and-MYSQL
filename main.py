from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.window import Window

Window.size = 1100, 650
Window.clearcolor =1,1,1,1


class LoginScreen(Screen):
    pass

class Dashboard(Screen):
    pass

class PatientScreen(Screen):
    pass

class ForgetPassword(Screen):
    pass

class doctorpan(Screen):
    pass
    
class WindowManager(ScreenManager):
    pass



kv = Builder.load_file("login.kv")

class MainApp(App):
    def build(self):
        return kv

MainApp().run()





