import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/adolf-fick/Desktop/git_ws/Mekatronikk3/install/ngc_hmi'
