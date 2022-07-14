#include <ros/ros.h>
#include <std_msgs/String.h>
#include <sstream>
#include <iostream>
#include <cstdio>
#include  <bits/stdc++.h>
#include <string>
using namespace std;

int main(int argc, char **argv){
    
    ros::init(argc,argv,"chattera");
    ros::NodeHandle nh;
    ROS_INFO_STREAM("Hello");
    ros::Publisher chatter_pub = nh.advertise<std_msgs::String>("chattera", 1000);
    ros::Rate loop_rate(10);
    cout<<"Chatter has been initiated"<<endl;
    int count = 0;
        while (ros::ok()){
            std_msgs::String msg;
            /*std::stringstream ss;
            ss << "hello world " << count;
            msg.data = ss.str();
            ROS_INFO("%s", msg.data.c_str());*/
            std::string mess;
            std::cout<<"Ready to receive message"<<endl;
            std::getline (std::cin,mess);
            cout<<endl;
            cout<<"\""<<mess<<"\""<<" has been sent"<<endl;
            msg.data = mess;
		chatter_pub.publish(msg);

		ros::spinOnce();

		loop_rate.sleep();
		++count;
	}
    return 0;
}