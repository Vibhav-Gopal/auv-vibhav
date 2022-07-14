cmake_minimum_required(VERSION 3.0.2)
project(chatting)


find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)


catkin_package(CATKIN_DEPENDS roscpp rospy std_msgs)
include_directories(${catkin_INCLUDE_DIRS})



add_executable(chattera src/chattera.cpp)
add_executable(readera src/readera.cpp)
add_executable(chatterb src/chatterb.cpp)
add_executable(readerb src/readerb.cpp)
target_link_libraries(chattera ${catkin_LIBRARIES})
target_link_libraries(readera ${catkin_LIBRARIES})
target_link_libraries(chatterb ${catkin_LIBRARIES})
target_link_libraries(readerb ${catkin_LIBRARIES})

