from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *
hub = PrimeHub()
from spike import Motor

pair = MotorPair('E', 'F')
motor = Motor('C')

pair.move(30,'cm',0,30) # 전진 TV
pair.move(20,'cm',0,-30) # 후진 
pair.stop()
pair.move_tank(0.25,'rotations',0,30) # 왼쪽으로 꺾기 
pair.move(43,'cm',0,25) # 전진
pair.move_tank(0.5,'rotations',30,-30)

pair.move(30,'cm',0,30) # 전진 풍력발전소 밀기 1회
motor.run_for_degrees(200) # 팔 내리기
wait_for_seconds(3)
pair.move(20,'cm',0,-30) # 후진

pair.move(30,'cm',0,30) # 전진 풍력발전소 밀기 2회
wait_for_seconds(3)
pair.move(20,'cm',0,-30) # 후진

pair.move(30,'cm',0,30) # 전진 풍력발전소 밀기 3회

wait_for_seconds(3)
motor.run_for_degrees(-200) # 팔 올리기 
wait_for_seconds(3)
pair.move(20,'cm',0,-30) # 후진


pair.move_tank(1.5,'rotations',-30,30) # 왼쪽으로 135도 회전 

pair.move(100,'cm',0,30) # 전진. home으로 돌아옴
