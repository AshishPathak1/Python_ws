import os
import wave
import csv
import sys
import csv

def update_file_duration_count(csv_file_path):
    group_dict = {'less_than_1_min': 0.0, 'between_1_and_5_min': 0.0, 'between_5_and_10_min': 0.0, 'greater_than_10_min': 0.0}
    try:
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                duration_in_min = float(row['Duration (min)'])            
                if duration_in_min < 1.0:
                    group_dict['less_than_1_min'] += 1
                elif duration_in_min < 5.0:
                    group_dict['between_1_and_5_min'] += 1
                elif duration_in_min < 10.0:
                    group_dict['between_5_and_10_min'] += 1
                else:
                    group_dict['greater_than_10_min'] += 1
    except FileNotFoundError:
        print(f"CSV file not found: {csv_file_path}")
    return group_dict

# def get_wav_files(folder_path)->list:
#     wav_files = []
#     for root, dirs, files in os.walk(folder_path):
#         for file in files:
#             file = root + os.sep + file
#             if file.endswith('.wav'):
#                wav_files.append(file)
#     return(wav_files)
 
def iterate_over_wav_files(folder_path):
    # csv_file_name = generate_csv_file_name()
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file = root + os.sep + file
            if file.endswith('.wav'):
                    write_wave_file_info(file)

def get_audio_duration(wav_file):
    '''Returns .wav file duration in minutes by taking the wav file as a parameter'''
    try:
        with wave.open(wav_file, 'r') as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration_seconds = frames / float(rate)
            duration_minutes = duration_seconds / 60
        return round(duration_minutes,2)
    except wave.Error:
        print(f"Error processing file {wav_file}")
        return None

def generate_csv_file_name():
    from datetime import date
    today = date.today()
    return f"rep_{today.day}_{today.month}_{today.year}.csv"
    
def get_folder_path():
    folder_path = sys.argv[1]  
    print(f"The directory to iterate: {folder_path} ")
    return folder_path

def write_wave_file_info(wav_file):
    csv_file_name = generate_csv_file_name()
    minutes = get_audio_duration(wav_file)
    if minutes is not None:
        wav_file_rec = {'File Name': wav_file, 'Duration (min)':minutes}
        csv_file = open(csv_file_name,'a',newline='')   
        writer = csv.DictWriter(csv_file, fieldnames=wav_file_rec.keys())
        if csv_file.tell() == 0:  #if the file is empty
            writer.writeheader()
        writer.writerow(wav_file_rec) 
        csv_file.close()
    return csv_file_name
    
def write_summary(csv_file_name,data:dict):
    # print(data)
    with open(csv_file_name, 'a', newline='') as csvfile:
            fieldnames = ['File Group', 'Count (number of files)']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        
if __name__=='__main__':   
    try:
        folder_path = get_folder_path()
        iterate_over_wav_files(folder_path) 
        csv_file_name = generate_csv_file_name()
        data = update_file_duration_count(csv_file_name)
        print(data)
        write_summary(csv_file_name,data)
        
    except IndexError:
        print("The folder path to analyse has not been passed on command prompt")
        print("Correct Usage : python Audiotext.py <folder path from root>")