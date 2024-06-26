from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.popup import Popup

class FAQItem(BoxLayout):
    def __init__(self, question, answer, **kwargs):
        super(FAQItem, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Initialize button widget
        self.question_label = Button(
            text=question,
            size_hint_y=None,
            height=40,
            background_normal='',
            background_color=(0.2, 0.6, 0.9, 1),
            color=(1, 1, 1, 1)
        )
        self.question_label.bind(on_press=self.toggle_answer)
        #FAQ Answer template
        self.answer_label = Label(
            text=answer,
            size_hint_y=None,
            height=0,
            opacity=0,
            text_size=(Window.width - 50, None),
            color=(0, 0, 0, 1)
        )
        
        self.add_widget(self.question_label)
        self.add_widget(self.answer_label)
    #Toggle answer template
    def toggle_answer(self, instance):
        if self.answer_label.height == 0:
            self.answer_label.height = self.answer_label.texture_size[1] + 20 # Adjust height based on device later
            self.answer_label.opacity = 1
        else:
            self.answer_label.height = 0
            self.answer_label.opacity = 0

class FAQApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')
        with root.canvas.before:
            # Set background color
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=Window.size)
            root.bind(size=self._update_rect, pos=self._update_rect)
        
        # Add a top bar with a back button on the left and a hamburger button on the right
        top_bar = BoxLayout(size_hint_y=None, height=50, orientation='horizontal')
        
        # Back button
        back_button = Button(text='<', size_hint_x=None, width=50, background_normal='', background_color=(0.2, 0.6, 0.9, 1), color=(1, 1, 1, 1))
        back_button.bind(on_press=self.go_back)
        top_bar.add_widget(back_button)
        
        # FAQ Header label
        header_label = Label(text='FAQ', size_hint_x=1, halign='center', valign='middle', color=(0, 0, 0, 1))
        header_label.bind(size=self._update_header_label)
        top_bar.add_widget(header_label)
        
        # Hamburger button
        hamburger_button = Button(text='=', size_hint_x=None, width=50, background_normal='', background_color=(0.2, 0.6, 0.9, 1), color=(1, 1, 1, 1))
        hamburger_button.bind(on_press=self.show_menu)
        top_bar.add_widget(hamburger_button)
        
        root.add_widget(top_bar)
        
        # Layout for FAQ questions and buttons
        main_layout = BoxLayout(orientation='vertical', size_hint=(1, 1))
        scroll_view = ScrollView(size_hint=(1, 1))
        faq_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        faq_layout.bind(minimum_height=faq_layout.setter('height'))
        
        faqs = [
            ("How do I upload my Syllabus?", "You can upload your syllabus by choosing the File Upload option from the menu."),
            ("How do I set Reminders?", "Reminders should automatically be imported and exported to your device's calendar."),
            ("Can I use this for more than schoolwork?", "This application was designed to work with students."),
        ]
        
        for question, answer in faqs:
            faq_item = FAQItem(question, answer)
            faq_layout.add_widget(faq_item)
        
        scroll_view.add_widget(faq_layout)
        main_layout.add_widget(scroll_view)

        # Add Contact button at the bottom
        help_button = Button(text='Still Need Help?', size_hint_y=None, height=50, background_normal='', background_color=(0.2, 0.6, 0.9, 1), color=(1, 1, 1, 1))
        help_button.bind(on_press=self.connect_with_help)
        main_layout.add_widget(help_button)

        root.add_widget(main_layout)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def _update_header_label(self, instance, value):
        instance.text_size = (instance.width, None)
        instance.texture_update()
        instance.height = instance.texture_size[1]

    def show_menu(self, instance):
        # Create the popup menu
        menu_layout = BoxLayout(orientation='vertical')
        close_button = Button(text='Close', size_hint_y=None, height=40, on_press=lambda x: self.popup.dismiss())
        menu_layout.add_widget(close_button)
        # Add menu items and functionality
        menu_layout.add_widget(Button(text='Home'))
        menu_layout.add_widget(Button(text='Syllabus'))
        menu_layout.add_widget(Button(text='Reminders'))
        menu_layout.add_widget(Button(text='Calendar'))
        menu_layout.add_widget(Button(text='Profile'))

        self.popup = Popup(title='Menu', content=menu_layout, size_hint=(None, None), size=(200, 200))
        self.popup.open()
    #Contact Us button functionality
    def connect_with_help(self, instance):
        popup_content = BoxLayout(orientation='vertical', padding=10)
        popup_content.add_widget(Label(text="Contact us : email@business.com"))
        close_button = Button(text="Close", size_hint_y=None, height=40)
        close_button.bind(on_press=lambda x: help_popup.dismiss())
        popup_content.add_widget(close_button)
        
        help_popup = Popup(title="Help", content=popup_content, size_hint=(None, None), size=(300, 200))
        help_popup.open()

    def go_back(self, instance):
        # Need to Add button functionality
        pass

if __name__ == '__main__':
    FAQApp().run()
