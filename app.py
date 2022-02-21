from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.picker import MDDatePicker
from datetime import *
import sqlite3
from kivymd.uix.dialog import *
from kivymd.uix.list import *
from kivymd.uix.selectioncontrol import MDCheckbox

Window.size = (320, 590)

class login(Screen):

    logph = ObjectProperty(None)
    logpword = ObjectProperty(None)
    
    def sigin(self):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        try:
            c.execute("SELECT * FROM user WHERE phone=:phone", {'phone': self.logph.text})
            logincheck = c.fetchone()
            if self.logpword.text == logincheck[3]:
                self.manager.current = "das"
            else:
                print('wrong password')
        except TypeError:
            print('wrong user')

        conn.commit()
        conn.close()

    def sigu(self):
        self.manager.current = "sup"

    def fpword(self):
        self.manager.current = "fpword"


class dashboard(Screen):
    screen_man = ObjectProperty(None)

    def logot(self):
        self.manager.current = "log"

    def chgbook(self):
        self.manager.current = "bok"

class signu(Screen):

    nam = ObjectProperty(None)
    phone = ObjectProperty(None)
    email = ObjectProperty(None)
    pword = ObjectProperty(None)
    repword = ObjectProperty(None)
    
    def cansig(self):
        self.manager.current = "log"

    def creacct(self):
        if self.nam.text != "" and self.phone.text and self.email.text and self.pword.text and self.repword.text and self.pword.text == self.repword.text:
            detail = [self.nam.text, self.phone.text, self.email.text, self.pword.text, self.repword.text]
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute("INSERT INTO user VALUES(?,?,?,?,?)", detail )
            conn.commit()
            conn.close()
            self.manager.current = "log"

        else:
            print('wrong input')
        # to create a table 'user' in the database 'users'
        #c.execute("CREATE TABLE user(name text, phone text, email text, password text, conpassword text)")
        

class forpword(Screen):
    
    def canfpwor(self):
        self.manager.current = "log"

class book(Screen):

    problemtext = ObjectProperty(None)
    book_page = ObjectProperty(None)
    problems = ObjectProperty(None)
    date = ObjectProperty(None)
    time = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(book, self).__init__(**kwargs)

        for i in range(200):
            item = OneLineListItem(text ='hello' + str(i))
            self.problems.add_widget(item)
            
    def check(self):
        print("hello")
    
    def goback(self):
        self.manager.current = "das"

    def retur(self):
        self.manager.current = "das"

    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>
        '''
        self.date.text = (str(date))
                
    def show_time_pick(self):
        min_date = datetime.strptime("2020:02:15", '%Y:%m:%d').date()
        date_dialog = MDDatePicker(callback = self.get_date, min_date = min_date)
        date_dialog.open()

    def listselect(self):
        pass

class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''right container'''
    



class MainApp(MDApp):
    def build(self):
        Builder.load_file("login.kv")
        sm = ScreenManager()
        sm.add_widget(login(name="log"))
        sm.add_widget(dashboard(name="das"))
        sm.add_widget(signu(name="sup"))
        sm.add_widget(forpword(name="fpword"))
        sm.add_widget(book(name="bok"))
        self.theme_cls.primary_palette = "Cyan"
        return sm

MainApp().run()
