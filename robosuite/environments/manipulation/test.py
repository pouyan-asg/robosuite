"""a simple test to see if mujoco works"""


import mujoco
from mujoco import viewer
import os

# Path to your MJCF XML file
model_path = "/home/pouyan/phd/imitation_learning/robosuite/robosuite/models/assets/robots/meca500/robot.xml"
# model_path = "/home/pouyan/phd/imitation_learning/robosuite/robosuite/environments/manipulation/quadruped.xml"
assert os.path.exists(model_path), f"File not found: {model_path}"

# Load the model
model = mujoco.MjModel.from_xml_path(model_path)
data = mujoco.MjData(model)

# Launch interactive viewer with free camera
with viewer.launch_passive(model, data) as v:
    print("Use mouse to rotate/pan/zoom. Press ESC to quit.")
    while v.is_running():
        mujoco.mj_step(model, data)
        v.sync()


