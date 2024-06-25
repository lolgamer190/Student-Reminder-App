from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivymd.theming import ThemeManager
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout

from forgot import forgotPassword

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

class MainApp(MDApp):
    Window.size = [300,600]
    theme_cls = ThemeManager()
    def build(self):
        self.GUI = Builder.load_file("main.kv")
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.primary_hue = '200'
        return self.GUI
    def change_screen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name
    def data_table(self):
        self.table = MDDataTable(
        column_data = [
            ("Assignment Name", dp(50)),
            ("Due Date", dp(50)),
            ]
    )
    def forgotP(self):
        forgotPassword()


if __name__ == '__main__':
    MainApp().run()