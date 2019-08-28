'''
Lab 24: Rain Data
    The 'City of Portland Bureau of Environmental Services' operates and maintains a network of rain gauges around Portland, and publishes their data publicly: http://or.water.usgs.gov/non-usgs/bes/

    The data tables available on the site look something like...

        Daily  Hourly data -->

        Date     Total    0   1
        --------------------------
        25-MAR-2016     0    0   0
        24-MAR-2016     6    0   1
        23-MAR-2016     -    -   -
        MORE...

    Download one of these files and write a function to load the file. The two columns that are most important are the date and the daily total. The simplest representation of this data is a list of tuples, but you may also use a list of dictionaries, or a list of instances of a custom class.

    To parse the dates, use datetime.strptime. This allows for easy access to the year, month, and day as ints. Below I've shown how to parse an example string, resulting in a datetime object. We can then access the year, month, and day on that datetime as ints. Later, if you want to print the datetime in a more human-readable format, you can use datetime.strftime.

        import datetime
        date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
        print(date.year)   # 2016
        print(date.month)  # 3
        print(date.day)    # 25
        print(date)  # 2016-03-25 00:00:00
        print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016

Version 2:
    Now that you've successfully extracted the data, let's done some statistics.

Version 3:
    Using matplotlib create a chart of the dates and the daily totals for a given year. The x_values will be a list of dates, The y_values are a list of the daily totals. If you don't have matplotlib installed, run pip install matplotlib. You can learn more about matplotlib here.
        import matplotlib.pyplot as plt
        ...
        plt.plot(x_values, y_values)
        plt.show()
        Some charts you can make are:
    all the data, date vs daily total
    monthly totals, average across multiple years
    total yearly rainfall, year by year
'''

import datetime

print('Welcome to Lab 24: Rain Data. A program coded in python by Caleb Mealey.')
print('In this lab, we will open the \'Harney Rain Gage\' file from the City of Portland, extract the data and display the mean and plot it using mathplot')
print('Data are the number of tips of the rain gage bucket. Each tip is 0.01 inches of rainfall. Dates and times are PACIFIC STANDARD TIME.')
print('In order to begin reading, manipulating, and more, we will open it...')
print('We will open \'harney_pump_gage.csv\' now.')

with open('./assets/harney_pump_gage.csv', 'r') as file:
            lines = file.read().split('\n')
            # print(lines)
            data = []
            header_row = []
            header_row = lines[6].split(',')
            print(header_row)
            lines = lines[7:]
            avg_sum = 0
            most_rainy_day = ['default', 0]
            first_date_and_last_date = ['','']
            yearly_totals_dic = {}
            for i in range(len(lines)-1):
                row = lines[i].split(',')
                for y in row:
                    date = datetime.datetime.strptime(f'{row[0]}', "%d-%b-%Y")
                    row[0]= date.strftime('%d-%b-%Y')
                    # if date.year in yearly_totals_dic.keys():
                    #     yearly_totals_dic[date.year['sum:']] += row[1]
                    # else:
                    #     yearly_totals_dic[date.year] = [('year:', date.year), ('sum:', row[1])]
                if int(row[1]) > most_rainy_day[1]:
                    most_rainy_day[0] = row[0]
                    most_rainy_day[1] = int(row[1])
                row[1] = int(row[1])
                row = tuple(row)
                data.append(row)
                avg_sum += row[1]
            first_date_and_last_date = [data[0][0], data[-1][0]]
            
            mean = (1 / len(data))*(avg_sum)
            print(f'The daily mean between {first_date_and_last_date[0]} and {first_date_and_last_date[1]} is: {mean} tips of the rain gage bucket.')
            print(f'Each tip is 0.01 inches of rainfall. So the average amount of rainfall at this gage was: {(mean * 0.01)} inches of rainfall per each 24 hours.')
            print(f'The most rainy day of the year was: {most_rainy_day[0]} with {most_rainy_day[1]} tips of the bucket, or {(most_rainy_day[1]*0.01)} inches of rain.')

            var_sum = 0
            print(data)
            for x in range(len(data)):
                var_x = data[x][1]- mean
                var_x = var_x**2
                var_sum += var_x
            variance = var_sum / len(data)
            print(f'The variance we calculated from the mean was: {variance}')

            print(f'The square deviation is: {(variance**0.5)}')

            # print(yearly_totals_dic)