import csv
import re
import os
import time
import datetime

program_cycle_counter = 1 
output_folder = 'C:\\CSV_Import\\Dataparc_Import' 

# creates the folder of data output files if its not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#this method returns a number that doesn't exist in the csv file list which is used numbering files
def unique_number_selector():
    i = 0
    i_is_unique = False
    csv_files = [f for f in os.listdir('C:\CSV_Import\Dataparc_Import') if f.endswith('.csv')]

    for file_name in csv_files:
        if(file_name[-5:-4] != str(i)):
            i_is_unique = True
        else:
            i_is_unique = False
            i += 1
    return i


def process_csv(file_name_param):   
    # reading data
    with open(file_name_param, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data_holder = row
    try:
        file_string = ""
        for i in data_holder:
            file_string += i

        data_list = file_string.split("\\n")

        # removing title data
        data_list.pop(0)
        data_list.pop(0)

        clean_data = []

        # regex statment to select specific data
        pattern = r'\\"(.*)\\"\\"(.*)\\"\\"(.*)\\"'

        # split the data by regex statment
        i = 0
        while i < len(data_list):
            match = re.match(pattern, data_list[i])

            if match:
                acu_list = [match.group(1), match.group(2), match.group(3)]
                clean_data.append(acu_list)
            i += 1

        global file_number
        file_number = unique_number_selector() 

        # prints the clean data
        with open(f"{output_folder}\\csv_data{file_number}.csv", "w") as output_file:
            for item in clean_data:
                acu_string = ""
                for value in item:
                    acu_string += value + ", "
                output_file.write(acu_string.strip().strip(',') + "\n")

    except Exception as error:
        with open('error_log.txt', 'a') as error_log_file:
            #the text must be str so the data converted to str
            error_log_file.write(str(error) + '\t' + str(datetime.datetime.now()) + '\n')


# main program
while True:
    # reads all local csv files
    csv_files = [f for f in os.listdir() if f.endswith('.csv')]

    # processes all csv files
    for csv_file in csv_files:
        process_csv(csv_file)
        #remove used csv import file
        os.remove(csv_file)

    #clearing CLI 
    os.system('cls')

    # prints some information about running (aka live-log)    
    print(f"Program has executed {program_cycle_counter} times.\nExecutation Time: {datetime.datetime.now()}\n")

    program_cycle_counter += 1
    
    # 30 seconds delay
    time.sleep(30) 
