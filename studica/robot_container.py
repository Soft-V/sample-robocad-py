from robocad.studica import RobotVmxTitan
from robocad.shufflecad.shufflecad import Shufflecad

from constants import Constants
from robot_wrapper import RobotWrapper
from program import Program
from global_holder import GlobalHolder

class RobotContainer:
    @staticmethod
    def init():
        GlobalHolder.robot = RobotVmxTitan(Constants.IS_REAL_ROBOT)
        GlobalHolder.wrapper = RobotWrapper()
        GlobalHolder.program = Program()
        if (Constants.ENABLE_SHUFFLECAD):
            Shufflecad.start()

    @staticmethod
    def stop():
        # stopping user program
        if GlobalHolder.program is not None:
            GlobalHolder.program.end()
        # stopping our robot
        if GlobalHolder.robot is not None:
            GlobalHolder.robot.stop()
        if (Constants.ENABLE_SHUFFLECAD):
            Shufflecad.stop()