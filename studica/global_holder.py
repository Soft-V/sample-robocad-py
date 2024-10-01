# workaround of python circular import problem
from robocad.studica import RobotVmxTitan
from robocad.shufflecad.shufflecad import Shufflecad
from robocad.shufflecad.shufflecad_holder import ShuffleVariable, CameraVariable

class GlobalHolder:
    robot: RobotVmxTitan = None
    wrapper = None
    program = None

    sv_ir_sensor: ShuffleVariable = Shufflecad.add_var(ShuffleVariable("ir sens", ShuffleVariable.FLOAT_TYPE, ShuffleVariable.OUT_VAR))
    sv_us_sensor: ShuffleVariable = Shufflecad.add_var(ShuffleVariable("us sens", ShuffleVariable.FLOAT_TYPE, ShuffleVariable.OUT_VAR))
