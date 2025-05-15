from engine.app import App
from engine.InputKeys import InputKeys

app = App()

def logar_a():
    if app.input.is_key_down(InputKeys.A):
        print(1)

app.on_update_game(logar_a)


app.execute()