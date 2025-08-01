from pynput import keyboard


def on_press(key):
    if key == (keyboard.Key.ctrl and keyboard.Key.caps_lock):
        print("Testing........")


def on_release(key):
    #print('combination released')
    if key == keyboard.Key.esc:
        # Stop listener
        return False


with keyboard.Listener(
        on_press=on_press, on_release=on_release) as listener:
    listener.join()
