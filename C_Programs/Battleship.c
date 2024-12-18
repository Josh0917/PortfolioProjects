/*
  Synopsis: Playing Battleship
  Author: Josh J
  Date:
*/
#include <stdio.h>
#define X 5
#define Y 5


//Function prototype
char printGrid(char row[X][Y], size_t one, size_t two);


//main
int main(void){

//Variables
char guess[X][Y];


char row[X][Y] =
{
 {'-','-','-','-','-'},
 {'-','-','-','-','-'},
 {'-','-','-','-','-'},
 {'-','-','-','-','-'},
 {'-','-','-','-','-'}
};

printGrid(row, X, Y);

printf("Player One place your ships");

//scanf("",);

return 0;
}

//Functions
char printGrid(char row[X][Y], size_t one, size_t two){
  for(int i = 0; i < one; i++){
    for(int j = 0; j < two; j++){
      printf("-");
    }
    printf("\n");
  }
}
