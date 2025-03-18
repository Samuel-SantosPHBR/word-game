from window_manager import WindowManager

class App:
    _instance = None

    def __init__(self):
        self.input = {}
        self.window = WindowManager()
        self.elements = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __render(self):
        self.window.run()

    def execute(self):
        self.__render()