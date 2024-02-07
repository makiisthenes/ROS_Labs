# !/usr.bin/env python
# Make sure the source command runs this as a python file and not a bash file.

# Start of ROS node for the robot using Python and RosPy Library.
# This node is responsible for the communication between the robot and the ROS Master.

# Subscriber and Publisher Basics for the robot.
# Based on the url:
# http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber(python)


# These dependencies are required for the ROS node to work, however these dependencies are present in the CMakeLists.txt file, 
# and package, so will present in the robot's system when building.

import rospy
from std_msgs.msg import String

# Publisher Node and Observer Node.

def publisher():
    """Talker into the topic, given. """
    pub = rospy.Publisher('chatter_topic', String, queue_size=10)  # We are stating that the ROSNode is published to the topic 'chatter_topic' with the message type 'String'.
    rospy.init_node('talker', anonymous=True)  # We need to set a ROS Node Name, and we are setting it to 'talker'.
    rate = rospy.Rate(10) # 10hz  This set, means when using function sleep of the rate object, it sleeps to achieve the 10Hz rate. Sleeps for 1/10 seconds.
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)  # This function, prints the message to console, get written to node log file, and also written to rosout tool, good for debugging.
        pub.publish(hello_str)
        rate.sleep()



if __name__ == "__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
    