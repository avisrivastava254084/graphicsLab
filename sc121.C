#include <graphics.h>
#include <stdlib.h>
#include <stdio.h>
#include <conio.h>
#include<math.h>
void main()
{
            int gm;
            int gd=DETECT;
            int x[10],y[10],nx[10],ny[10];
            int sx,sy,xt,yt,r,n,i,j,k,l;
            float t;
            initgraph(&gd,&gm,"C:\TC\BGI:");
            printf("\t Screen-saver with basic transformations");
            printf("Enter the no. of co-ordinates of your polygon :");
            scanf("%d", &n);
            for(i=0;i<n'i++) {
            setcolor(1);
            printf("X[%d]:  Y[%d]:",i,i);
            scanf("%d  %d",&x[i],&y[i]);
            line(x[i],y[i],x[i+1],y[i+1]);
            getch();
            }
            printf("\n 1.Translation\n 2.Rotation\n 3.Scaling\n 4.exit");
            printf("Enter your choice:");
            scanf("%d",&c);
            switch(c)
            {
                        case 1:
                                    printf("\n Enter the translation factor");
                                    scanf("%d%d",&xt,&yt);
                                    
                                    for(j=0;j<n;j++) {
                                    nx[i]=x[j]+xt;
                                    ny[i]=y[j]+yt;
                                    line(nx[j],ny[j],nx[j+1],ny[j+1]);
                                    getch();
                                    }
                        case 2:
                                    printf("\n Enter the angle of rotation");
                                    scanf("%d",&r);
                                    t=3.14*r/180;
                                    for(k=0;k<n;k++) {
                                    nx[k]=abs(x[k]*cos(t)-y[k]*sin(t));
                                    ny[k]=abs(x[k]*sin(t)+y[k]*cos(t));
                                    line(nx[k],ny[k],nx[k+1],ny[k+1]);
                                    getch();
                                    }
                        case 3:
                                    printf("\n Enter the scalling factor");
                                    scanf("%d%d",&sx,&sy);
                                    for(l=0;l<n;l++) {
                                    nx[l]=x[l]*sx;
                                    ny[l]=y[l]*sy;
                                    line(nx[l],ny[l],nx[l+1],ny[l+1]);
                                    getch();
                                    }
                        case 4:
                                    break;
                        default:
                                    printf("Enter the correct choice");
                                    }
                                    closegraph();
                                    }
