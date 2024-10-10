import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/alfred/shared_mac/Mekatronikk3/src/install/regulator'
