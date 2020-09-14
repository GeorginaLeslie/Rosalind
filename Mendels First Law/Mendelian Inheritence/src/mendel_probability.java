public class mendel_probability {
    double k; // number of homozygous dominant factors
    double m; // number of heterozygous factors
    double n; // number of homozygous recessive factors
    double total; // total population

    public mendel_probability(double homozy_dom , double heterozy, double homozy_rec) {
        k = homozy_dom;
        m= heterozy;
        n = homozy_rec;
        total=k+m+n;


    }

    public double dominant_prob_calc(){



        double comp_dominant_prob = ((k/total)*((k-1)/(total-1))) + ((k/total)*(m/(total-1))) + ((k/total)*(n/(total-1))) + ((m/total)*(k/(total-1))) + ((((m/total)*((m-1)/(total-1)))*0.75)) + (((m/total)*(n/(total-1)))*0.5)+
                ((n/total)*(k/(total-1))) +(((n/total)*(m/(total-1)))*0.50);


        double recessive_prob = ((m/total)*(m-1/(total-1)))*0.25 + ((m/total)*(n/(total-1)))*0.5 + ((n/total)*(n-1));

        return comp_dominant_prob;
    }
}
