# entrance of the whole program

import signal
import time

from robot_container import RobotContainer
from constants import Constants

# handling signals of prog terminate
def handler(signum, _):
    RobotContainer.stop()
    raise SystemExit("Exited")


signal.signal(signal.SIGTERM, handler)
signal.signal(signal.SIGINT, handler)


RobotContainer.init()

# wait a bit so robocad inites
time.sleep(0.1)

RobotContainer.program.initialize()

while True:
    try:
        RobotContainer.program.execute()

        time.sleep(Constants.MAIN_LOOP_DELAY)
    except (Exception, IOError) as e:
        # handle errors if needed
        pass
