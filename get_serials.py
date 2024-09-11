import pyrealsense2 as rs

# Create a context object. This object owns the handles to all connected RealSense devices.
ctx = rs.context()

print(f"Number of devices connected: {len(ctx.devices)}")

if len(ctx.devices) == 0:
    print("No RealSense devices detected. Check connection and permissions.")
else:
    for dev in ctx.devices:
        print(f"Device: {dev.get_info(rs.camera_info.name)}, Serial Number: {dev.get_info(rs.camera_info.serial_number)}")
