#include <stdio.h>
#include <string.h>
#include "isotope_check.h"
int main() {
    char prtstr[1000];
    printf("Please enter protein string sequence:");
    scanf("%s",prtstr);
    int x=0;
    double prtmass=0.0;
    while(x != strlen(prtstr)){
        prtmass = prtmass+ get_mass(prtstr[x]);
        x++;
    }
    printf("Total weight = %f", prtmass);
}
