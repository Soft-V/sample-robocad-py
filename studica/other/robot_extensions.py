from robocad.studica import RobotVmxTitan

class RobotExtensions:
    @staticmethod
    def get_analog(robot: RobotVmxTitan, port: int) -> float:
        if (port == 1): return robot.analog_1
        elif (port == 2): return robot.analog_2
        elif (port == 3): return robot.analog_3
        elif (port == 4): return robot.analog_4
        else: return 0

    @staticmethod
    def get_ultrasound(robot: RobotVmxTitan, port: int) -> float:
        if (port == 1): return robot.us_1
        elif (port == 2): return robot.us_2
        else: return 0

    @staticmethod
    def set_motor_speed(robot: RobotVmxTitan, port: int, speed: float) -> None:
        if (port == 0): robot.motor_speed_0 = speed
        elif (port == 1): robot.motor_speed_1 = speed
        elif (port == 2): robot.motor_speed_2 = speed
        elif (port == 3): robot.motor_speed_3 = speed

    @staticmethod
    def get_motor_enc(robot: RobotVmxTitan, port: int) -> float:
        if (port == 0): return robot.motor_enc_0
        elif (port == 1): return robot.motor_enc_1
        elif (port == 2): return robot.motor_enc_2
        elif (port == 3): return robot.motor_enc_3
        else: return 0
