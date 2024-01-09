from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *
hub = PrimeHub()
from spike import Motor

pair = MotorPair('E', 'F')
motor = Motor('C')

pair.move(300,'cm',0,30) # 전진 TV 장난감 끌고가는 코드 
