
from random import randint

class Life:
    CHANGEOPTIONS = [ "car", "job", "house", "spouse" ]

    @staticmethod
    def GetChange():
        result = 'No change'
        if ( randint(1, round(365.25 * 3)) == 1):
            result = Life.CHANGEOPTIONS[ randint(0, len(Life.CHANGEOPTIONS) - 1)]
        return result

print("Today's suggested change: {}".format(Life.GetChange()))
