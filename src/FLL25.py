from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Axis, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.tools import hub_menu

hub = None
robot = None
arm1 = None
arm2 = None

def _init_hub():
    """Initialize the prime hub"""
    _hub = PrimeHub(top_side=Axis.Z,front_side=Axis.Y)
    _hub.speaker.beep()
    _hub.light.on(Color.GREEN)
    return _hub

def _init_robot():
    """Initializes the drive base (aka robot)"""
    right_motor = Motor(Port.E, Direction.CLOCKWISE)
    left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    _robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=120)
    _robot.use_gyro(True)
    print(_robot.settings())
    return _robot

def _init_arm1():
    """Initializes the first arm"""
    arm = Motor(Port.F)
    return arm

def _init_arm2():
    """Initializes the second arm"""
    arm = Motor(Port.B)
    return arm

def init():
    """initialization function, should only be called once"""
    global hub, robot, arm1, arm2
    hub = _init_hub()
    robot = _init_robot()
    arm1 = _init_arm1()
    arm2 = _init_arm2()
    wait(10)

def speed(straight_speed, straight_acceleration, turn_rate, turn_acceleration):
    """Here you can modify the speed settings. You can call this function multiple times"""
    robot.settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)

def straight(distance):
    """Drive straight. Use negative value to drive back"""
    robot.straight(-distance)

def turn(angle):
    """Turn by relative angle. Negative angle turns counterclockwise"""
    robot.turn(angle)

def rot1(angle):
    """Turn arm1 by realtive angle. Negative angle turns counterclockwise"""
    arm1.run_angle(200, angle)

def rot2(angle):
    """Turn arm2 by realtive angle. Negative angle turns counterclockwise"""
    arm2.run_angle(500, angle)

def rotspeed1(angle):
    arm1.run_angle(1000, angle)

def rotspeed2(angle):
    arm2.run_angle(1000, angle)    

def rotslow1(angle):
    arm1.run_angle(420, angle)

def rotslow2(angle):
    arm2.run_angle(60, angle)



def rot1stalled(speed, duty_limit = 40):
    arm1.run_until_stalled(speed, duty_limit=duty_limit)

 
def rot2stalled(speed, duty_limit = 40):
    arm2.run_until_stalled(speed, duty_limit=duty_limit)

init()
speed(500,700,300,300)

def test():
    straight(410)
    turn(27)
    straight(240)
    turn(-71)
    straight(220)
    rot2(-80)
    straight(-175)
    turn(-45)
    straight(62)
    rot1(160)
    rot1(-330)
    
    straight(-100)
    turn(10)
    rot1(300)
    rot2(63)
    straight(120)
    rot2(-65)


    rot1(-130)





def main():
    menu = ["A", "B", "C","1","2","3","4","5"]

    while True:
    # Make a menu to choose a letter. You can also use numbers.
        selected = hub_menu(*menu)

    # Based on the selection, run a program.
        if selected == "A":
            test()
        elif selected == "B":
            pass
        elif selected == "C":
            pass
        elif selected == "1":
            pass
        elif selected == "2":
            pass
        elif selected == "3":
            pass
        elif selected == "4":
            pass
        elif selected == "5":
            pass
        else:
            pass

        # advance menu
        next_index = (menu.index(selected) + 1) % len(menu)
        menu = menu[next_index:] + menu[:next_index]

main()