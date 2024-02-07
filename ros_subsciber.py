# !/usr.bin/env python

# This is the subscriber node for the robot, that will listen to the chatter_topic,
# and will print the message to the console.

import rospy
from std_msgs.msg import String

def callback(data):
    """Callback function for the subscriber."""
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


def subscriber():
    """Will listen to topic 'chatter_topic' and print the message via loginfo."""
    # Nodes must be unique, and so previous ones with the same name will be kicked.
    # Anonymous is set to True, such that a unique name for our listener can be generated.
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter_topic', String, callback)  # We are subscribing to the topic 'chatter_topic' with the message type 'String'.

    rospy.spin()  # Keeps the node from exiting until the node has been shutdown.

    return


if __name__ == "__main__":
    subscriber()
