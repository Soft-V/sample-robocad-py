from robocad.studica import RobotVmxTitan
from robocad.shufflecad import Shufflecad

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
            GlobalHolder.shufflecad = Shufflecad(GlobalHolder.robot)
            GlobalHolder.init_variables()

    @staticmethod
    def stop():
        # stopping user program
        if GlobalHolder.program is not None:
            GlobalHolder.program.end()
        # stopping shufflecad
        if GlobalHolder.shufflecad is not None:
            GlobalHolder.shufflecad.stop()
        # stopping our robot
        if GlobalHolder.robot is not None:
            GlobalHolder.robot.stop()