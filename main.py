import kivy
kivy.require('2.0.0')
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

#plyer for android notification ecc
from plyer import notification

#kivyMD
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemableBehavior
 
KV = '''
<CustomToolbar>:
    size_hint_y: None
    height: self.theme_cls.standard_increment
    padding: "5dp"
    spacing: "12dp"

    MDLabel:
        text: "Hi-drate"
        pos_hint: {"center_y": .5}
        size_hint_x: None
        width: self.texture_size[0]
        text_size: None, None
        font_style: 'H6'

    Widget:

    MDIconButton:
        id: button_2
        icon: "dots-vertical"
        pos_hint: {"center_y": .5}
        on_release: app.settings_menu.open()

Screen:
    CustomToolbar:
        id: toolbar
        elevation: 10
        pos_hint: {"top": 1}

GridLayout:
    rows: 3
    
'''

sm = ScreenManager()

homepage_screen = Screen(name="Homepage")
sm.add_widget(homepage_screen)

about_screen = Screen(name="About")
sm.add_widget(about_screen)

settings_screen = Screen(name="Settings")
sm.add_widget(settings_screen)

class CustomToolbar(
    ThemableBehavior, RectangularElevationBehavior, MDBoxLayout
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = self.theme_cls.primary_color

class Hydrate(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.screen = Builder.load_string(KV)
        self.settings_menu = self.create_menu(
            "Settings", self.screen.ids.toolbar.ids.button_2,
        )

        sm.add_widget(self.screen)

    def create_menu(self, text, instance):
        #Change icons and give importance
        menu_items = [{"icon": "help", "text": "About"},
                        {"icon": "application-settings", "text": "Settings"}
        ]

        #tweak this for width
        menu = MDDropdownMenu(caller=instance, items=menu_items, width_mult=5)
        menu.bind(on_release=self.menu_callback)
        return menu

    def menu_callback(self, instance_menu, instance_menu_item):
        if instance_menu_item.text == "About":
            sm.current = "About"
            print(sm.current)

        if instance_menu_item.text == "Settings":
            sm.current = "Settings"
            print("settings")

    def build(self):
        return self.screen

if __name__ == '__main__':
    Hydrate().run()
