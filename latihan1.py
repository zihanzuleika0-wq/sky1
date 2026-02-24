from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
class MyApp(App)
		def build(self)
			    layout = BoxLayout(orientation= 'horizontal')
			    layout.add_widget(Label(text="Aplikasi Kivy"))
			    layout.add_widget(Button(text="Klik Saya"))
			    return layout
MyApp().run()