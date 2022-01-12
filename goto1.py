from dronekit import LocationGlobalRelative, VehicleMode, connect
import time

vehicle = connect('tcp:127.0.0.1:5762', wait_ready=True, timeout=60)
print("Connected!")
#vehicle = connect('udp:127.0.0.1:14551', wait_ready=True, timeout=60)

while not vehicle.is_armable:
    print("初期化待ちです")
    time.sleep(2)

vehicle.wait_for_mode("GUIDED")

vehicle.arm()

#vehicle.groundspeed = 3.2 

targetAltitude = 20

print("離陸！")
vehicle.simple_takeoff(targetAltitude)

while True:
    print("高度: ",vehicle.location.global_relative_frame.alt)
    if vehicle.location.global_relative_frame.alt >= targetAltitude * 0.95:
        print("到達しました。")
        break
    time.sleep(1)

aLocation = LocationGlobalRelative(35.8556853, 139.4642982, 20)

#座標は大野中の畑道35.8556853, 139.4642982,

vehicle.simple_goto(aLocation)
 
