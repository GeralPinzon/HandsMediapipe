import math
import mediapipe as mp
import cv2

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

with mp_hands.Hands( 
   static_image_mode = True,
   max_num_hands=1,
   min_detection_confidence=0.5 ) as hands:

   image = cv2.imread("tres.jpeg")
   height, width, _ = image.shape
   image = cv2.flip(image, 1)

   image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
   
   results = hands.process(image_rgb) 
   print(results.multi_handedness)
   
   if results.multi_hand_landmarks:
      for handLandmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, handLandmarks, mp_hands.HAND_CONNECTIONS)
            thumbIsOpen = False
            indexIsOpen = False
            middelIsOpen = False
            ringIsOpen = False
            pinkyIsOpen = False
         
            pseudoFixKeyPoint = handLandmarks.landmark[2].x
            if handLandmarks.landmark[3].x < pseudoFixKeyPoint and handLandmarks.landmark[4].x < pseudoFixKeyPoint:
               thumbIsOpen = True

            pseudoFixKeyPoint = handLandmarks.landmark[6].y
            if handLandmarks.landmark[7].y < pseudoFixKeyPoint and handLandmarks.landmark[8].y < pseudoFixKeyPoint:
               indexIsOpen = True
         

            pseudoFixKeyPoint = handLandmarks.landmark[10].y
            if handLandmarks.landmark[11].y < pseudoFixKeyPoint and handLandmarks.landmark[12].y < pseudoFixKeyPoint:
               middelIsOpen = True

            pseudoFixKeyPoint = handLandmarks.landmark[14].y
            if handLandmarks.landmark[15].y < pseudoFixKeyPoint and handLandmarks.landmark[16].y < pseudoFixKeyPoint:
               ringIsOpen = True

            pseudoFixKeyPoint = handLandmarks.landmark[18].y
            if handLandmarks.landmark[19].y < pseudoFixKeyPoint and handLandmarks.landmark[20].y < pseudoFixKeyPoint:
               pinkyIsOpen = True

            if thumbIsOpen and indexIsOpen and middelIsOpen and ringIsOpen and pinkyIsOpen:
               print("FIVE!")

            elif not thumbIsOpen and indexIsOpen and middelIsOpen and ringIsOpen and pinkyIsOpen:
               print("FOUR!")

            elif not thumbIsOpen and indexIsOpen and middelIsOpen and ringIsOpen and not pinkyIsOpen:
               print("THREE!")

            elif not thumbIsOpen and indexIsOpen and middelIsOpen and not ringIsOpen and not pinkyIsOpen:
               print("TWO!")

            elif not thumbIsOpen and indexIsOpen and not middelIsOpen and not ringIsOpen and not pinkyIsOpen:
               print("ONE!")

            elif not thumbIsOpen and indexIsOpen and not middelIsOpen and not ringIsOpen and pinkyIsOpen:
               print("ROCK!")

            elif thumbIsOpen and indexIsOpen and not middelIsOpen and not ringIsOpen and pinkyIsOpen:
               print("SPIDERMAN!")

            elif not thumbIsOpen and not indexIsOpen and not middelIsOpen and not ringIsOpen and not pinkyIsOpen:
               print("FIST!")
   
            print("FingerState: thumbIsOpen? " + str(thumbIsOpen) + " - indexIsOpen? " + str(indexIsOpen) + " - middelIsOpen? " +
            str(middelIsOpen) + " - ringIsOpen? " + str(ringIsOpen) + " - pinkyIsOpen? " + str(pinkyIsOpen))
image = cv2.resize(image, (600, 600))
cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
