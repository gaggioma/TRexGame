#import browser interaction library to open page https://trex-runner.com/
#Download chrome dirver here https://chromedriver.chromium.org/downloads
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

#Keyboard interaction
from pynput.keyboard import Key, Controller

#delay generator
import time

#Image crop
import cv2

#remove file
import os

#Manage matrix
import numpy as np

def RemoveAllFilesInFolder(folderName):

    for filename in os.listdir(folderName):
        file_path = os.path.join(folderName, filename)
        try:
            os.unlink(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def loadDriver():

    s = Service("..\\chromedriver\\chromedriver.exe")

    #Load Chrome driver for Windows
    driver = webdriver.Chrome(service=s)

    #An implicit wait tells WebDriver to poll the DOM for a certain amount of time when trying to find any element (or elements) not immediately available.
    driver.implicitly_wait(10)

    driver.maximize_window() #Expand browser window

    return driver

if __name__ == "__main__":

    #Load driver
    driver = loadDriver()

    #Open game page "https://trex-runner.com/"
    driver.get("https://trex-runner.com")

    #Init keyboard controller
    keyboard = Controller()

    #Delay of 5s  and then start game
    time.sleep(1)
    keyboard.press(Key.space)
    keyboard.release(Key.space)

    #Remove all images
    RemoveAllFilesInFolder("./images")

    imgCount = 0

    while 1:
        imageName = "./images/screenshot_" + str(imgCount) + ".png"
        imageCropName = "./images/cropped_" + str(imgCount) + ".png"
        
        driver.save_screenshot(imageName)

        img = cv2.imread(imageName)
        x = 732
        y = 380
        w = 197
        h = 25
        crop_img = img[y:y+h, x:x+w] #cv2.imread("./images/cropped.png")
        cv2.imwrite(imageCropName, crop_img)

        #min color
        minColorCode = crop_img.min()
        print("Min color code image:" + str(imgCount) + ", " + str(minColorCode))

        #Avg color code
        avgColorCode = np.average(crop_img)
        print("Avg color code image:" + str(imgCount) + ", " + str(avgColorCode))

        jumpCount = 10
        if int(minColorCode) == 83:
            for jumpCout in range(jumpCount):
                keyboard.press(Key.up)
                #time.sleep(0.05) #Push time = f(avgColorCode). Little value => long jump 
                jumpTime = (1-avgColorCode/247) * 15
                print("Image:" + str(imgCount) + " sleep time: " + str(jumpTime))
                #time.sleep(jumpTime)
                keyboard.release(Key.up)

        imgCount = imgCount+ 1
