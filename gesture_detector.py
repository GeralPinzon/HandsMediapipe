import math
import mediapipe as mp
import cv2

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

with mp_hands.Hands( 
   static_image_mode = True,
   max_num_hands=1,
   min_detection_confidence=0.5 ) as hands:

   image = cv2.imread("I_Uno_A.jpeg")
   #image = cv2.imread("I_Dos_A.jpeg")
   #image = cv2.imread("I_Tres_A.jpeg")
   #image = cv2.imread("I_Cuatro_A.jpeg")
   #image = cv2.imread("D_Cinco_A_Borrosa.jpeg")
   #image = cv2.imread("I_Cinco_A.jpeg")
   #image = cv2.imread("I_Rock_A.jpeg")
   #image = cv2.imread("I_Spider_A.jpeg")

   height, width, _ = image.shape
   image = cv2.flip(image, 1) #Comentar si se usa la camara frontal

   image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
   
   results = hands.process(image_rgb)
   label = results.multi_handedness[0].classification[0].label
   
   print(results.multi_handedness)
      
   if results.multi_hand_landmarks is not None:
      
      label = results.multi_handedness[0].classification[0].label  # label gives if hand is left or right
      for handLandmarks in results.multi_hand_landmarks:
            
            mp_drawing.draw_landmarks(image, handLandmarks, mp_hands.HAND_CONNECTIONS)
            thumbIsOpen = False
            indexIsOpen = False
            middelIsOpen = False
            ringIsOpen = False
            pinkyIsOpen = False
         
            pseudoFixKeyPoint = handLandmarks.landmark[2].x

            if label == 'Right':
               if handLandmarks.landmark[3].x < pseudoFixKeyPoint and handLandmarks.landmark[4].x < pseudoFixKeyPoint:
                  thumbIsOpen = True
            elif label == 'Left':
               if handLandmarks.landmark[3].x > pseudoFixKeyPoint and handLandmarks.landmark[4].x > pseudoFixKeyPoint:
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
               print("CINCO!")

            elif not thumbIsOpen and indexIsOpen and middelIsOpen and ringIsOpen and pinkyIsOpen:
               print("CUATRO!")

            elif not thumbIsOpen and indexIsOpen and middelIsOpen and ringIsOpen and not pinkyIsOpen:
               print("TRES!")

            elif not thumbIsOpen and indexIsOpen and middelIsOpen and not ringIsOpen and not pinkyIsOpen:
               print("DOS!")

            elif not thumbIsOpen and indexIsOpen and not middelIsOpen and not ringIsOpen and not pinkyIsOpen:
               print("UNO!")

            elif not thumbIsOpen and indexIsOpen and not middelIsOpen and not ringIsOpen and pinkyIsOpen:
               print("ROCK!")

            elif thumbIsOpen and indexIsOpen and not middelIsOpen and not ringIsOpen and pinkyIsOpen:
               print("SPIDERMAN!")

            elif not thumbIsOpen and not indexIsOpen and not middelIsOpen and not ringIsOpen and not pinkyIsOpen:
               print("PUÑO!")
            elif  thumbIsOpen and indexIsOpen and not middelIsOpen and not ringIsOpen and not pinkyIsOpen:
               print("LUNES!")
   

            print("FingerState: thumbIsOpen? " + str(thumbIsOpen) + " - indexIsOpen? " + str(indexIsOpen) + " - middelIsOpen? " +
            str(middelIsOpen) + " - ringIsOpen? " + str(ringIsOpen) + " - pinkyIsOpen? " + str(pinkyIsOpen))
            
image = cv2.resize(image, (600, 600))
image = cv2.flip(image, 1) 
cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
