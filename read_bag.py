#! /usr/bin/python3
import pyrealsense2 as rs

# Create a pipeline object for data flow management
pipeline = rs.pipeline()

# Configure the pipeline to stream from the .bag file
config = rs.config()
config.enable_device_from_file("path_to_file.bag")

# Start streaming from the file
pipeline.start(config)

try:
    while True:
        # Wait for a coherent set of frames
        frames = pipeline.wait_for_frames()

        # Get the depth and color frames
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()

        if not depth_frame or not color_frame:
            continue

        # Further processing of frames (e.g., conversion to numpy arrays) can be done here

        # Example: Convert frames to numpy arrays
        import numpy as np
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        # Display the frames or process further
        # For instance, you could use OpenCV to display the frames
        import cv2
        cv2.imshow('Depth Frame', depth_image)
        cv2.imshow('Color Frame', color_image)

        # Break loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Stop the pipeline
    pipeline.stop()
    cv2.destroyAllWindows()
