#include <stdio.h>
#include <string.h>
//
// Created by georgie's pc (thicc) on 07/09/2020.
//

char* find_motif(char full[], char sub[]){
    int i=0;
    int locations[1000];
    while ( i< strlen(full)){
        int j=0;

        while( j< strlen(sub)){
            if(full[i+j]==sub[j] && i + j <= strlen(full)){
                j++;
                if(full[i+j+1]==sub[j+1]){

                }
                continue;
            } else{
                break;
            }

        }
        i++;

    }

}