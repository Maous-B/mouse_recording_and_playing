import keyboard
import ctypes
import pyautogui
import os
import win32api, win32con
import time

def main():
    
    print("Hold R to record mouse movements and P to play the mouse movement")
    
    with open("position.txt", "w") as file_writing:
        with open("position.txt", "r") as file_reading:
            while True:
                if keyboard.is_pressed('r') or keyboard.is_pressed('R'):
                    x_pos, y_pos = pyautogui.position()
                    position = str(x_pos) + "," + str(y_pos)
                    file_writing.writelines(position + '\n')
                    file_writing.flush()
                if keyboard.is_pressed('p') or keyboard.is_pressed('P'):
                    for line in file_reading:
                        currentline = line.split(",")
                        x_coords = int(currentline[0])
                        y_coords = int(currentline[1])
                        #print("x : " + x_coords + " y : " + y_coords)
                        x_res = win32api.GetSystemMetrics(0)
                        y_res = win32api.GetSystemMetrics(1)
                        nx = int(x_coords*65535/x_res)
                        ny = int(y_coords*65535/y_res)
                        win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,nx,ny)
                        
main()