# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 10:07:55 2018

@author: Hrishikesh Pisal
"""

# The so-called CSV (Comma Separated Values) format is the most common 
# import and export format for spreadsheets and databases.
import csv

# Python CSV reader with defaul delimiter
def  simpleReaderExample():
    # file = open('numberdata1.csv', 'r')

    with open('mark.csv', 'r') as fileObject:
        # Return a reader object (iterator) which will iterate over lines 
        # in the given csvfile.
        csv_reader = csv.reader(fileObject) #default delimiter ','
        for row in csv_reader:
            # print(row)  #List
            # print(*row)  #Content of the List
            for field in row:
                print(f"{field:10}",end="")
            print()

# Python CSV reader with different delimiter
def  simpleReaderDelimiter():
   
    with  open('namedata.csv', 'r') as fileObject:
        reader = csv.reader(fileObject, delimiter = '|')
        dash_line = f"\n{'-'*55}"
        for record in reader:
            # print("No. of fields :",len(record))
            print(dash_line)
            for field in record:
                print(f"{field:15}",end="")
    print(dash_line)
            
# Every row that is read is a List
def csvReader():
    
    with open('employeeBD.csv') as input_file:
        csv_reader = csv.reader(input_file)

        for line_count,row in enumerate(csv_reader,start=0): # Row is List
            # print("type of row : ",type(row))
            if line_count == 0:
                # print(type(row))
                print(f'Column names are {", ".join(row)}')
            else:
                print(f'\t{line_count:>3}. {row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            
        print(f'Processed {line_count-1} records.')

def list_all_dialects():
    # Return the names of all registered dialects.
    dialects_list = csv.list_dialects()
    print("Supported Dialects are as follows:")
    for dialect in dialects_list:
        print(f"\t{dialect}")


# The csv.writer() method returns a writer object which converts the user's data into delimited strings on the given file-like object.
def csv_writer(dataList, fileName):
    """
    Write data to a CSV file path
    """
    # if newline is specified as '' or '\n' while 
    # opening the file then no translation will occur
    with open(fileName, mode="w",newline='') as output_file:
        # dialect = excel
        # writer = csv.writer(output_file, 
        #                     dialect='excel',  
        #                     delimiter=',',
        #                     lineterminator='\n')
        # unix : using '\n' as line terminator and quoting all fields.
        # writer = csv.writer(output_file, dialect='unix',  delimiter=',')
        # excel-tab :properties of an Excel-generated TAB-delimited file
        writer = csv.writer(output_file, dialect='excel-tab')
        line_counter = 0
        for alist in dataList:
            line_counter += 1
            writer.writerow(alist)
            
    print(f'Wrote {line_counter} lines.')
    print(f'Wrote {len(dataList)} lines.')
  

# The csv.DictReader class operates like a regular reader but maps the information read into a dictionary. The keys for the dictionary can be passed in with the fieldnames parameter or inferred from the first row of the CSV file.
        
def csvDictReader1():
    with open('employeeBD.csv', mode='r') as input_file:
        csv_dict_reader = csv.DictReader(input_file, dialect='excel')
        print(type(csv_dict_reader))  # csv.DictReader
        # print(*csv_dict_reader)
        # 
        row = next(csv_dict_reader)
        # print(type(row))  # collections.OrderedDict till 3.7 & dict later
        
        print(row)   # OrderedDict
        print(f'Column names are {", ".join(row)}')
        # print(f'Column names are {", ".join(row.keys())}')
        print(f'\t{row["Name"]} works in the {row["Department Name"]} \
department, and was born in {row["Birthday month"]}.')
        row = csv_dict_reader.__next__()
        print(f'\t{row["Name"]} works in the {row["Department Name"]} \
department, and was born in {row["Birthday month"]}.')
        row = next(csv_dict_reader)
        print(f'\t{row["Name"]} works in the {row["Department Name"]} \
department, and was born in {row["Birthday month"]}.')


def csvDictReader2():
    with open('employeeBD.csv', mode='r') as input_file:
        csv_dict_reader = csv.DictReader(input_file, dialect='excel')
        line_count = 1
        for row in csv_dict_reader: # row : OrderedDict /Dict
              print(f'\t{row["Name"]} works in the {row["Department Name"]}\
  department, and was born in {row["Birthday month"]}.')
              line_count += 1
            
        print(f'Processed {line_count} records.')
       
def csvDictReader_search():
    with open('employeeBD.csv', mode='r') as input_file:
        csv_dict_reader = csv.DictReader(input_file, dialect='excel')
        name = input('Please enter the employees name : ')
        # print(csv_dict_reader)
        for record_dict in csv_dict_reader: 
            if(record_dict['Name'].upper()==name.upper()):
                print(f'\t{record_dict["Name"]} works in the \
 {record_dict["Department Name"]} department, \
 and was born in {record_dict["Birthday month"]}.')
                break #terminate for loop
        else:
            print(f'{name} not found' )
        
        
def csvDictWriter(filename, columnNames, list_dict):
    """
    Writes a CSV file using DictWriter
    """
    import os.path
    path = os.path.realpath(filename)
    with open(path, "w",newline='') as out_file:
#        print(fieldnames)
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=columnNames)
        writer.writeheader( )
        write_one_row_at_time(writer,list_dict)
        out_file.write("\n\n")
        writer.writeheader( )
        write_all_rows_at_once(writer,list_dict)
      
    
def write_one_row_at_time(writer, list_dict):
    for row_dict in list_dict:
        writer.writerow(row_dict)   
    
def  write_all_rows_at_once(writer,list_dict):
    writer.writerows(list_dict)
    
    
def readWithPandas():
    import pandas
    df = pandas.read_csv('dict_output.csv')
    # print(type(df))
    print(df)
    print()
    
 
def readWithPandas_withindex():
    import pandas
    df = pandas.read_csv('dict_output.csv', index_col='city')
    # print(type(df)  ) 
    print(df.sort_index())
    print()
    
   
def readExcelfile():
    import pandas
    
    print(".xls files require xlrd to be installed" )
    data = pandas.read_excel('RegistrationReport.xls', 
                             sheet_name='Sheet2',
                             index_col='Email')
    print(data)
    
    print(".xlsx files require openpyxl to be installed" )
    data = pandas.read_excel('RegistrationReport.xlsx', 
                             sheet_name='Sheet1',
                             index_col='Registration Time')
    print(data)
    print("\n************")

    
if __name__ == "__main__":    
    # simpleReaderExample()   
    # simpleReaderDelimiter()
    # csvReader()
    # list_all_dialects()
  # 
#    Write data to a CSV file path
    # data = ["first_name:last_name:city:0".split(":"),
    #         'Amit\'s:Shinde:Pune:13'.split(":"),
    #         "Sushant:Pailwal:Sangli:14".split(":"),
    #         "Trishant:Nimsankar:Nasik:15".split(":"),
    #         "Chetan:Pujari:Baramati:16".split(":"),
    #         "Saikrashna:Vittanala:Tumkur:17".split(":"),
    #         "Abhishek:Kamble:Nagar:18".split(":")
    #         ]
    # fileName = "output.csv"
    # csv_writer(data, fileName)
#       
    # csvDictReader1()
    # csvDictReader2()
    # csvDictReader_search()
  # Writes a CSV file using DictWriter  
    # data = ["first_name,last_name,city".split(","),
    #         "Amit,Shinde,Pune".split(","),
    #         "Sushant,Pailwal,Sangli".split(","),
    #         "Trishant,Nimsankar,Nasik".split(","),
    #         "Chetan,Pujari,Baramati".split(","),
    #         "Saikrashna,Vittanala,Tumkur".split(","),
    #         "Abhishek,Kamble,Nagar".split(",")
    #         ] 
    # list_dict = []
    # columnNames = data[0]
    # for values in data[1:]:
    #     inner_dict = dict(zip(columnNames, values))
    #     # print(inner_dict)
    #     list_dict.append(inner_dict)
    # # print(list_dict)
    # filename = "dict_output.csv"
    # csvDictWriter(filename, columnNames, list_dict)
#    
    # readWithPandas()
    # readWithPandas_withindex()
    # readExcelfile()