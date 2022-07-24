//This file contains functions related to the keypad. It is unfinished as we never ended up using it 
#include "PinAssignments.h"
#include "Libraries.h"


void board_communication_setup() {
  pinMode(INPUT,BINARY_IN_1);
  pinMode(INPUT,BINARY_IN_2);
  pinMode(INPUT,BINARY_IN_3);
}


int board_communication(){
  int song;
  bool binary[3] = {digitalRead(BINARY_IN_1) , digitalRead(BINARY_IN_2), digitalRead(BINARY_IN_3)}; 
  switch(binary){
    
  }
  
  return song;
}
