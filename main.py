from engine.app import App
from engine.InputKeys import InputKeys

app = App()

def logar_a():
    print(app.input.is_key_down(InputKeys.A))

app.on_update_game(logar_a)


app.execute()