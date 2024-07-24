from re import S
from kivy.properties import StringProperty
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
from kivymd.uix.textfield import MDTextField
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from database import LoginDetails
from kivy.uix.button import Button

class FAQItemContent(BoxLayout):
    answer = StringProperty("")

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

    def on_start(self):
        faq_list = self.root.ids.faq_screen.ids.faq_list

        faqs = [
            {"question": "How do I upload?", "answer": "How do I upload my Syllabus? You can upload your syllabus by choosing the File Upload option from the menu."},
            {"question": "Reminders?", "answer": "How do I set Reminders? Reminders can be set manually in the Reminders tab."},
            {"question": "Useability?", "answer": "Can I use this for more than schoolwork? This application was designed to work with students."},
            {"question": "Changed due date?", "answer": "What if a due date changed? You can manually add and edit new assignments."}
        ]

        for faq in faqs:
            content = FAQItemContent(answer=faq["answer"])
            faq_list.add_widget(
                MDExpansionPanel(
                    icon="help-circle-outline",
                    content=content,
                    panel_cls=MDExpansionPanelOneLine(
                        text=faq["question"],
                         font_style='Subtitle1',
                    ),
                    height=dp(48) 
                )
            )
    
        
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        
        date_dialog.open()

    def show_help_popup(self):
        popup_content = BoxLayout(orientation='vertical', padding=10, spacing=5)
        
        # Name field
        self.name_field = MDTextField(hint_text="First and Last Name", size_hint_y=None, height=dp(40))
        popup_content.add_widget(self.name_field)

        # Message field
        self.message_field = MDTextField(hint_text="Your Message", size_hint_y=None, height=dp(100), multiline=True)
        popup_content.add_widget(self.message_field)

        # Submit button
        submit_button = Button(text="Send", size_hint_y=None, height=dp(50))
        submit_button.bind(on_release=self.send_email)
        popup_content.add_widget(submit_button)
        
        # Close button
        close_button = Button(text="Close", size_hint_y=None, height=dp(50))
        close_button.bind(on_release=lambda x: self.help_popup.dismiss())
        popup_content.add_widget(close_button)


        self.help_popup = Popup(title="Contact Us", content=popup_content, size_hint=(None, None), size=(300, 300))
        self.help_popup.open()

    def send_email(self, instance):
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        # Get user input
        name = self.name_field.text
        message = self.message_field.text

        # Email settings
        sender_email = "group12project3444@gmail.com"
        receiver_email = "group12project3444@gmail.com"
        app_password = "sdgm mirm vypq bvsg"
        subject = "Help Request from {}".format(name)
        body = "Name: {}\n\nMessage:\n{}".format(name, message)

        # Create email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send email
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender_email, app_password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
                self.show_message_popup("Success", "Your message has been sent!")
        except Exception as e:
            self.show_message_popup("Error", str(e))

        self.help_popup.dismiss()

    def show_message_popup(self, title, message):
        popup = Popup(title=title, content=MDLabel(text=message, halign='center'), size_hint=(None, None), size=(300, 200))
        popup.open()

     
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