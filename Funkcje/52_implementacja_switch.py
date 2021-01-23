'''funkcje switch i case są nie dostępne w pythonie
ale wystąpują w wielu innych językach i są w "kanonie" funkcji
i takiej funkcji się nie da zrobić. Ta zmienia nazwę tygodnia na j. francuski.
function(argument){
    switch(argument) {
        case 0:
            return "lundi";
        case 1:
            return "mardi";
        case 2:
            return "mercredi";
        case 3:
            return "jeudi";
        case 4:
            return "vendredi";
        case 5:
            return "samedi";
        case 6:
            return "dimanche";
        default:
            return "! error !";
    };
};
'''

def WeekDayInFrench(dayNumber):

    names = {
        0: 'lundi',
        1: 'mardi',
        2: 'mercredi',
        3: 'jeudi',
        4: 'vendredi',
        5: 'samedi',
        6: 'dimache'
    }
    return names.get(dayNumber,'error')

print(WeekDayInFrench(4))
print(WeekDayInFrench(8))

