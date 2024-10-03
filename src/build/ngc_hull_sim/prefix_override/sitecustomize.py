import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/alfred/shared_mac/MEPA2001_2024/src/install/ngc_hull_sim'
