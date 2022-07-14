#include <ros/ros.h>
#include <std_msgs/String.h>
#include <sstream>
#include <iostream>
#include <cstdio>
#include  <bits/stdc++.h>
#include <string>
void chatterCallback(const std_msgs::String::ConstPtr& msg){
	//ROS_INFO_STREAM("I heard: " << msg->data.c_str());
    std::cout<<"A says: "<<(msg->data.c_str());
    std::cout<<"\n";
    
}
int main(int argc, char **argv){

	ros::init(argc, argv, "readera");


	ros::NodeHandle nr;

	ros::Subscriber sub = nr.subscribe("chattera", 1000, chatterCallback);

	ros::spin();

	return 0;
}