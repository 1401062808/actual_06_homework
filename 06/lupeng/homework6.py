# python starup file
import sys
import readline
import rlcompleter
import atexit
import os
#tab complection
readline.parse_and_bind('tab: complete')
#histroy file
histfile = os.path.join(os.environ['HOME'], '.pythonhistroy')
try:
    readline.read_history_file(histfile)
except IOError:
    pass
atexit.register(readline.write_history_file, histfile)

del os, histfile, readline, rlcompleter
Username : admin 
Password : 0qcpCmi6 
