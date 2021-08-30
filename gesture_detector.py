import math
import mediapipe as mp
import cv2

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
diccionarioPalabras = {
               "11111":"CINCO",
               "01111":"CUATRO",
               "01110":"TRES",
               "01100":"DOS",
               "01000":"UNO",
               "01001":"ROCK",
               "11001":"SPIDERMAN",
               "00000":"PUÑO",
               "11000":"LUNES",
            }
with mp_hands.Hands( 
   static_image_mode = True,
   max_num_hands=1,
   min_detection_confidence=0.5 ) as hands:

   #image = cv2.imread("I_Uno_A.jpeg")
   #image = cv2.imread("I_Dos_A.jpeg")
   #image = cv2.imread("I_Tres_A.jpeg")
   #image = cv2.imread("I_Cuatro_A.jpeg")
   image = cv2.imread("D_Cinco_A_Borrosa.jpeg")
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
            thumbIsOpen = "0"
            indexIsOpen = "0"
            middelIsOpen = "0"
            ringIsOpen = "0"
            pinkyIsOpen = "0"
                     
            pseudoFixKeyPoint = handLandmarks.landmark[2].x

            if label == 'Right':
               if handLandmarks.landmark[3].x < pseudoFixKeyPoint and handLandmarks.landmark[4].x < pseudoFixKeyPoint:
                  thumbIsOpen = "1"
            elif label == 'Left':
               if handLandmarks.landmark[3].x > pseudoFixKeyPoint and handLandmarks.landmark[4].x > pseudoFixKeyPoint:
                  thumbIsOpen = "1"

            pseudoFixKeyPoint = handLandmarks.landmark[6].y
            if handLandmarks.landmark[7].y < pseudoFixKeyPoint and handLandmarks.landmark[8].y < pseudoFixKeyPoint:
               indexIsOpen = "1"
         
            pseudoFixKeyPoint = handLandmarks.landmark[10].y
            if handLandmarks.landmark[11].y < pseudoFixKeyPoint and handLandmarks.landmark[12].y < pseudoFixKeyPoint:
               middelIsOpen = "1"

            pseudoFixKeyPoint = handLandmarks.landmark[14].y
            if handLandmarks.landmark[15].y < pseudoFixKeyPoint and handLandmarks.landmark[16].y < pseudoFixKeyPoint:
               ringIsOpen = "1"

            pseudoFixKeyPoint = handLandmarks.landmark[18].y
            if handLandmarks.landmark[19].y < pseudoFixKeyPoint and handLandmarks.landmark[20].y < pseudoFixKeyPoint:
               pinkyIsOpen = "1"
            resultadoValidacion = thumbIsOpen+indexIsOpen+middelIsOpen+ringIsOpen+pinkyIsOpen

            if resultadoValidacion in diccionarioPalabras:
               palabra = diccionarioPalabras[resultadoValidacion]
            print("Estado Dedos (" + resultadoValidacion + "): PulgarIsOpen? " + str(thumbIsOpen) + " - indexIsOpen? " + str(indexIsOpen) + " - middelIsOpen? " +
            str(middelIsOpen) + " - ringIsOpen? " + str(ringIsOpen) + " - pinkyIsOpen? " + str(pinkyIsOpen))

image = cv2.resize(image, (600, 600))
image = cv2.flip(image, 1) 
cv2.imshow(palabra,image)
cv2.waitKey(0)
cv2.destroyAllWindows()
