//this file is an early revision of integrating a board communication system between the itsy bitsy and the arduino
//We used this and other cpp files to concurrently test dances while we worked on other parts of the project
#include "moon_walk.h"
//#include "board_commication.h"
#include "general_servo.h"
#include "PinAssignments.h"
#include "Libraries.h"


void setup() {
  walk_setup();
  board_communication_setup();

  

}

void loop() {
 int song = board_commncation();
 if(song == 1){
   moon_walk();
 }
 
 
    
}
