#!/usr/bin/env python

import rospy
import lcm

from go1_imu_republisher import imu_lcm
from sensor_msgs.msg import Imu

def imuHandler(channel, data):
    lcmMsg =imu_lcm.decode(data)
    rosMsg = Imu()

    # TODO
    # rosMsg.angular_velocity.x = ...
    # rosMsg.angular_velocity.y = ...
    # rosMsg.angular_velocity.z = ...
    # rosMsg.linear_acceleration.x = ...
    # rosMsg.linear_acceleration.y = ...
    # rosMsg.linear_acceleration.z = ...

    pub.publish(rosMsg)

def republisher():
    pub = rospy.Publisher('imu', Imu, queue_size=10)
    rospy.init_node('go1_imu_republisher', anonymous=True)
    rate = rospy.Rate(100) # 10hz
    global lc = lcm.LCM()
    global subscription = lc.subscribe("IMU", imuHandler)
    while not rospy.is_shutdown():
        lc.handle()
        rate.sleep()

if __name__ == '__main__':
    try:
        republisher()
    except rospy.ROSInterruptException:
        pass
    lc.unsubscribe(subscription)
