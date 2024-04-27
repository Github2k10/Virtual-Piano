import cv2
import mediapipe as mp
import pyglet
import time

# Constants
wCam, hCam = 640, 480
w, h = 40, 150
playlist = ['./tones/tone1.mp3', './tones/tone2.mp3', './tones/tone3.mp3', './tones/tone4.mp3', './tones/tone5.mp3', './tones/tone6.mp3', './tones/tone7.mp3']
handpoints = [(i * 50 + 80, 130) for i in range(7)]
ractpoints = [(i * 50 + 60, 0) for i in range(7)]

# Initialize camera
cap = cv2.VideoCapture(0) 
cap.set(3, wCam)
cap.set(4, hCam)

# Initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# Load all songs
songs = [pyglet.media.load(song) for song in playlist]


def findHands(img, draw=True):
    """Detects hands in the image and draws landmarks if draw parameter is set to True."""
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks and draw:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    return img, results


def findPositions(img, results, draw=True):
    """Finds the positions of landmarks on detected hands."""
    lmList = []

    if results.multi_hand_landmarks:
        for myHand in results.multi_hand_landmarks:
            xList = []
            yList = []
            lList = []

            for id, lm in enumerate(myHand.landmark):
                hi, wi, c = img.shape
                cx, cy = int(lm.x * wi), int(lm.y * hi)
                xList.append(cx)
                yList.append(cy)
                lList.append([id, cx, cy])

                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)
            lmList.append(lList)

            if draw:
                cv2.rectangle(img, (xmin - 20, ymin - 20), (xmax + 20, ymax + 20),
                              (0, 255, 0), 2)

    return img, lmList


def playMusic(p1, p2):
    """Plays music based on the hand position on the virtual piano."""
    # Check if hand position is within the range of any piano key, and play the corresponding song
    # based on the position
    if (handpoints[0][0] - 7 < p1 < handpoints[0][0] + 7) and (
            handpoints[0][1] - 7 < p2 < handpoints[0][1] + 7):
        cv2.rectangle(img, ractpoints[0], (ractpoints[0][0] + w, ractpoints[0][1] + h), (255, 0, 255), -1)
        song = pyglet.media.load(playlist[0])
        song.play()
        time.sleep(0.1)
    elif (handpoints[1][0] - 7 < p1 < handpoints[1][0] + 7) and (
            handpoints[1][1] - 7 < p2 < handpoints[1][1] + 7):
        cv2.rectangle(img, ractpoints[1], (ractpoints[1][0] + w, ractpoints[1][1] + h), (255, 0, 255), -1)
        song = pyglet.media.load(playlist[1])
        song.play()
        time.sleep(0.1)
    elif (handpoints[2][0] - 7 < p1 < handpoints[2][0] + 7) and (
            handpoints[2][1] - 7 < p2 < handpoints[2][1] + 7):
        cv2.rectangle(img, ractpoints[2], (ractpoints[2][0] + w, ractpoints[2][1] + h), (255, 0, 255), -1)
        song = pyglet.media.load(playlist[2])
        song.play()
        time.sleep(0.1)
    elif (handpoints[3][0] - 7 < p1 < handpoints[3][0] + 7) and (
            handpoints[3][1] - 7 < p2 < handpoints[3][1] + 7):
        cv2.rectangle(img, ractpoints[3], (ractpoints[3][0] + w, ractpoints[3][1] + h), (255, 0, 255), -1)
        song = pyglet.media.load(playlist[3])
        song.play()
        time.sleep(0.1)
    elif (handpoints[4][0] - 7 < p1 < handpoints[4][0] + 7) and (
            handpoints[4][1] - 7 < p2 < handpoints[4][1] + 7):
        cv2.rectangle(img, ractpoints[4], (ractpoints[4][0] + w, ractpoints[4][1] + h), (255, 0, 255), -1)
        song = pyglet.media.load(playlist[4])
        song.play()
        time.sleep(0.1)
    elif (handpoints[5][0] - 7 < p1 < handpoints[5][0] + 7) and (
            handpoints[5][1] - 7 < p2 < handpoints[5][1] + 7):
        cv2.rectangle(img, ractpoints[5], (ractpoints[5][0] + w, ractpoints[5][1] + h), (255, 0, 255), -1)
        song = pyglet.media.load(playlist[5])
        song.play()
        time.sleep(0.1)
    elif (handpoints[6][0] - 7 < p1 < handpoints[6][0] + 7) and (
            handpoints[6][1] - 7 < p2 < handpoints[6][1] + 7):
        cv2.rectangle(img, ractpoints[6], (ractpoints[6][0] + w, ractpoints[6][1] + h), (255, 0, 255), -1)
        song = pyglet.media.load(playlist[6])
        song.play()
        time.sleep(0.1)


while True:
    success, img = cap.read()
    img, results = findHands(img)
    img, lmlist = findPositions(img, results)

    # Draw rectangles representing piano keys on the image
    for i, (rect, point) in enumerate(zip(ractpoints, handpoints)):
        cv2.rectangle(img, rect, (rect[0] + w, rect[1] + h), (255, 0, 255), 2)
        cv2.circle(img, point, 7, (255, 0, 255), cv2.FILLED)

    # Check if hand landmarks are detected and play music accordingly
    if len(lmlist) >= 1:
        p1, p2 = lmlist[0][8][1:]
        p3, p4 = lmlist[0][12][1:]

        playMusic(p1, p2)
        playMusic(p3, p4)

    if len(lmlist) >= 2:
        p1, p2 = lmlist[1][8][1:]
        p3, p4 = lmlist[1][12][1:]

        playMusic(p1, p2)
        playMusic(p3, p4)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
