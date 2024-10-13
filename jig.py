import pyautogui
import time

pyautogui.FAILSAFE = False

def activity_simulator(interval=60):
    """
    Alternates between moving the mouse and pressing F15 key every 'interval' seconds (default: 60 seconds).
    """
    print("Activity simulator started. Press Ctrl+C to stop.")
    try:
        action_counter = 0
        while True:
            if action_counter % 2 == 0:
                # Move mouse
                pyautogui.moveRel(5, 0)
                time.sleep(0.1)  # Short delay between movements
                pyautogui.moveRel(-5, 0)
                print(f"Mouse moved. Waiting for {interval} seconds...")
            else:
                # Press F15 key
                pyautogui.press('f15')
                print(f"F15 key pressed. Waiting for {interval} seconds...")
            
            action_counter += 1
            time.sleep(interval)
            
    except KeyboardInterrupt:
        print("Activity simulator stopped.")

if __name__ == "__main__":
    activity_simulator()
