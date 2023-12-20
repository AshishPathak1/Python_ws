import os
import wave
import csv
import sys

def update_file_duration_count(duration_in_min,group_dict):
    if ( duration_in_min) < 1.0 :
        group_dict['less_than_1_min'] +=1
    elif duration_in_min < 5.0 :
        group_dict['between_1_and_5_min'] +=1
    elif duration_in_min < 10.0:
        group_dict['between_5_and_10_min'] += 1
    else:
        group_dict['greater_than_10_min'] +=1
    
def get_wav_files(folder_path):
    wav_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file = root + os.sep + file
            if file.endswith('.wav'):
               wav_files.append(file)
    return(wav_files)

def get_audio_duration(wav_file):
    # print(f"Reading file : {wav_file}")
    '''Returns .wav file duration in minutes by taking the wav file as a parameter'''
    try:
        with wave.open(wav_file, 'r') as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration_seconds = frames / float(rate)
            duration_minutes = duration_seconds / 60
        result = round(duration_minutes,2)
        return result
    except wave.Error:
        print(f"Error processing file {wav_file}")
        return 0

def write_to_csv(data, csv_file):
    with open(csv_file, 'w', newline='') as csvfile:
        fieldnames = ['File Name', 'Duration (min)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
            
def generate_csv_file_name():
    from datetime import date
    today = date.today()
    return f"report_{today.day}_{today.month}_{today.year}.csv"
    
def get_folder_path():
    folder_path = sys.argv[1]  
    print(f"The directory to iterate: {folder_path} ")
    return folder_path

def process_data(wav_files,group_dict):
    for wav_file in wav_files:
        # file_name = os.path.basename(wav_file)
        minutes = get_audio_duration(wav_file)
        update_file_duration_count(minutes,group_dict)
        print(f"{wav_file} {minutes} min")    
        duration_str = f"{minutes}"
        data.append({'File Name': wav_file, 'Duration (min)': duration_str})

if __name__=='__main__':   
    group_dict = {'less_than_1_min':0,'between_1_and_5_min':0,'between_5_and_10_min':0,'greater_than_10_min':0}
    try:
        folder_path = get_folder_path()
        wav_files = get_wav_files(folder_path)
        data = []
        process_data(wav_files,group_dict)
        csv_file_name = generate_csv_file_name() 
        write_to_csv(data, csv_file_name)  
    except IndexError:
        print("The folder path to analyse has not been passed on command prompt")
        print("Correct Usage : python Audiotext.py <folder path from root>")