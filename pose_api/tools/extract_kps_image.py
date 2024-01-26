from ultralytics import YOLO
from pose_api.tools.select_kps import select_specific_kps
import json
import os
from urllib.request import urlretrieve
import cv2

currentFile_parent_folder = os.path.dirname(os.path.abspath(__file__))

keypoint_order_path = f'{currentFile_parent_folder}/keypoint_order.json'
body_groups_path = f'{currentFile_parent_folder}/body_groups.json'

with open(keypoint_order_path, 'r') as f:
    keypoint_order_data = json.load(f)

with open(body_groups_path, 'r') as f:
    body_groups_data = json.load(f)


def kps_extractor(image):
    pose_model = None
    pose_model_path = os.path.join(currentFile_parent_folder, 'cv_models' ,'YOLOv8m-pose-p6.pt')
    if os.path.exists(pose_model_path):
        pose_model = YOLO(pose_model_path)
    else:
        yolov8m_pose_url = 'https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8m-pose.pt'
        urlretrieve(yolov8m_pose_url, pose_model_path)
        pose_model = YOLO(pose_model_path)

    if image is not None:
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
        width, height, __channels = image.shape
        print('shape', image.shape)
        results = pose_model(source=image, show=False, save=False, show_boxes=False)
        keypoint_data = {}
        frame_num = 0

        for result in results:
            print('frame ', frame_num)
            frame_num += 1
            kpts = result.keypoints.xy[0]
            
            converted_kps = []
            
            for idx in range(len(kpts)):
                x, y = int(kpts[idx][0]), int(kpts[idx][1]) # OpenCV only deals with ints, not floats
                converted_kps.append([x/width, y/height ]) # Normalize kps coordinates 0-1

            keypoint_data[frame_num] = converted_kps

        return keypoint_data

    else:
        print("ERROR: No image available")
        return dict()

