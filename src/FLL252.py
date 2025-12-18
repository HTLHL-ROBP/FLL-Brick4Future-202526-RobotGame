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
    straight(420)
    #schlag damit Zahnräder fliegen
    rotspeed2(120)
    rotspeed2(-120)
    rotspeed2(120)
    rotspeed2(-120)
    rotspeed2(120)
    rotspeed2(-120)
    #Steine rollen lassen
    turn(-30)
    straight(300)
    turn(110)
    rot1(-120)
    straight(70)
    
    turn(-40)
    rot1(-10)
    turn(-50)
    rot1(130)
    # Steine rausschieben
    turn(-83)
    straight(-330)
    straight(100)
    wait(500)
    straight(-170)
    turn(85)
    straight(120)
    turn(-20)
    straight(20)
    rot1(-130)
    turn(10)
    rot1(130)
    straight(-150)
    turn(15)
    straight(-100)
    
    
    #turn(78)
    #straight(140)
    #rot1(-130)
    #turn(10)
    #rot1(130)
    #zurueck fahren
    #straight(-110)
    #turn(-75)
    #straight(400)
   # turn(-100)
    #straight(700)

def test1():
    #umlegen
    straight(170)
    turn(-45)
    straight(300)
    turn(-40)
    #aufheben Lore
    straight(-150)
    turn(42)
    straight(300)
    rot2(80)
    straight(140)
    rot2(-80)
    #aufstellen aufdrücken
    turn(-30)
    straight(285)
    turn(30)
    straight(-800)
    straight(300)
    #Lore rüberfahren
    turn(-43)
    rot1(-150)
    straight(250)
    rot1(75)
    wait(2000)
    straight(-100)
    rot1(75)
    
    #zrück fahren
    straight(-200)
    turn(25)
    straight(-500)
    turn(50)
    straight(-580)
    
    stop()


def test2():
    straight(-200)

def test3():
    straight(300)
    turn(-90)
    straight(700)
    turn(-90)
    straight(110)
    turn(-65)
    straight(50)
    rot2(1200)
    stop()   
        







def main():
    menu = ["A", "B", "C","1","2","3","4","5"]

    while True:
        # make a menu to choose a letter. You can also use numbers.
        selected = hub_menu(*menu)

        # based on the selection, run a program.
        if selected == "A":
            test1()

        elif selected == "B":
            test3()

        elif selected == "C":
            print(version)
            
        
        else:
            pass

        # advance menu
        next_index = (menu.index(selected) + 1) % len(menu)
        menu = menu[next_index:] + menu[:next_index]
 
main()