from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Axis, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.tools import hub_menu
from pybricks import version

hub = PrimeHub()
hub: PrimeHub = None
robot: DriveBase = None
arm1: Motor = None
arm2: Motor = None

def _init_hub():
    """Initialize the prime hub"""
    _hub = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
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
    arm1.run_angle(500, angle)

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
speed(
        straight_speed=500,
        straight_acceleration=700,
        turn_rate=300,
        turn_acceleration=300
    )

def run_1():
    straight(410)
    turn(27)
    straight(240)
    turn(-70)
    straight(210)

    #schlaufe hoch heben
    rot2(-68)
    straight(-160)
    turn(-45)

    #links rechts schieben
    straight(35)
    rot1(-170)
    rot1(300)

    #zurück fahren für roten stiehl raus ziehen
    straight(-100) 

    #arm runter für roten stiehl
    rot2(80)

    #vor zu fahren zu rotem stiehl
    straight(120)
    rot2(-70)
    
    #zurück fahren
    straight(-120)
    turn(-80)
    straight(500)


    raise SystemExit

def run_2():
    #fahren zu schiff
    straight(310)

    #runter ziehen
    rot2(200)
    straight(-90)
    rot2(-200)
    straight(-60)

    #schiff hochschieben
    turn(-30)
    straight(200)
    turn(30)
    straight(200)

    #fahren zu katapult
    straight(-40)
    turn(-50)
    straight(440)
    turn(50)
    straight(20)

    #mast runterdrücken
    rot1(-140)
    rot1(140)

    #karren rausziehen
    turn(60)
    straight(100)
    turn(160)
    straight(-310)
    rot2(220)
    turn(-50)

    #
    straight(-600)
    turn(-80)
    stop()


  

def power():
    print(hub.battery.current())

def main():
    menu = ["A", "B", "C"]

    while True:
        # make a menu to choose a letter. You can also use numbers.
        selected = hub_menu(*menu)

        # based on the selection, run a program.
        if selected == "A":
            run_1()

        elif selected == "B":
            run_2()

        elif selected == "C":
            print(version)
            
        
        else:
            pass

        # advance menu
        next_index = (menu.index(selected) + 1) % len(menu)
        menu = menu[next_index:] + menu[:next_index]

main()

print(hub.battery.voltage())
print(hub.battery.current())
