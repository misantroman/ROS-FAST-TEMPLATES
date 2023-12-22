"""
Victor Velazquez, Ros Node Template Python 

This template is for a service client node

make code excecutable: chmod +x scripts/name_client_node.py

add to CMakeLists.txt:
catkin_install_python(PROGRAMS scripts/name_client_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

catkin_install_python(PROGRAMS scripts/name_server_node.py scripts/name_client_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
"""


#!/usr/bin/env python

import rospy
from your_package.srv import YourService, YourServiceRequest  # Replace with your service and request message types

def service_client():
    # Initialize the ROS node with a unique name
    rospy.init_node('service_client_node_name')

    # Create a ROS service client (replace 'your_service_name' with the actual service name)
    rospy.wait_for_service('your_service_name')  #blocks until the service is available

    try:
        client = rospy.ServiceProxy('your_service_name', YourServiceType) # handle for calling the service

        # Create a request message (replace with your specific request data)
        request = YourServiceRequest()
        request.field_name = "Request Data"  # Customize the request data

        # Call the service and wait for a response
        response = client(request)

        # Process the response data (replace with your processing logic)
        unprocessed_data = response.result

        #...process...

        processed_data = unprocessed_data

        rospy.loginfo("Received response: %s", processed_data)

    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s", e)

if __name__ == '__main__':
    service_client()
