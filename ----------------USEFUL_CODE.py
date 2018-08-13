


#   linked local to remote so i can "git push"
#   git push -u origin <branchname>
#
#   Assuming that your remote is set up correctly as origin, you'll do git push -u origin <branchname>.
#   Where -u is --set-upstream, which sets the remote branch <branchname> that you want to correspond to the local branch you're pushing from.




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

