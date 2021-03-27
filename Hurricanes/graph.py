import matplotlib.pyplot as plt
import pandas as pd 
from dateutil import parser
from datetime import datetime
from datetime import date
"""
x = [1, 2, 3]
y = [4, 5, 6]

plt.plot(x, y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Title')
plt.show()
"""
# https://wikitable2csv.ggor.de/ for data conversion
#https://stackoverflow.com/questions/1574088/plotting-time-in-python-with-matplotlib @later

LOWER_BOUND_YEAR = 1850
UPPER_BOUND_YEAR = 2020

def find_year_as_obj(str_date):
    streak = 0
    first_idx = 0
    on_streak = False
    for i in range(0, len(str_date)):
        if str_date[i].isdigit():
            if on_streak:
                streak += 1
                if streak == 4:
                    str_year = str_date[first_idx : first_idx + 4]
                    datetime_year = date(int(str_year), 1, 1)
                    return datetime_year
            else:
                on_streak = True
                streak = 1
                first_idx = i
        else:
            on_streak = False
            streak = 0
    return None


def get_data(direc):
    full_data = []
    for i in range(1, 6):
        cat_data = {}
        if i == 4: #@todo delete
            full_data.append([])
            continue 
        df = pd.read_csv(direc + '/cat' + str(i) + '.csv')
        date_time_data = []
        for index, row in df.iterrows():
            str_time = row['Dates as a Category ' + str(i)]
            if '–' in str_time: 
                str_time = str_time[0:str_time.index('–')] + str_time[str_time.index(','):]
            elif '—' in str_time:
                str_time = str_time[0:str_time.index('—')] + str_time[str_time.index(','):]
            try:
                datetime_object = parser.parse(str_time) #https://stackoverflow.com/questions/466345/converting-string-into-datetime
            except:

                datetime_object = find_year_as_obj(str_time)
                if datetime_object == None:
                    continue
             
            date_time_data.append(datetime_object)   
        for date_time in date_time_data:
            year = date_time.year
            if year in cat_data:
                cat_data[year] += 1
            else:
                cat_data[year] = 1

        year_values_array = []
        
        for year in range(LOWER_BOUND_YEAR, UPPER_BOUND_YEAR + 1):
            if year not in cat_data:
                year_values_array.append(0)
            else:
                year_values_array.append(cat_data[year])
        full_data.append(year_values_array)
        """
        for point in cat_data:
            tuple_cat_data.append((point, cat_data[point]))
        full_data.append(tuple_cat_data)
        """

    return full_data    


def graph_data(data):
    plt.figure()
    plt.plot(data[0], color='green')
    plt.plot(data[1], color='purple')
    plt.plot(data[2], color='brown')
    #plt.plot(data[3], color='red') @todo actually do cat 4 parsing
    plt.plot(data[3], color='blue')

    plt.show()
    dA = 0
    


if __name__ == "__main__":
    data = get_data('Hurricanes/Data')
    graph_data(data)