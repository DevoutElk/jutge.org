#Storytelling
# X53748
# 'https://jutge.org/problems/X53748_en'

name = input("")
age = input("")
gender = input("")
city = input("")
favourite_sport = input("")
favourite_team = input("")
ideal_job = input("")
if gender == "girl":
    pronoun = ("she")
    possesiver_pronoun = ("her")
else:
    pronoun = ("he")
    possesiver_pronoun = ("his")
print(name,"is a",age,"year-old",gender+".",pronoun.capitalize(),"is living with",possesiver_pronoun,"parents in an apartment in the centre of",city+", where",pronoun,"hangs out with",possesiver_pronoun,"friends. Moreover, in",possesiver_pronoun,"free time",pronoun,"plays",favourite_sport,"in a team called",favourite_team+".",name,"would like to pursue a career in",ideal_job,"when",pronoun,"is older, that's why",pronoun,"is studying hard.")