#!/usr/bin/env python2

import rospy
from std_msgs.msg import String

rospy.init_node("surname")
pub=rospy.Publisher("surname",String)
rate=rospy.Rate(3)

surname="Puranik"
while not rospy.is_shutdown():
    pub.publish(surname)
    rate.sleep()