"""
Victor Velazquez, Ros Node Template Python 

This template is for a full service server node that subscribes to another node and also publishes

make code excecutable: chmod +x scripts/name_server_node.py

add to CMakeLists.txt:
catkin_install_python(PROGRAMS scripts/name_server_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

"""

#!/usr/bin/env python

import rospy
from your_package.srv import YourServiceType, YourServiceResponse  # Replace with your service and response message types
from std_msgs.msg import YourInputMessageType, YourOutputMessageType  # Replace with your topic message types

def service_callback(req):
    # This function is called when a service client makes a request
    # Process the request and generate a response
    response = YourServiceResponse()

    # Perform the desired service logic here
    response.result = process_request(req)

    return response

def process_request(request):
    # Add your service logic here based on the request data
    # You can access request fields like request.field_name
    # Return the result based on your processing logic
    #
    #...process...
    #
    result = request  # Replace with your processing logic
    return result


def topic_input_callback(data):
    # This function is called whenever new data is received from the subscribed topic
    # Process the topic data as needed
    processed_data = process_topic_data(data)
    publish_to_topic(processed_data)

def process_topic_data(data):
    # Add your topic data processing logic here
    # You can access various fields of the topic message using data.field_name
    # Return the processed data
    processed_data = data  # Replace with your processing logic
    return processed_data

def publish_to_topic(data):
    #use this function whether in the server response, or in the input data

    # Publish the processed data on another topic

    #...process date before publishing

    processed_data = data

    pub.publish(processed_data)

if __name__ == '__main__':
    # Initialize the ROS node with a unique name
    rospy.init_node('service_server_and_topics_node_nanme')

    # Create a ROS service server (replace 'your_service_name' with the actual service name)
    rospy.Service('your_service_name', YourServiceType, service_callback)

    # Subscribe to the 'input_topic' topic (replace 'input_topic' with your actual input topic name)
    rospy.Subscriber('input_topic', YourInputMessageType, topic_input_callback)

    # Create a publisher for the 'output_topic' topic (replace 'output_topic' with your actual output topic name)
    pub = rospy.Publisher('output_topic', YourOutputMessageType, queue_size=10)

    rospy.loginfo("Service server is ready to receive requests and subscribe/publish topics.")

    # Spin to keep the node alive and handle incoming service requests and topic messages
    rospy.spin()
