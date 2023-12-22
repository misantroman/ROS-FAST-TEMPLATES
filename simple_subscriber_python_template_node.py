#!/usr/bin/env python

"""
Victor Velazquez, Ros Node Template Python 

This template is for a node that subscribes to a topic, process data

"""


import rospy
from sensor_msgs.msg import YourSensorMessageType  # Replace with the actual message type

def sensor_callback(data):
    # This function is called whenever new data is received from the sensor topic
    # Process the sensor data as needed
    processed_data = process_sensor_data(data)

    # Perform your desired processing on the data here

def process_sensor_data(data):
    # Add your sensor data processing logic here
    # You can access various fields of the sensor message using data.field_name
    # For example, if it's a LaserScan message, you can access data.ranges, data.angle_min
    # Return the processed data
    processed_data = data  # Replace with your processing logic
    #
    #process data and finally return it
    #
    return processed_data

if __name__ == '__main__':
    # Initialize the ROS node with a unique name
    rospy.init_node('sensor_subscriber_node')

    # Subscribe to the sensor topic (replace 'sensor_topic' with your actual topic name)
    rospy.Subscriber('sensor_topic', YourSensorMessageType, sensor_callback)

    # Spin to keep the node alive and process incoming sensor data
    rospy.spin()