#! /usr/bin/python3
import pyrealsense2 as rs
import numpy as np
import cv2
import time
from datetime import datetime

# Initialize the RealSense pipeline 

pipeline_d435i = rs.pipeline()

# Configuration for D435i
config_d435i = rs.config()
config_d435i.enable_device('D435i_SERIAL_NUMBER')  # Replace with the actual serial number of the D435i
config_d435i.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
config_d435i.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

# Start the pipeline
pipeline_d435i.start(config_d435i)

try:
    while True:
        # Get frame
        frames_d435i = pipeline_d435i.wait_for_frames()



        # Get the color and depth frames from D435i
        color_frame_d435i = frames_d435i.get_color_frame()
        depth_frame_d435i = frames_d435i.get_depth_frame()

        if not color_frame_d435i or not depth_frame_d435i:
            continue

        # Convert the frames to numpy arrays
        color_image_d435i = np.asanyarray(color_frame_d435i.get_data())
        depth_image_d435i = np.asanyarray(depth_frame_d435i.get_data())

        # Save the images once per second
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        cv2.imwrite(f'D435i_color_{timestamp}.png', color_image_d435i)
        cv2.imwrite(f'D435i_depth_{timestamp}.png', depth_image_d435i)

        print(f'Captured images at {timestamp}')

        # Wait for 1 second before capturing the next frame
        time.sleep(1)

finally:
    # Stop the pipelines
    pipeline_d435i.stop()
