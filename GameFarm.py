import cv2 as cv
import pyautogui 
import numpy as np
from win32 import win32gui
from win32api import GetSystemMetrics
import time
import math
import keyboard

# Roblox HWND
roblox_found = win32gui.FindWindow(0, "Roblox")

tree_img = cv.imread("./tree.png")

list_of_sweet_spots = []

pixel_count = 0

def HoughLines(img):
    global final_region
    img_copy = np.copy(img)
    img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    img = cv.adaptiveThreshold(img, 200, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    
    #cv.imshow("thresh", img)
    #cv.waitKey(0)
    #cv.destroyAllWindows()
    
    img = cv.Canny(img, 100, 200)

    #cv.imshow("thresh", img)
    #cv.waitKey(0)
    #cv.destroyAllWindows()

    lines = cv.HoughLinesP(img , 1, np.pi/180, 50, 10, 5, 10)

    for i in range(0, len(lines)):
        # check if lines are 70+ degrees
        ax,ay,bx,by = lines[i][0]
    
        degrees = 40
        curr_deg = math.degrees(math.atan((ay-by)/(ax-bx)))

        if curr_deg >= degrees or curr_deg <= (-1*degrees):
            cv.line(img_copy, (ax,ay), (bx,by), (255, 0, 0), 2)

            # check distance from line to center screen
            center_screenX = (((final_region[2]+final_region[0])/2)/2)
            print("Center screen:"+str(center_screenX))
            print("line ax: " +str(ax))
            moving_distance = 200

            print("distance from left:" + str(center_screenX - ax) + " distance from right:" + str(ax- center_screenX))

            # check side of screen
            if ax < center_screenX:
                distance = center_screenX - ax
                if distance < moving_distance:
                    print("Pressing d")
                    keyboard.press("d")
                    time.sleep(.15)
                    keyboard.release("d")

            elif ax > center_screenX:
                distance = ax - center_screenX
                if distance < moving_distance:
                    print("Pressing a")
                    keyboard.press("a")
                    time.sleep(.15)
                    keyboard.release("a")

    cv.imshow("Lines", img_copy)
    cv.waitKey(100)

def laneAssist(img):
    # add threshold
    #img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

    #cv.imshow("gray", img)
    #cv.waitKey(0)
    #cv.destroyAllWindows()

    retur, img = cv.threshold(img, 150, 255, cv.THRESH_BINARY)
    
    #cv.imshow("thresh", img)
    #cv.waitKey(0)
    #cv.destroyAllWindows()

    # custom line detection
    # we have to split loops in horizontally and vertically 
    for py in range(0, 1):
        for px in range(0, GetSystemMetrics(0)):
            print(img[px, py])

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

def objectDetection(img):
    pass

cut_region = (0,0,0,0)
mainloop = True
if roblox_found:
    while mainloop:
        time.sleep(0.5)

        # Roblox Window Size for screen capture
        roblox_RECT = win32gui.GetWindowRect(roblox_found)
        
        cut_region = roblox_RECT
        final_region = (cut_region[0]+200, cut_region[1]+210, cut_region[2]-570, cut_region[3]-600)
        screenie = pyautogui.screenshot(region=(final_region))
        screenie = np.array(screenie)
        screenie = cv.cvtColor(screenie, cv.COLOR_BGR2RGB)

        #LookForSweetSpot(screenie, [255,0,0], 10)
        
        HoughLines(screenie)

else:
    print('Roblox not found. Please open roblox then the software.')
