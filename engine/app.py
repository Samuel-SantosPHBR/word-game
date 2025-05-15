from .window_manager import WindowManager
from .input_manager import InputManager

class App:
    _instance = None

    def __init__(self):
        self.input = InputManager()
        self.window = WindowManager()
        self.on_update = None
        self.on_start = None
        self.elements = []
        self.is_running = True

    def on_start_game(self, lambda_funtion):
        self.on_start = lambda_funtion

    def on_update_game(self, lambda_funtion):
        self.on_update = lambda_funtion

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __render(self):
        self.window.render()

    def __handle_events(self):
        return self.window.handle_events()
    
    def get_input_manager(self):
        return self.input

    def execute(self):
        if self.on_start is not None:
            self.on_start()  
        
        while self.is_running:
            if self.on_update is not None:
                self.on_update()

            
            self.is_running = self.__handle_events()
            self.input.update()
            
            self.__render()