#include <stdio.h>
#include <stdlib.h>
#include <graphics.h>
#define MAX 20

void get_line_intersection(int x1, int y1, int x2, int y2){
    int result = null;
    double s1_x = x2 - x1;
    double s1_y = y2 - y1;
    double s2_x = x2 - x1;
    double s2_y = y2 - y1;
    double s = (-s1_y * (x1 - x1) + s1_x * (y1 - y1)) / (-s2_x * s1_y + s1_x * s2_y);
    double t = ( s2_x * (y1 - y1) - s2_y * (x1 - x1)) / (-s2_x * s1_y + s1_x * s2_y);

    if (s >= 0 && s <= 1 && t >= 0 && t <= 1){
        int a0 = x1 + (t * s1_x);
        int b0 = y1 + (t * s1_y);
    }
}


