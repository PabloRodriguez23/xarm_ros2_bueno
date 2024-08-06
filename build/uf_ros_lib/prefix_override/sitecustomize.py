import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/prodriguez/GITS/xarm_ros2_bueno/install/uf_ros_lib'
