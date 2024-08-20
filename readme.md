This program takes input file which contains noisy data and give an output file with cleared data with specified format.

## Sample unformatted row(input):
\"TEST_RANDOOM_TEXT\",\"08/15/2024 03:45\",\"0\"
## Sample formated row (output): 
TEST_RANDOOM_TEXT, 08/15/2024 03:45, 0

## Sample CSV File Contains Following Data As Input:
    "\"name\",\"timestamp\",\"value\"\n\"TEST_RANDOOM_TEXT\",\"08/15/2024 03:45\",\"0\"\n\"TEST_RANDOOM_TEXT\",\"08/15/2024 03:45\",\"0\"\n\"TEST_RANDOOM_TEXT\",\"08/15/2024 03:45\",\"0\"\n\"TEST_RANDOOM_TEXT\",\"08/15/2024 03:45\",\"0\"\n\"TEST_RANDOOM_TEXT\",\"08/15/2024 03:45\",\"0\"\n\"TEST_RANDOOM_TEXT\",\"08/15/2024 03:45\",\"0\"\n\"TEST_RANDOOM_TEXT\",\"08/15/2024 03:45\",\"0\"\n\"TEST_RANDOOM_TEXT\",\"08/15/2024 03:45\",\"0\"\n\"TEST_RANDOOM_TEXT\",\"08/15/2024 03:45\",\"1\"\n\"TEST_RANDOOM_TEXT\",\"08/15/2024 03:45\",\"0\"\n\"TEST_RANDOOM_TEXT\",\"08/15/2024 03:50\",\"0\"\n\"TEST_RANDOOM_TEXT\",\"08/15/2024 03:50\",\"0\"\n\"TEST_RANDOOM_TEXT\",\"08/15/2024 03:50\",\"0\"\n\"TEST_RANDOOM_TEXT\",\"08/15/2024 03:50\",\"0\"\n\"TEST_RANDOOM_TEXT\",\"08/15/2024 03:50\",\"0\"\n\"TEST_RANDOOM_TEXT\",\"08/15/2024 03:50\",\"0\"\n\"TEST_RANDOOM_TEXT\",\"08/15/2024 03:50\",\"0\"\n\"TEST_RANDOOM_TEXT\",\"08/15/2024 03:50\",\"0\"\n\"TEST_RANDOOM_TEXT\",\"08/15/2024 03:50\",\"1\"\n\"TEST_RANDOOM_TEXT\",\"08/15/2024 03:50\",\"0\"\n\"TEST_RANDOOM_TEXT\",\"08/15/2024 03:55\",\"0\"\n\"TEST_RANDOOM_TEXT\",\"08/15/2024 03:55\",\"0\"\n\"TEST_RANDOOM_TEXT\",\"08/15/2024 03:55\",\"0\"\n\"TEST_RANDOOM_TEXT\",\"08/15/2024 03:55\",\"0\"


## Sample CSV File Contains Following Data As Output:
    TEST_RANDOOM_TEXT, 08/15/2024 03:45, 0
    TEST_RANDOOM_TEXT, 08/15/2024 03:45, 0
    TEST_RANDOOM_TEXT, 08/15/2024 03:45, 0
    TEST_RANDOOM_TEXT, 08/15/2024 03:45, 0
    TEST_RANDOOM_TEXT, 08/15/2024 03:45, 0
    TEST_RANDOOM_TEXT, 08/15/2024 03:45, 0
    TEST_RANDOOM_TEXT, 08/15/2024 03:45, 0
    TEST_RANDOOM_TEXT, 08/15/2024 03:45, 0
    TEST_RANDOOM_TEXT, 08/15/2024 03:45, 1
    TEST_RANDOOM_TEXT, 08/15/2024 03:45, 0
    TEST_RANDOOM_TEXT, 08/15/2024 03:50, 0
    TEST_RANDOOM_TEXT, 08/15/2024 03:50, 0
    TEST_RANDOOM_TEXT, 08/15/2024 03:50, 0
    TEST_RANDOOM_TEXT, 08/15/2024 03:50, 0
    TEST_RANDOOM_TEXT, 08/15/2024 03:50, 0
    TEST_RANDOOM_TEXT, 08/15/2024 03:50, 0
    TEST_RANDOOM_TEXT, 08/15/2024 03:50, 0
    TEST_RANDOOM_TEXT, 08/15/2024 03:50, 0
    TEST_RANDOOM_TEXT, 08/15/2024 03:50, 1
    TEST_RANDOOM_TEXT, 08/15/2024 03:50, 0
    TEST_RANDOOM_TEXT, 08/15/2024 03:55, 0
    TEST_RANDOOM_TEXT, 08/15/2024 03:55, 0
    TEST_RANDOOM_TEXT, 08/15/2024 03:55, 0
    TEST_RANDOOM_TEXT, 08/15/2024 03:55, 0

<hr /> 

## Input File:
Program accepts any file with csv file extension. It reads all csv files on the local folder automatically.
## Output File:
\* symbol represents the sequential number(1,2,3... etc.) afterthat csv_data*.csv is sample output file. <br />
Note: program select missing numbers to use on numbering. For example we have following files in the output folder: <br />
csv_data1.csv <br />
csv_data3.csv <br />
In this case program produces csv_data2.csv file and keeps producing as csv_data4.csv, csv_data5.csv... 

<hr /> 

## Config:
Data Import Location: Local Folder <br />
Data Export Location: C:\CSV_Import\Dataparc_Import

<hr /> 

## Warning:
Data file must start with: <br />
 "\"name\",\"timestamp\",\"value\"\n\"KPS09E01_viscosity100\",\"08/15/2024 03:45\",\"0\"\n\"KPS09E01_remaining_oil_life\....." <br />
Because of program deletes titles(it deletes till first '\n' char) if the file has different beginning, program will delete these datas.

<hr /> 

## Notes:
Program produces error_log file if an error occured. It writes error to the file with timestamp.
