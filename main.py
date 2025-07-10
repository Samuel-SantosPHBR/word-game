from engine.app import App
from engine.InputKeys import InputKeys

app = App()

images_data = [
    {"path": "images/testRender.png", "x": 100, "y": 100},
]

def logar_a():
    if app.input.is_key_down(InputKeys.D):
        images_data[0]["x"] += 3
    if app.input.is_key_down(InputKeys.A):
        images_data[0]["x"] -= 2

app.on_update_game(logar_a)


app.execute(images_data)