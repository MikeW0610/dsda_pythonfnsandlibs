import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

colour_index = 0;

def get_consumption_for_meterid(meter_id, consumption):
    return consumption[consumption['meter_id'].isin([meter_id])]

def get_reading_times_for_date(date, consumption):
    return [x for x in consumption.columns if(x[0:10]==date)]

def plot_consumption_for_meterid_date(meter_id, date, consumption):
    reading_times = get_reading_times_for_date(date, consumption)
    consumption_for_meterid = get_consumption_for_meterid(meter_id, consumption)
    consumption_for_meterid_filtered = consumption_for_meterid[reading_times]
    
    meter_readings = pd.DataFrame(index = reading_times, columns=["Reading"])
    meter_readings["Reading"] = consumption_for_meterid_filtered.iloc[0,0:len(reading_times)+1].values
    plt.title('Electricity Consumption', fontsize=14)
    plt.xlabel('Time', fontsize=14)
    plt.ylabel('Energy MWh', fontsize=14)
    plt.xticks(np.arange(0, 48, 6), rotation=90)
    plt.plot(reading_times, consumption_for_meterid_filtered.values[0], 'b')
    #plt.savefig('Consumption.jpg', bbox_inches='tight')
    
def remove_date(reading_times):
    return [x[-8:] for x in reading_times]

def choose_colour():
    global colour_index
    ret_colour = list(mcolors.BASE_COLORS)[colour_index%len(mcolors.BASE_COLORS)]
    colour_index=colour_index+1
    return ret_colour
    
def plot_consumption_for_meterid_dates(meter_id, date_list, consumption):
    global colour_index
    # Setup common plot elements
    consumption_for_meterid = get_consumption_for_meterid(meter_id, consumption)
    
    plt.title('Electricity Consumption', fontsize=14)
    plt.xlabel('Time', fontsize=14)
    plt.ylabel('Energy MWh', fontsize=14)
    plt.xticks(np.arange(0, 48, 6), rotation=90)
 
    
    for d in date_list:
        reading_times = get_reading_times_for_date(d, consumption)
        consumption_for_meterid_filtered = consumption_for_meterid[reading_times]
        
        meter_readings = pd.DataFrame(index = remove_date(reading_times), columns=["Reading"])
        meter_readings["Reading"] = consumption_for_meterid_filtered.iloc[0,0:len(reading_times)+1].values
                
        plt.plot(remove_date(reading_times), consumption_for_meterid_filtered.values[0], choose_colour(), label = d)
        
    plt.legend(loc="upper left")
    colour_index=0;
