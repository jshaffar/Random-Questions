import json

def highest_freq(file_name):
    largest_date = None
    largest_value = None
    with open(file_name, 'r') as f:
        dic = json.load(f)

        for month_key in dic:
            day_dict = dic[month_key]
            for day_pair in day_dict:
                for key in day_pair:
                    if largest_value == None or day_pair[key] >= largest_value:
                        largest_date = month_key + " " + key
                        largest_value = day_pair[key]
    print(largest_date)
    print(largest_value)


def calc_freq(file_name, output_file_name):
    freq = {}

    with open(file_name) as f:
        dic = json.load(f)
        is_starting_year = True
        for year_key in dic:
            year_val = dic[year_key]
            for month_dict in year_val:
                for month_key in month_dict:
                    if month_key not in freq:
                        freq[month_key] = []
                    day_dict = month_dict[month_key]
                    for day_key in day_dict:
                        people = day_dict[day_key]
                        #      if day_key not in freq[month_key]:
                        if is_starting_year:
                            freq[month_key].append({day_key:0})

                        for f in range(0, len(freq[month_key])):
                            if day_key in freq[month_key][f]:
                                freq[month_key][f][day_key] += len(people)
                                break
            is_starting_year = False                        
        
    with open(output_file_name, 'w') as fo:
        json.dump(freq, fo, indent = 4)

        

if __name__ == '__main__':
    file_name = 'Wikipedia-Deaths/Data/deaths.json'
    output_file_name = 'Wikipedia-Deaths/Results/total_deaths.json'
    #calc_freq(file_name, output_file_name)
    highest_freq(output_file_name)