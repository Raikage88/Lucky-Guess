from kivy.app import App
from kivy.graphics import Color, Line
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput

Window.size = (400, 600)

class Opening(GridLayout):
    def __init__(self, **kwargs):
        super(Opening, self).__init__(**kwargs)

        self.width = Window.size[0]
        self.height = Window.size[1]
        self.add_gradient()

    def add_gradient(self):
        alpha_channel_rate = 0
        increase_rate = 1 / self.width

        for sep in range(self.width):
            self.canvas.add(Color(rgba=(100/255, 0, 190/255, alpha_channel_rate)))
            self.canvas.add(Line(points=[sep, 0, sep, self.height], width=1))
            alpha_channel_rate += increase_rate

        # Landing Page
        self.cols = 1
        self.padding = 100
        self.spacing = 30
        self.title = Label(
            text="Lvcky Guesses",
            font_size=50,
            color=(0, 0, 0.8, 1)
        )
        self.add_widget(self.title)

        # Adding Landing Page Buttons
        self.start = Button(
            text="START",
            font_size=15
        )
        self.start.bind(on_press=self.displayStart)
        self.add_widget(self.start)

        self.instructions = Button(
            text="INSTRUCTIONS",
            font_size=15
        )
        self.add_widget(self.instructions)

        self.end = Button(
            text="END",
            font_size=15
        )
        self.add_widget(self.end)

    def displayStart(self, instance):
        self.land = Label(
            text="Lvcky Guesses",
            font_size=40
        )
        self.add_widget(self.land)

        # Adding Quest
        self.quest = Label(
            text="Can you guess six(6) lucky numbers",
            font_size=15
        )
        self.add_widget(self.quest)

class Entry(GridLayout):
    def __init__(self, **kwargs):
        super(Entry, self).__init__(**kwargs)

        self.cols = 1
        self.padding = 100
        self.spacing = 30
        self.title = Label(
            text="Lvcky Guesses",
            font_size=50,
            color=(0, 0, 0.8, 1)
        )
        self.add_widget(self.title)

        self.quest = Label(
            text="Can you guess the six(6) numbers?",
            font_size=15,
        )
        self.add_widget(self.quest)

        self.range = Label(
            text="Enter your guesses (1-99):",
            font_size=15,
        )
        self.add_widget(self.range)

        self.player = TextInput(
            text="Player Guess: ",
            multiline=False
        )
        self.add_widget(self.player)


class Lucky(App):
    def build(self):
        return Entry()

if __name__ == '__main__':
    Lucky().run()

