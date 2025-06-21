
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
import random

Window.clearcolor = (0, 0, 0, 1)
Window.size = (360, 640)

class FallingManGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.man = Label(text="لع", font_size='24sp', pos=(180, 600))
        self.add_widget(self.man)
        self.score = 0
        self.speed = 1
        self.max_score = 20
        self.game_over = False
        self.points = []
        self.spawn_points()
        self.score_label = Label(text="النقاط: 0", pos=(10, 600), font_size='18sp')
        self.add_widget(self.score_label)
        Clock.schedule_interval(self.update, 1/30)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        if self._keyboard.widget:
            self._keyboard.widget.layout = 'numeric'
        self._keyboard.bind(on_key_down=self.on_key_down)

    def spawn_points(self):
        for _ in range(10):
            x = random.randint(0, Window.width - 20)
            y = random.randint(300, 600)
            label = Label(text="*", pos=(x, y), font_size='20sp')
            self.add_widget(label)
            self.points.append(label)

    def on_key_down(self, keyboard, keycode, text, modifiers):
        if self.game_over:
            return
        if keycode[1] == 'a':
            self.man.x -= 20
        elif keycode[1] == 'd':
            self.man.x += 20

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self.on_key_down)
        self._keyboard = None

    def update(self, dt):
        if self.game_over:
            return

        self.man.y -= self.speed
        self.speed += 0.001
        for point in self.points:
            point.y -= self.speed * 0.5
            if point.y < 0:
                point.y = random.randint(300, 600)
                point.x = random.randint(0, Window.width - 20)

        for point in self.points:
            if abs(self.man.center_x - point.center_x) < 20 and abs(self.man.center_y - point.center_y) < 20:
                self.score += 1
                self.score_label.text = f"النقاط: {self.score}"
                point.y = random.randint(300, 600)
                point.x = random.randint(0, Window.width - 20)

        if self.score >= self.max_score:
            self.game_over = True
            win_label = Label(text="أنت رابح!", font_size='24sp', center=(Window.width//2, Window.height//2))
            self.add_widget(win_label)
        elif self.man.y < 0:
            self.game_over = True
            lose_label = Label(text="أنت ميت!", font_size='24sp', center=(Window.width//2, Window.height//2))
            self.add_widget(lose_label)

class GameApp(App):
    def build(self):
        return FallingManGame()

if __name__ == '__main__':
    GameApp().run()
