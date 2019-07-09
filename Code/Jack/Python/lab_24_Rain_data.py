import datetime


def make_it_rain(filename):
    l_rain = []
    with open(filename) as file:
        rain = file.read().split('\n')
    rain = rain[11:]
    for i, line in enumerate(rain):
        rain[i] = line.split()
        daily_average = int(rain[i][1])/24
    avg = sum(daily_average)
    for line in rain:
        var_sum += (((int(line[1]))/24) - avg)**2
    var_sum /= len(rain) - 1
    l_rain.append(datetime.datetime.strptime(rain[0], '%d-%b-%Y'), var_sum)
    return l_rain


rain = make_it_rain('./Resources/rain.txt')
print('-'*60)
print(rain)
