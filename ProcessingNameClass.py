###In this document you implement the actual processing of data####

#Import necessary libraries or functions
import numpy as np
import math
import rospy

#ProcessingName MUST have a name that expresses what the objective of the class is, what you want to obtain

class ProcessingName:
    # Constructor of the ProcessingName Class
    def __init__(self):
        ##Example of initiation of variables
        self.variable_1 = 0  #  
        self.variable_2 = 0  #  

        self.P1 = [0, 0]  # Point 
        self.D = 0        


    ####DEFINE THE FUNCTIONS OF THE CLASS#####


    
    def estimateD(self):
        # 
        #Explanation of the function

        self.D = np.sqrt(self.X*self.X + self.Y*self.Y)

    def functionOne():
        rospy.loginfo ("function one processing file")
        
    def functionTwo():
        rospy.loginfo ("function two processing file")

    
    def setPoint(self):
        # Equation of distance between a point P0 and a line defined by two points P1 and P2
        self.P1 = [self.variable_1, self.variable_2] 


    # Method to set a X vector value of the object
    def setX(self, variable_1):
        self.variable_1 = variable_1

    # Method to set a Y vector value of the object
    def setY(self, variable_2):
        self.variable_2 = variable_2