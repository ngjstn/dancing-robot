#define buzzer 10 //buzzer pin

#define com0 2 // communication pins
#define com1 3
#define com2 4

#define rest 0 //notes 
#define C2 65
#define CS2 69
#define D2 73
#define DS2 78
#define E2 82
#define F2 87
#define FS2 93
#define G2 98
#define GS2 104
#define A2 110
#define AS2 117
#define B2 123
#define C3 131
#define CS3 139
#define D3 147
#define DS3 156
#define E3 165
#define F3 175
#define FS3 185
#define G3 196
#define GS3 208
#define A3 220
#define AS3 233
#define B3 247
#define C4 262
#define CS4 277
#define D4 294
#define DS4 311
#define E4 330
#define F4 349
#define FS4 370
#define G4 392
#define GS4 415
#define A4 440
#define AS4 466
#define B4 494
#define C5 523
#define CS5 554
#define D5 587
#define DS5 622
#define E5 659
#define F5 698
#define FS5 741
#define G5 784
#define GS5 831
#define A5 880
#define AS5 932
#define B5 988

void setup() {
  pinMode(buzzer, OUTPUT); //setup buzzers
  pinMode(com0, INPUT); //set up pins for comunication
  pinMode(com1, INPUT);
  pinMode(com2, INPUT);
}

int song = 0; //default song

void loop() {
  if (digitalRead(com0) && digitalRead(com1) && !digitalRead(com2)){ //plays wii sports if the communication pins are set for wii sports
    wiiSports();
  }
  else if (!digitalRead(com0) && !digitalRead(com1) && digitalRead(com2)){ //plays allstar
    allStar();
  }
  else if (digitalRead(com0) && !digitalRead(com1) && digitalRead(com2)){ //plays runningInThe90s
    runningInThe90s();
  }
}

void wiiSports(){ //plays wii sports 
  const short wii_sports[][2] = {{DS4, 967},
                          {E4, 967},
                          {FS4, 362},
                          {B4, 362},
                          {AS4, 241},
                          {B4, 362},
                          {FS4, 362},
                          {DS4, 241},
                          {B3, 362},
                          {CS4, 362},
                          {DS4, 241},
                          {CS4, 1935},
                          {rest, 967},
                          {DS4, 967},
                          {E4, 725},
                          {DS4, 120},
                          {E4, 120},
                          {FS4, 362},
                          {B4, 362},
                          {CS5, 241},
                          {B4, 725},
                          {B4, 120},
                          {CS5, 120},
                          {E5, 362},
                          {DS5, 362},
                          {CS5, 241},
                          {B4, 483},
                          {FS4, 241},
                          {GS4, 483},
                          {CS5, 241},
                          {CS5, 967},
                          {rest, 241},
                          {CS5, 120},
                          {DS5, 120},
                          {E5, 362},
                          {DS5, 362},
                          {CS5, 241},
                          {B4, 483},
                          {FS4, 1875},
                          {rest, 241},
                          {CS5, 120},
                          {DS5, 120},
                          {E5, 362},
                          {DS5, 362},
                          {CS5, 241},
                          {B4, 483},
                          {FS5, 1935},
                          {rest, 483}};
    for (auto &pair : wii_sports) {
      tone(buzzer, pair[0]);
      delay(pair[1]);
      tone(buzzer, rest);
      if (!digitalRead(com0) || !digitalRead(com1) || digitalRead(com2)) {
        break;
      }
    }
}

void allStar() { //plays allstar
  const short all_star[][2] = {{rest, 1730},
                        {FS4, 576},
                        {CS5, 288},
                        {AS4, 288},
                        {AS4, 576},
                        {GS4, 288},
                        {FS4, 288},
                        {FS4, 288},
                        {B4, 576},
                        {AS4, 288},
                        {AS4, 288},
                        {GS4, 288},
                        {GS4, 288},
                        {FS4, 288},
                        {rest, 288},
                        {FS4, 288},
                        {CS5, 288},
                        {AS4, 288},
                        {AS4, 288},
                        {GS4, 288},
                        {GS4, 288},
                        {FS4, 288},
                        {FS4, 288},
                        {DS4, 288}, 
                        {DS4, 288},
                        {CS4, 576},
                        {rest, 865},
                        {FS4, 288},
                        {FS4, 288},
                        {CS5, 288},
                        {AS4, 288},
                        {AS4, 288},
                        {GS4, 288},
                        {GS4, 288},
                        {FS4, 288},
                        {FS4, 288},
                        {B4, 576},
                        {AS4, 288},
                        {AS4, 288},
                        {GS4, 288},
                        {GS4, 288},
                        {FS4, 288},
                        {FS4, 288},
                        {CS5, 288},
                        {rest, 288},
                        {AS4, 288},
                        {AS4, 288},
                        {GS4, 576},
                        {FS4, 288},
                        {FS4, 288},
                        {GS4, 288},
                        {GS4, 288}, 
                        {DS4, 865},
                        {rest, 1153}};
    for (auto &pair : all_star) {
      tone(buzzer, pair[0]);
      delay(pair[1]);
      tone(buzzer, rest);
      if (digitalRead(com0) || digitalRead(com1) || !digitalRead(com2)) {
        break;
      }
    }
}

