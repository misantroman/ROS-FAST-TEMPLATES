#!/usr/bin/env python

"""
Victor Velazquez, Ros Node Template Python 

This template is for a node that subscribes to a topic, process data and publishes

"""


import rospy
from std_msgs.msg import String  #modify for specific type of message

def subscriber_callback(data):
    # This function is called whenever new data is received from the subscribed topic
    # Process the data as needed
    processed_data = "Processed: " + data.data

    # Create a message with the processed data  // here just has the case of string extend or modify as necessary
    processed_message = String()
    processed_message.data = processed_data

    # Publish the processed data on a different topic
    pub.publish(processed_message)

if __name__ == '__main__':
    # Initialize the ROS node with a unique name
    rospy.init_node('your_publisher_node')

    # Create a publisher on the 'processed_topic' topic with String messages
    pub = rospy.Publisher('processed_topic', String, queue_size=10)

    # Subscribe to the 'original_topic' topic and type message then call callback
    rospy.Subscriber('original_topic', String, subscriber_callback)

    # Spin to keep the node alive and process incoming data
    rospy.spin()