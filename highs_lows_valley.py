import csv
from datetime import datetime
from matplotlib import pyplot as plt

#obtem as temperaturas maximas e minimas do arquivo
filename = 'highs-lows/death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
        
        #print(highs)

#faz a plotagem dos dados
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


#formata o grafico
title = 'Temperaturas altas e baixas diárias - 2014\nVale da Morte, CA'
plt.title(title, fontsize=20)
fig.autofmt_xdate()
plt.ylabel('Temparatura (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()