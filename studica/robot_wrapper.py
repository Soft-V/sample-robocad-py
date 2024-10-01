# the same as Training in studica examples

from global_holder import GlobalHolder
from constants import Constants

class RobotWrapper:
    def get_ir(self):
        return getattr(GlobalHolder.robot, "analog_" + str(Constants.SHARP_PORT))
    
    def get_us(self):
        return getattr(GlobalHolder.robot, "us_" + str(Constants.SONIC_PORT))
    
    def set_left_motor_speed(self, speed: float):
        setattr(GlobalHolder.robot, "motor_speed_" + str(Constants.LEFT_MOTOR_PORT), speed)

    def set_right_motor_speed(self, speed: float):
        setattr(GlobalHolder.robot, "motor_speed_" + str(Constants.RIGHT_MOTOR_PORT), speed)

    def get_left_motor_enc(self):
        return getattr(GlobalHolder.robot, "motor_enc_" + str(Constants.LEFT_MOTOR_PORT))
    
    def get_right_motor_enc(self):
        return getattr(GlobalHolder.robot, "motor_enc_" + str(Constants.RIGHT_MOTOR_PORT))
    
    def get_yaw(self):
        return GlobalHolder.robot.yaw
    
    def set_servo_angle(self, angle: float):
        GlobalHolder.robot.set_angle_hcdio(angle, Constants.SERVO_MOTOR_PORT)

    def get_camera_image(self):
        return GlobalHolder.robot.camera_image

    
    def periodic(self):
        '''Code that runs once every robot loop'''

        # Updates for outputs to the shufflecad
        GlobalHolder.sv_ir_sensor.set_float(self.get_ir())
        GlobalHolder.sv_us_sensor.set_float(self.get_us())

        # Updates servo angle from shufflecad
        self.set_servo_angle(GlobalHolder.sv_servo_motor.get_float())

        # Updates camera image in shufflecad
        GlobalHolder.cv_default_camera.set_mat(self.get_camera_image())
