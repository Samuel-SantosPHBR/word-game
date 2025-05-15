from window_manager import WindowManager

class App:
    _instance = None

    def __init__(self):
        self.input = {}
        self.window = WindowManager()
        self.on_update = None
        self.on_start = None
        self.elements = []

    def on_start_game(self, lambda_funtion):
        self.on_start = lambda_funtion

    def on_update_game(self, lambda_funtion):
        self.on_update = lambda_funtion

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __render(self):
        self.window.run()

    def execute(self):
        if self.on_start not is None:
            self.on_start()
        
        while True:
            if self.on_update not is None:
                self.on_update()
            #self.__render() Falar com Luiz