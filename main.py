from re import S
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivymd.theming import ThemeManager
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.clock import Clock
from kivymd.uix.pickers import MDDatePicker
from database import LoginDetails
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.popup import Popup
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog

class LoginScreen(Screen):
    pass

class SignupScreen(Screen):
    pass

class CalendarScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class SyllabusScreen(Screen):
    pass

class ReminderScreen(Screen):
    pass
class ProfileScreen(Screen):
    pass
class FileScreen(Screen):
    pass
class ChangePassword(Screen):
    pass
class ForgotPassword(Screen):
    pass
class FaqScreen(Screen):
    pass
class ChangeName(Screen):
    pass
class ChangeEmail(Screen):
    pass
class ChangeUsername(Screen):
    pass

class userDetails():
    def __init__(self):
        self.name = "name"
        self.username = "username"
        self.email = "email"
    
    def changeName(self, a):
        self.name = a
        print("setter name called")
        print(self.name)
    
    def changeUsername(self, username):
        self.username = username
        
    def changeEmail(self, email):
        self.email = email
        

class MainApp(MDApp):
    dialog = None
    
    x = userDetails()
    
    def login(self,x, email): 
        x.changeName("placeholder")
        x.username = "placeholder"
        x.email = email
    
    
    Window.size = [300,600]
    theme_cls = ThemeManager()
    
    def build(self):
        self.GUI = Builder.load_file("main.kv")
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.primary_hue = '200'
        self.loginDetails = LoginDetails()
        return self.GUI
    def change_screen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name

    
        
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        
        date_dialog.open()

    #Help popup in FAQ
    def show_help_popup(self):
        popup_content = BoxLayout(orientation='vertical', padding=10)
        popup_content.add_widget(MDLabel(text="Contact us : email@business.com"))
        close_button = MDRaisedButton(text="Close", size_hint_y=None, height=40)
        close_button.bind(on_release=lambda x: help_popup.dismiss())
        popup_content.add_widget(close_button)

        help_popup = Popup(title="Help", content=popup_content, size_hint=(None, None), size=(300, 200))
        help_popup.open()
     
    def confirm_registration_dialog(self):
        if not self.dialog:
            self.dialog= MDDialog(
                title="Notice:",
                type="custom",
                text="There will be a temporary password sent to your email for your first login. Please change it once you login.",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        text_color=self.theme_cls.primary_color,
                    )
                ],
            )
        self.dialog.open()
    def already_account_dialog(self):
        if not self.dialog:
            self.dialog= MDDialog(
                title="Notice:",
                type="custom",
                text="There is already an account associated with this email address. Login or select forgot password.",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        text_color=self.theme_cls.primary_color,
                    )
                ],
            )
        self.dialog.open()
    def no_validation_dialog(self):
        if not self.dialog:
            self.dialog= MDDialog(
                title="Notice",
                type="custom",
                text="One of the fields is incorrect. Please retry or use any potential features for help.",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        text_color=self.theme_cls.primary_color,
                    )
                ],
            )
        self.dialog.open()


if __name__ == '__main__':
    MainApp().run()