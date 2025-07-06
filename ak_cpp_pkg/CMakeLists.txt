cmake_minimum_required(VERSION 3.8)
project(ak_cpp_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED)
find_package(ak_robot_interfaces REQUIRED)

add_executable(robot2_news_station src/robot2_news_station.cpp)
ament_target_dependencies(robot2_news_station rclcpp example_interfaces)

add_executable(smartphone2 src/smartphone2.cpp)
ament_target_dependencies(smartphone2 rclcpp example_interfaces)

add_executable(add_two_int_server src/add_two_int_server.cpp)
ament_target_dependencies(add_two_int_server rclcpp example_interfaces)

add_executable(add_two_ints_client_no_oop src/add_two_ints_client_no_oop.cpp)
ament_target_dependencies(add_two_ints_client_no_oop rclcpp example_interfaces)

add_executable(add_two_ints_client src/add_two_ints_client.cpp)
ament_target_dependencies(add_two_ints_client rclcpp example_interfaces)

add_executable(hw_status_publisher src/hardware_status_publisher.cpp)
ament_target_dependencies(hw_status_publisher rclcpp ak_robot_interfaces)

install(TARGETS
  robot2_news_station
  smartphone2
  add_two_int_server
  add_two_ints_client_no_oop
  add_two_ints_client
  hw_status_publisher
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()