#!/usr/bin/env python2
import rospy
from std_msgs.msg import String

rospy.init_node('name')
pub=rospy.Publisher('name',String)
rate=rospy.Rate(3)

name="Ritvik"
while not rospy.is_shutdown():
    pub.publish(name)
    rate.sleep()