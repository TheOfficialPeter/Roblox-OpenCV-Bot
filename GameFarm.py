import cv2 as cv
import pyautogui 
import numpy as np
from win32 import win32gui
import time

# Roblox HWND
roblox_found = win32gui.FindWindow(0, "Roblox")

tree_img = cv.imread("./tree.png")

# init orb
orb = cv.ORB_create()

orb.create()

def Canny(img):
    new_img = cv.Canny(img, 0, 200)
    return new_img

mainloop = True
if roblox_found:
    while mainloop:
        time.sleep(0.5)

        print('Roblox found')
        
        # Roblox Window Size for screen capture
        roblox_RECT = win32gui.GetWindowRect(roblox_found)

        screenie = pyautogui.screenshot(region=(roblox_RECT))
        screenie = np.array(screenie)
        screenie = cv.cvtColor(screenie, cv.COLOR_BGR2RGB)

        keyp1, desc1 = orb.detectAndCompute(screenie, None)
        keyp2, desc2 = orb.detectAndCompute(tree_img, None)

        bf = cv.BFMatcher(cv.NORM_HAMMING)
        
        # get features that match in both images
        matches = bf.match(desc1, desc2)

        # sort them
        matches = sorted(matches, key= lambda x:x.distance)

        # draw all matching features
        screenie = cv.drawMatches(screenie, keyp1, tree_img, keyp2, matches[:1000], None)

        cv.imshow("Screenshot", screenie)
        cv.waitKey(0)
        cv.destroyAllWindows()
else:
    print('Roblox not found. Please open roblox then the software.')
