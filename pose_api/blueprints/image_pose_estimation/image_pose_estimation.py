from flask import (
    Response, Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, make_response
)
import time
import cv2
import numpy as np
from pose_api.tools.extract_kps_image import kps_extractor

bp = Blueprint('image_pose_estimation', __name__)


@bp.route('/image_pose_estimation/joint_angles/image', methods=['GET', 'POST'])
def estimate_joint_angles_image():
    print('request received... processing')
    try: 
        if request.method == 'POST':
            image_filestr = request.files['image'].read()
            image_bytes = np.fromstring(image_filestr, np.uint8)
            img = cv2.imdecode(image_bytes, cv2.IMREAD_UNCHANGED)

            kp_data = kps_extractor(image=img)
            print(kp_data)

            return kp_data
    except Exception as e:
        print(e)

    return 'Request not set up'
