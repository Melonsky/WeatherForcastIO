from forecastiopy import *
import datetime

fio = ForecastIO.ForecastIO('',
                            units=ForecastIO.ForecastIO.UNITS_SI,
                            lang=ForecastIO.ForecastIO.LANG_POLISH,
                            latitude=45.3561438, longitude=22.8862692)
current = FIOCurrently.FIOCurrently(fio)
daily = FIODaily.FIODaily(fio)
print 'Temperatura:',current.temperature,'C'
print 'Pogoda:', current.summary
print 'Prawd. Opadow:', current.precipProbability
print daily.data[0].keys()
for i in range(0, len(daily.data)):
    time = datetime.datetime.fromtimestamp(int(daily.data[i]["time"])).strftime('%A %Y-%m-%d')
    print time, daily.data[i]["icon"], daily.data[i]["summary"], "Min:", daily.data[i]["temperatureMin"] , "Max:",  daily.data[i]["temperatureMax"]
