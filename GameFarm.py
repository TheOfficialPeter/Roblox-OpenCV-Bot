import cv2 as cv
import pyautogui 
import numpy as np
from win32 import win32gui
import time

# Roblox HWND
roblox_found = win32gui.FindWindow(0, "Roblox")

tree_img = cv.imread("./tree.png")

def Canny(img):
    new_img = cv.Canny(img, 0, 200)
    return new_img

list_of_sweet_spots = []

pixel_count = 0
def LookForSweetSpot(img, color, colorDiff):
    for i in np.array(img):
        pixel_count += 1
        if i[0] < color[0]+colorDiff and i[0] > color[0]-colorDiff and i[1] < color[1]+colorDiff and i[1] > color[1]-colorDiff and i[2] < color[2]+colorDiff and i[2] > color[2]-colorDiff:
            # color is inside interval
            print("Color is inside interval")
            list_of_sweet_spots.append(pixel_count)
    
def CutSweetSpot(img):
    global cut_region
    cut_region = list_of_sweet_spots[0]

def GetSweetSpotShape(img, img_shape):
    pass

# predict where image should be
def GetSweetSpotPred(img1, img2):
    img_diff = 0

cut_region = (0,0,0,0)
mainloop = True
if roblox_found:
    while mainloop:
        time.sleep(0.5)

        print('Roblox found')
        
        # Roblox Window Size for screen capture
        roblox_RECT = win32gui.GetWindowRect(roblox_found)
        
        cut_region = roblox_RECT
        screenie = pyautogui.screenshot(region=(cut_region))
        screenie = np.array(screenie)
        screenie = cv.cvtColor(screenie, cv.COLOR_BGR2RGB)

        LookForSweetSpot(screenie, [255,0,0], 10)

        cv.imshow("Screenshot", screenie)
        cv.waitKey(0)
        cv.destroyAllWindows()
else:
    print('Roblox not found. Please open roblox then the software.')
