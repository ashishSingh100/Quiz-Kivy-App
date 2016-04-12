from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.screenmanager import FadeTransition
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
import webbrowser
from kivy.clock import Clock
class SecondScreen(Screen):
	pass
	
class AnotherScreen(Screen):
	pass
class Score1(Screen):
	count_r=NumericProperty(0)
	I=3
	def do_score(self):
		self.count_r=self.count_r+10
		self.l1.text='YOUR SCORE IS '+str(self.count_r)
		self.I=self.I+1

class ThirdScreen(Screen):
	pass

class FourthScreen(Screen):
	pass
class FifthScreen(Screen):
	pass

class MainScreen(Screen):
	
	def go_there(self):
		webbrowser.open("http://winteriscoming.net")



class WinScreen(Screen):
	pass
	
		


class ScreenManagement(ScreenManager):
	pass


presentation=Builder.load_file('simple.kv')

class SimpleKivy(App):
	def build(self):
		self.screens = {}
		self.screens["wordcomp"] = Score1(app=self)
		self.screens["score"] = WinScreen(app=self)
		self.screens["wordcomp"].bind(count_r=self.screens["score"].setter('score'))
		return presentation

SimpleKivy().run()