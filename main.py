from kivymd.app import MDApp
from kivy.lang import Builder
from kivy_garden.mapview import MapView

class MyApp(MDApp):
	def build(self):
		self.screen = Builder.load_file("main.kv")
		return self.screen

MyApp().run()
