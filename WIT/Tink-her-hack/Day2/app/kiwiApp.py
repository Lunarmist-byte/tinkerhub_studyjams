from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import StringProperty
import time

class ClockApp(App):
    time_text = StringProperty("00:00:00")

    def build(self):
        label = Label(text=self.time_text, font_size="50sp")
        self.bind(time_text=label.setter("text"))
        Clock.schedule_interval(self.update_time, 1)
        return label

    def update_time(self, dt):
        self.time_text = time.strftime("%H:%M:%S")

if __name__ == "__main__":
    ClockApp().run()
