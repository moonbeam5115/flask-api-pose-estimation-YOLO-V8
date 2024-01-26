import json
import os

currentFile_parent_folder = os.path.dirname(os.path.abspath(__file__))

keypoint_order_path = f'{currentFile_parent_folder}/keypoint_order.json'
body_groups_path = f'{currentFile_parent_folder}/body_groups.json'

with open(keypoint_order_path, 'r') as f:
    keypoint_order_data = json.load(f)

with open(body_groups_path, 'r') as f:
    body_groups_data = json.load(f)

def select_specific_kps(kps:list = None, select_type='custom'):
    '''
    Allows you to select specific Keypoints from Yolov8 Pose Estimation model

    select_type='custom'
    You can select from any of the following combination of keypoints
    "Nose", "Left-eye", "Right-eye", "Left-ear", "Right-ear",
    "Left-shoulder", "Right-shoulder", "Left-elbow", "Right-elbow",
    "Left-wrist", "Right-wrist", "Left-hip", "Right-hip",
    "Left-knee", "Right-knee", "Left-ankle", "Right-ankle
    
    select_type='complex'
    You can also select a body complex (collection of common joints)
    "L_Knee-complex", "R_Knee-complex", 
    "L_Hip-complex", "R_Hip-complex",
    "L_Shoulder-complex", "R_Shoulder-complex",
    "L_Elbow-complex", "R_Elbow-complex"

    select_type='side'
    Finally, you can select a side of the body: Left or Right
    "L_side",
    "R_side"

    Output:
    List of Integer(s) representing the index IDs of the joint from keypoint_order.json
    0-16
    '''
    output_kps = []
    if select_type == 'custom':
        for kp_name in kps:
            output_kps.append(keypoint_order_data[kp_name])

        return output_kps
    elif select_type == 'complex':
        for kp_complex in kps:
            complex_names = body_groups_data[kp_complex]
            for kp_name in complex_names:
                kp_value = keypoint_order_data[kp_name]
                if kp_value not in output_kps:
                    output_kps.append(keypoint_order_data[kp_name])
        
        return output_kps

    elif select_type == 'side':
        for body_side in kps:
            side_kp_names = body_groups_data[body_side]
            for kp_name in side_kp_names:
                output_kps.append(keypoint_order_data[kp_name])

        return output_kps
    
    else:
        print("Please select from one of: 'custom', 'complex', or 'side'")

