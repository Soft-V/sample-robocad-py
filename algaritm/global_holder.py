# workaround of python circular import problem
from robocad.algaritm import RobotAlgaritm
from robocad.shufflecad import Shufflecad
from robocad.shufflecad import ShuffleVariable, CameraVariable

class GlobalHolder:
    robot: RobotAlgaritm = None
    shufflecad: Shufflecad = None
    wrapper = None
    program = None

    # Shufflecad variables init
    sv_ir_sensor: ShuffleVariable = None
    sv_us_sensor: ShuffleVariable = None
    sv_servo_motor: ShuffleVariable = None
    cv_default_camera: CameraVariable = None

    @classmethod
    def init_variables(cls):
        cls.sv_ir_sensor = cls.shufflecad.add_var(ShuffleVariable("ir sens", ShuffleVariable.FLOAT_TYPE, ShuffleVariable.OUT_VAR))
        cls.sv_us_sensor = cls.shufflecad.add_var(ShuffleVariable("us sens", ShuffleVariable.FLOAT_TYPE, ShuffleVariable.OUT_VAR))
        cls.sv_servo_motor = cls.shufflecad.add_var(ShuffleVariable("servo m", ShuffleVariable.SLIDER_TYPE, ShuffleVariable.IN_VAR))
        cls.cv_default_camera = cls.shufflecad.add_var(CameraVariable("default"))
