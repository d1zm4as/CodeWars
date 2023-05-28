/*
def human_years_cat_years_dog_years(human_years):
    catYears = 0
    dogYears = 0
    if human_years == 1:
        catYears += 15
        dogYears += 15
        return [human_years, catYears, dogYears]
    elif human_years == 2:
        catYears += 24
        dogYears += 24
        return [human_years, catYears, dogYears]
    elif human_years > 2:
        catYears += 24
        dogYears += 24
        years = human_years - 2
        catYears += years*4
        dogYears += years*5
        return [human_years, catYears, dogYears]
    return [0,0,0]

*/


typedef struct Human_Cat_Dog_Years {
    unsigned human_years, cat_years, dog_years;
} years;

years human_years_cat_years_dog_years(unsigned human) {

    unsigned cat_years = 0;
    unsigned dog_years = 0;
    if(human ==1){
        cat_years+=15;
        dog_years+=15;
        years expected = {human,cat_years,dog_years};
        return expected;
    }
    else if(human==2){
        cat_years+=24;
        dog_years+=24;
        years expected = {human,cat_years,dog_years};
        return expected;
    }
    else if(human>2){
        cat_years+=24;
        dog_years+=24;
        int ano = human-2;
        cat_years+=ano*4;
        dog_years+=ano*5;
        years expected = {human,cat_years,dog_years};
        return expected;
}
    years expected = {0,0,0};
    return expected;
    }
