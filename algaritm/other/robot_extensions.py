from robocad.algaritm import RobotAlgaritm

class RobotExtensions:
    @staticmethod
    def get_analog(robot: RobotAlgaritm, port: int) -> float:
        if port == 1: return robot.analog_1
        elif port == 2: return robot.analog_2
        elif port == 3: return robot.analog_3
        elif port == 4: return robot.analog_4
        elif port == 5: return robot.analog_5
        elif port == 6: return robot.analog_6
        elif port == 7: return robot.analog_7
        elif port == 8: return robot.analog_8
        else: return 0

    @staticmethod
    def get_ultrasound(robot: RobotAlgaritm, port: int) -> float:
        if port == 1: return robot.us_1
        elif port == 2: return robot.us_2
        elif port == 3: return robot.us_3
        elif port == 4: return robot.us_4
        else: return 0

    @staticmethod
    def set_motor_speed(robot: RobotAlgaritm, port: int, speed: float) -> None:
        if port == 0: robot.motor_speed_0 = speed
        elif port == 1: robot.motor_speed_1 = speed
        elif port == 2: robot.motor_speed_2 = speed
        elif port == 3: robot.motor_speed_3 = speed

    @staticmethod
    def get_motor_enc(robot: RobotAlgaritm, port: int) -> float:
        if port == 0: return robot.motor_enc_0
        elif port == 1: return robot.motor_enc_1
        elif port == 2: return robot.motor_enc_2
        elif port == 3: return robot.motor_enc_3
        else: return 0
