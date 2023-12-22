"""
Victor Velazquez, Ros Node Template Python 

This template is for a service server node

make code excecutable: chmod +x scripts/name_server_node.py

add to CMakeLists.txt:
catkin_install_python(PROGRAMS scripts/name_server_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

"""


#!/usr/bin/env python

import rospy
from your_package.srv import YourServiceType, YourServiceResponse  # Replace with your service and response message types

def handle_request(req):
    # This function is called when a service client makes a request
    # Process the request and generate a response

    #create empty instance of response message
    response = YourServiceResponse()
    
    # Perform the desired service logic inside process request 
    response.result = process_request(req)

    return response  #returns instance of YourServiceResponse

def process_request(request):
    # Add your service logic here based on the request data
    # You can access request fields like request.field_name
    # Return the result based on your processing logic
    #
    #...process...
    #
    result = request  # Replace with your processing logic
    return result

if __name__ == '__main__':
    # Initialize the ROS node with a unique name
    rospy.init_node('service_server_node_name')

    # Create a ROS service server (replace 'your_service_name' with the actual service name) , all request pass to handle_request
    rospy.Service('your_service_name', YourServiceType, handle_request)

    rospy.loginfo("Service server is ready to receive requests.")

    # Spin to keep the node alive and handle incoming service requests
    rospy.spin()
