#!/usr/bin/env python


from udm_group2_gb.srv import *
import rospy
import rosservice

def handle_req(req):
    c=req.a.data
    rosservice.call_service('/global_localization',True)
    for x in range(c):	
    	rosservice.call_service('/request_nomotion_update',True)

    rep=udm_serviceResponse()
    rep.c.data=c
    rep.res.data=True
    return rep
def simple_server():
    rospy.init_node('simple_service_server')
    s = rospy.Service('simple_Service', udm_service, handle_req)
    rospy.spin()

if __name__ == "__main__":
    simple_server() 
