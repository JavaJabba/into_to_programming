# ScriptName:       revision_functions.py
# Author:           Dylan Murray 121747725


from turtle import width

def calcWindChillIndex(windSpeed:float, airTemp:float):
    '''
    Read in input air temperature and wind speed, then calculate wind chill index.
    '''

    wci = 3.12 + 0.6215(airTemp) - 11.37(windSpeed ** 0.16) + 0.3965(airTemp * (windSpeed ** 0.16))
    return "Wind Chill is currently" , wci