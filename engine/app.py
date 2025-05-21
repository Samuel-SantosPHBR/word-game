import pygame
from .window_manager import WindowManager
from .input_manager import InputManager

class App:
    _instance = None

    def __init__(self):
        self.input = InputManager()
        self.window = WindowManager(self.input)
        self.on_update = None
        self.on_start = None
        self.is_running = True

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def on_start_game(self, lambda_function):
        self.on_start = lambda_function

    def on_update_game(self, lambda_function):
        self.on_update = lambda_function

    def get_input_manager(self):
        return self.input

    def __render(self):
        self.window.render()

    def __handle_events(self):
        return self.window.handle_events()

    def execute(self):
        if self.on_start is not None:
            self.on_start()

        while self.is_running:
            events = pygame.event.get()  # <- captura uma vez
            self.input.update(events)    # <- atualiza input com os eventos
            self.is_running = self.window.handle_events(events)

            if self.on_update is not None:
                self.on_update()

            self.__render()
