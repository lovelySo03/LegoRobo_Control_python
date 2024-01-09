from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

# 허브의 기능을 사용하기 위해 PrimeHub를 초기화하고, hub라고 이름을 붙입니다.
hub = PrimeHub()

# 허브에 있는 5X5 light matrix에 Happy 이미지를 표시합니다.
hub.light_matrix.show_image('HAPPY')

#//////////////// 모터가 가진 기능을 객체를 통해 사용하기 
# 모터 선언해주기. 모터가 포트 C에 연결됨
motor = Motor('C')
motor.set_default_speed(100)
# 모터가 절대위치 0으로 이동함 
motor.run_to_position(0)

# 왼쪽 모터 포트E에 연결, 오른쪽 모터는 포트 F에 연결
pair = MotorPair('E','F')

# 전진 및 후진(move)
pair = MotorPair('E','F')
pair.move(20,'cm',0,30)
wait_for_seconds(3)
pair.move(20,'cm',0,-30)

# 탱크 모드 
# 로봇이 20cm만큼 왼쪽 모터 30, 오른쪽 모터 30의 속도로 움직인다 
# 속도가 양수이기 때문에 앞으로 이동한다 
pair.move_tank(20,'cm',30,30) 

# 로봇이 20cm만큼 왼쪽 모터 -30, 오른쪽 모터 -30의 속도로 움직인다
# 속도가 양수이기 때문에 앞으로 이동한다
pair.move_tank(20,'cm',-30,-30)

# 로봇이 50의 속도로 앞으로 움직이기 시작한다
# 속도가 양수이면 앞으로, 음수이면 뒤로 움직인다
pair.start(speed=50)
#3초 기다리는 동안 로봇이 앞으로 움직인다
wait_for_seconds(3)
#로봇이 멈춘다 
pair.stop()

#Point turn
# 로봇이 720도만큼 왼쪽 모터30, 오른쪽 모터-30의 속도로 움직인다 
# 모터가 서로 반대로 회전하기 때문에 point turn을 한다 
pair.move_tank(720,'degrees',30,-30)
# 로봇이 2회전만큼 왼쪽 모터 -30, 오른쪽 모터 30의 속도로 움직인다
# 모터가 서로 반대로 회전하기 때문에 point turn을 한다 
pair.move_tank(2,'rotations',-30,30)


# Swing turn 
# 로봇이 720도만큼 왼쪽 모터 30, 오른쪽 모터 0의 속도로 움직인다. 
# 하나의 모터만 회전하기 때문에 Swing turn을 한다 
pair.move_tank(720,'degrees',30,0)
pair.move_tank(2,'rotations',0,30)

# 로봇이 5초 동안 왼쪽 모터 50, 오른쪽 모터 30의 속도로 움직인다
# 양쪽 모터가 서로 다른 속도로 회전하기 때문에 Curve Turn을 한다 
pair.move_tank(5,'seconds',50,30)

# 로봇의 팔을 위로 110도 움직이기 
motor.run_for_degrees(-110) 
# 로봇의 팔을 아래로 110도 움직이기
motor.run_for_degrees(110)

# 스피커 기능 사용하기
# Primehub 라는 객체를 생성해서 사용하기
hub = PrimeHub()
hub.light_matrix.show_image('RABBIT')
# 이 코드를 사용하면, 소리가 난다. 
# 이 소리를 이용해서 디버깅 가능 
hub.speaker.beep(67,0.5)

# 멜로디 만들기 
hub.speaker.beep(67,0.5)
hub.speaker.beep(79,0.5)
hub.speaker.beep(76,0.5)
hub.speaker.beep(72,0.5)
hub.speaker.beep(74,0.5)
hub.speaker.beep(67,0.5)
hub.speaker.beep(67,0.5)

# light matrix 표현하기 
hub.light_matrix.show_image('RABBIT')
hub.light_matrix.show_image('DUCK')

# 힘의 세기를 측정할 수 있는 ForceSensor
# 힘 센서가 포트 D에 연결됩니다.
door_bell = ForceSensor('D')
# 센서를 누르면 콘솔에 Hello가 프린트 된다
while True:
    if door_bell.is_pressed():
        print('Hello')
        break

# 몇 번 눌렀는지 숫자 표시
force_sensor = ForceSensor('D')
hub = PrimeHub()
count = 0
while count < 10:
    force_sensor.wait_until_pressed()
    force_sensor.wait_until_released()
    count = count + 1
    hub.light_matrix.write(count)

    # 색상을 측정하는 컬러센서
    # 컬러센서가 포트 A에 연결됩니다.
    color_sensor = ColorSensor('A')
    wait_for_seconds(0.5)
    # 색상을 측정합니다
    color = color_sensor.get_color()
    # 콘솔에 색상 이름을 표시합니다.
    print('Detected:', color)

    # 노란색, 빨간색 측정하고 소리내기
    while True:
        if color_sensor.get_color() == 'yellow':
            hub.speaker.beep(80,1)
        elif color_sensor.get_color() == 'red':
            hub.speaker.beep(100,1)

    # 색상별로 다른 동작하기
    while True:
        if color_sensor.get_color() == 'green':
            hub.light_matrix.write('G')
            hub.speaker.beep(71)
            pair.start(0,20)
        elif color_sensor.get_color() == 'red':
            hub.light_matrix.write('R')
            hub.speaker.beep(75)
            pair.stop()
        else :
            hub.light_matrix.write('X')
        # 현재 색상에서 벗어나 새로운 색상을 만날 때까지 기다리기 
        color_sensor.wait_for_new_color()

    # 거리를 측정하는 센서
    # 거리센서를 포트 B에 연결시키기
    dist_sensor = DistanceSensor('B')
    wait_for_seconds(0.5)
    
    # 초음파 측정하기
    # 결과값 None은 거리를 알 수 없는 것 
    dist = dist_sensor.get_distance_cm()
    # 콘솔에 거리 표시하기
    print('dist_cm:', dist)

    # 거리센서의 None 예외처리
    while Ture:
        dist = dist_sensor.get_distance_cm()
        if dist != None:
            print(dist)
        wait_for_seconds(0.2) 

    # 라인 트레이싱
    while True:
        if color.get_color() == 'black':
            pair.start_tank(35,20)
        else :
            pair.start_tank(20,35)
