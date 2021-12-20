#include <stdio.h>
#include <stdlib.h>
#include <ros/ros.h>

int main (int argc,char **argv)
{
         ros::init(argc,argv,"C2a");
         ros::NodeHandle nh;
         
         printf("%d\n",26) ;
         printf("%d\n",032) ;
         printf("%d\n",0x1A) ;
 
         return 0;
}









