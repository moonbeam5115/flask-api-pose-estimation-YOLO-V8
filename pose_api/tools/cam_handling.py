import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

pose = mp_pose.Pose(
    min_detection_confidence=0.5, min_tracking_confidence=0.5)


# def gen(webcam):
#     while True:
#         try:
#             success, image = webcam.read()
#             print(success)

#             image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
#             # To improve performance, optionally mark the image as not writeable to
#             # pass by reference.
#             image.flags.writeable = False
#             results = pose.process(image)
#             # Draw the pose annotation on the image.
#             image.flags.writeable = True
#             image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#             mp_drawing.draw_landmarks(
#                 image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
#             ret, jpeg = cv2.imencode('.jpg', image)
#             frame = jpeg.tobytes()
#             yield (b'--frame\r\n'
#                 b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
#         except:
#             break


def reset_cam(webcam):
    webcam.open(-1)