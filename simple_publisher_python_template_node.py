"""
Victor Velazquez, Ros Node Template Python 

1 publisher, 1 subscriber, 1 service server and 1 service client

to run a node: rosrun your_package your_publisher_node.py

"""
#!/usr/bin/env python
#Publisher Template

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from std_msgs.msg import String  #this needs to be modified to the kind of message you want to publish

def publisher_node():
    pub = rospy.Publisher('topic_name)', String, queue_size=10)   #in string goes the message of the topic
    rospy.init_node('publisher_name', anonymous=True)
    rate = rospy.Rate(10) # loop rate 10hz  

    while not rospy.is_shutdown():  #runs as long as the ROS node is not shut down i.e publish aslong as it runs

        #The following lines can be changed for what ever processing of data is needed and then given to the message to then be published
        message = "hello world %s" % rospy.get_time()
        rospy.loginfo(message)   #print on terminal


        pub.publish(message)     ##publish on topic
        rate.sleep()   #publishing rate

if __name__ == '__main__':
    try:
        publisher_node()
    except rospy.ROSInterruptException:
        pass