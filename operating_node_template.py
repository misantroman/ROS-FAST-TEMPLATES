#!/usr/bin/env python

#IMPORT NECESSARY LIBRARIES

import numpy
import rospy

#IMPORT NECESSARY MESSAGES 

from visualization_msgs.msg import Marker #Included for RVIZ marker
from geometry_msgs.msg import Point #Included for RVIZ marker
from enum import Enum

#IMPORT NECESSARY FUNCTIONS/CLASSES

from subdron_object_detect import *


##Import actual processing class
#from subdron_objective_name.ProcessingNameClass import ProcessingName
from ProcessingNameClass.ProcessingNameClass import ProcessingName

from subdron_python_template.msg import node_topic_custom_message
from subdron_python_template.msg import StatusMsgTemplate
from subdron_python_template.msg import PublishTopicMessageType
from subdron_python_template.msg import SubscribeTopicMessageType


#from subdron_other_pkg import PublishTopicMessageType
#from subdron_other_pkg import SubscribeTopicMessageType


#IMPORT NECESSARY SERVICES, SERVICE_TYPE, SERVICE_RESPONSE

from std_srvs.srv import Trigger, TriggerResponse


class ProcessingNameNode(object):
    def __init__(self):
        self.namespace = rospy.get_namespace()[1:-1]
        #Constructor
        rospy.loginfo('node name starting ...')

        #variable initialization
        self.object_name_processing_class = ProcessingName()  #this is for example estimator class
        self.this_node_status = StatusMsgTemplate.STANDBY     #initialize and store the current status of the node   STANDBY is 1
        self.enable_service_flag = False                      #node waits to be enabled to perform

        self.object_name_processing_class.variable_1 = 1
        self.object_name_processing_class.variable_2 = 2


        ##import params
        self.param_1 = rospy.get_param(rospy.get_namespace() + "param_name_1")
        self.param_2 = rospy.get_param(rospy.get_namespace() + "param_name_2")        

        #create msg
        self.node_status_msg = StatusMsgTemplate()
        self.msg_to_publish = PublishTopicMessageType()

        #create publishers
        self.pub_node_status = rospy.Publisher("subdron_node_name/node_status_topic", StatusMsgTemplate, queue_size=1)
        self.pub_custom = rospy.Publisher("subdron_node_name/custom_topic", PublishTopicMessageType, queue_size = 1)


        #create subscribers
        self.subs_template = rospy.Subscriber(rospy.get_namespace() + "subdron_node_name/topic_to_subscribe_name",  SubscribeTopicMessageType, self.custom_callback, queue_size = 1)

        #services
        self.enable_srv = rospy.Service("~enable", Trigger, self.srv_enable)   #the ~ makes the ns .namespace?
        self.disable_srv = rospy.Service("~disable", Trigger, self.srv_disable)

        rospy.loginfo("node initialized")

    ##########################
    #        Services        #
    ##########################
    def srv_enable(self, req):
        res = TriggerResponse()
        res.success = True
        res.message = "Enable service called"        
        self.enable_service_flag = True
        self.this_node_status = StatusMsgTemplate.ACTIVE   # WAITING is 2  ACTIVE is 3
        rospy.loginfo ("service enabled")
        rospy.loginfo (self.this_node_status)
        return res

    def srv_disable(self, req):
        res = TriggerResponse()
        res.success = True
        res.message = "Disable service called"

        #Calling disable goes to STANDBY state
        self.this_node_status = StatusMsgTemplate.STANDBY
        rospy.loginfo (self.this_node_status)
        rospy.loginfo ("service disabled")
        self.enable_service_flag = False

        return res




    ##########################
    #        Publishers      #
    ##########################
    def publisher_node_status(self):
        #Status of the node shall be published always
        self.node_status_msg.header.stamp = rospy.Time.now()
        #rospy.loginfo ("publish status")
        self.node_status_msg.state = self.this_node_status
        self.pub_node_status.publish(self.node_status_msg)

    def publisher_custom(self):
        #works 2 if fine
        rospy.loginfo ("custom publisher")
        #setup all the variables of self.msg you want to publish
        self.msg_to_publish.header.stamp = rospy.Time.now()
        self.msg_to_publish.works = self.object_name_processing_class.variable_2
        self.pub_custom.publish(self.msg_to_publish)


    ##########################
    #        Callbacks      #
    ##########################

    def custom_callback(self, msg):
        rospy.loginfo ("subscriber callback")

        self.publisher_custom()
        if self.enable_service_flag:
            if msg:

                #Processing with the funcitions of the parent class
                self.custom_function_2()

                #Extra publishing
                self.publisher_custom()

            else:
                self.error_state()

    ##########################
    #        Functions      #
    ##########################

   # Function that runs the estimations and publishes de results 
    def run(self):
        #self.custom_function()
        self.publisher_node_status() #always publish the node state when running

        if self.this_node_status == StatusMsgTemplate.ACTIVE:
            self.publisher_custom() #publish the relavante statistics when we are receiving


    #Function to run 
    def custom_function(self):

        #Here you can call functions of the actual implementation of the procedure, of the object
        rospy.loginfo ("custom func")
        #self.object_name_processing_class.functionOne()
        #self.object_name_processing_class.functionTwo()
        #self.this_node_status = StatusMsgTemplate.ACTIVE

    def custom_function_2(self):

        ##processing
        self.this_node_status = StatusMsgTemplate.ACTIVE

    def error_state(self):
        self.this_node_status = StatusMsgTemplate.ERROR
        self.enable_service_flag = False
        rospy.loginfo ("Error... probably no mssge")

if __name__ == '__main__':
    # init ROS node
    rospy.init_node('subdron_node_name')
    # start node
    node = ProcessingNameNode()

    rate = rospy.Rate(10) #10Hz
    while not rospy.is_shutdown():
        node.run()
        rate.sleep()