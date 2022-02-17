import cv2 as cv
import pyautogui 
import numpy as np
from win32 import win32gui
import time

# Roblox HWND
roblox_found = win32gui.FindWindow(0, "Roblox")

tree_img = cv.imread("./tree.png")

list_of_sweet_spots = []

pixel_count = 0

def laneAssist(img):
    # add threshold
    #img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

    #cv.imshow("gray", img)
    #cv.waitKey(0)
    #cv.destroyAllWindows()

    retur, img = cv.threshold(img, 150, 255, cv.THRESH_BINARY)
    
    cv.imshow("thresh", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    # custom line detection
    # we have to split loops in horizontally and vertically 
    for pixel in range(0, len(img)):
        print(img[pixel][0])

    return img

def LookForSweetSpot(img, color, colorDiff):
    for i in np.array(img):
        pixel_count += 1
        
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
if True:
    while mainloop:
        time.sleep(0.5)

        print('Roblox found')
        
        # Roblox Window Size for screen capture
        #roblox_RECT = win32gui.GetWindowRect(roblox_found)
        
        #cut_region = roblox_RECT
        screenie = pyautogui.screenshot()
        screenie = np.array(screenie)
        screenie = cv.cvtColor(screenie, cv.COLOR_BGR2RGB)

        #LookForSweetSpot(screenie, [255,0,0], 10)
        screeie = laneAssist(screenie)

        cv.imshow("Screenshot", screenie)
        cv.waitKey(0)
        cv.destroyAllWindows()
else:
    print('Roblox not found. Please open roblox then the software.')
