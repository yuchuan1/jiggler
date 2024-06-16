import pyautogui
import time

pyautogui.FAILSAFE = False

def mouse_j(interval=1):
    """j the mouse every 'interval' seconds."""
    print("Mouse j started. Press Ctrl+C to stop.")
    try:
        while True:
            pyautogui.moveRel(5, 0)
            time.sleep(interval)
            pyautogui.moveRel(-5, 0)
            time.sleep(interval)
            pyautogui.keyDown('shift')
            pyautogui.keyUp('shift')
    except KeyboardInterrupt:
        print("Mouse j stopped.")

if __name__ == "__main__":
    mouse_j()
