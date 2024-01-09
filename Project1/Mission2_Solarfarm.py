from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *
hub = PrimeHub()

pair = MotorPair('E', 'F')
motor = Motor("C")
motor.set_default_speed(100)
motor.run_for_degrees(300)
pair.move(50, 'cm', 0, 30)
pair.move_tank(0.5,'rotations',30,-30)
pair.move(45, 'cm', 0, 30)
pair.move_tank(0.5,'rotations',-30,30)
pair.move(20, 'cm', 0, 30)
pair.move_tank(0.5,'rotations',-30,30)
pair.move(25, 'cm', 0, 30)
pair.move_tank(0.5,'rotations',-30,30)
pair.move(20, 'cm', 0, 30)
pair.move_tank(0.5,'rotations',30,-30)
pair.move(20, 'cm', 0, 30)
pair.move_tank(0.5,'rotations',-30,30)
pair.move(50, 'cm', 0, 30)
