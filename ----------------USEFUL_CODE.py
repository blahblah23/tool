

from pprint import pprint
# change cwd to this script
import os
cwdpath = os.path.dirname(os.path.abspath(__file__))
# print(os.getcwd())
# print(repr(cwdpath))
os.chdir(cwdpath)


# pprint(os.path.__dict__)
print(os.listdir('.'))

    # makedir if needed
# filedir = 'txt\\{}'.format()
# if not os.path.exists(filedir):
#     os.makedirs(filedir, exist_ok=True)