void runningInThe90s() { //plays running in the 90s
  const short running_in_the_90s[][2] = {{A4, 94},
                                  {E4, 94},
                                  {A4, 94},
                                  {E5, 94},
                                  {D5, 94},
                                  {C5, 94},
                                  {A4, 94},
                                  {rest, 94},
                                  {A4, 94},
                                  {E4, 94},
                                  {A4, 94},
                                  {E5, 94},
                                  {D5, 94},
                                  {C5, 94},
                                  {A4, 94},
                                  {rest, 94},
                                  {C5, 94},
                                  {B4, 94},
                                  {G4, 94},
                                  {C5, 188},
                                  {B4, 94},
                                  {G4, 94},
                                  {rest, 94},
                                  {C5, 94},
                                  {B4, 94},
                                  {G4, 94},
                                  {D5, 188},
                                  {B4, 94},
                                  {G4, 94},
                                  {rest, 94},
                                  {A4, 94},
                                  {E4, 94},
                                  {A4, 94},
                                  {E5, 94},
                                  {D5, 94},
                                  {C5, 94},
                                  {A4, 94},
                                  {rest, 94},
                                  {A4, 94},
                                  {E4, 94},
                                  {A4, 94},
                                  {E5, 94},
                                  {D5, 94},
                                  {C5, 94},
                                  {A4, 94},
                                  {rest, 94}, 
                                  {C5, 94},
                                  {C5, 94},
                                  {rest, 94},
                                  {C5, 94},
                                  {D5, 94},
                                  {rest, 94},
                                  {D5, 94},
                                  {rest, 94},
                                  {E5, 94},
                                  {E5, 94},
                                  {rest, 94},
                                  {E5, 94},
                                  {D5, 94},
                                  {rest, 94},
                                  {D5, 94},
                                  {rest, 94},
                                  {A4, 94},
                                  {E4, 94},
                                  {A4, 94},
                                  {E5, 94},
                                  {D5, 94},
                                  {C5, 94},
                                  {A4, 94},
                                  {rest, 94}, 
                                  {A4, 94},
                                  {E4, 94},
                                  {A4, 94},
                                  {E5, 94},
                                  {D5, 94},
                                  {C5, 94},
                                  {A4, 94},
                                  {rest, 94},
                                  {C5, 94},
                                  {B4, 94},
                                  {G4, 94},
                                  {C5, 188},
                                  {B4, 94},
                                  {G4, 94},
                                  {rest, 94},
                                  {C5, 94},
                                  {B4, 94},
                                  {G4, 94},
                                  {D5, 188},
                                  {B4, 94},
                                  {G4, 94},
                                  {rest, 94},
                                  {A4, 94},
                                  {E4, 94},
                                  {A4, 94},
                                  {E5, 94},
                                  {D5, 94},
                                  {C5, 94},
                                  {A4, 94},
                                  {rest, 94},
                                  {A4, 94},
                                  {E4, 94},
                                  {A4, 94},
                                  {E5, 94},
                                  {D5, 94},
                                  {C5, 94},
                                  {A4, 94},
                                  {rest, 94},
                                  {E5, 188},
                                  {DS5, 188},
                                  {D5, 188},
                                  {CS5, 188},
                                  {C5, 188},
                                  {CS5, 188},
                                  {D5, 188},
                                  {DS5, 188}};
    for (auto &pair : running_in_the_90s) {
      tone(buzzer, pair[0]);
      delay(pair[1]);
      tone(buzzer, rest);
      if (!digitalRead(com0) || digitalRead(com1) || !digitalRead(com2)) {
        break;
      }
    }
}
