import os
import wave
import csv
import sys

class wav_file:
    def __init__(self) -> None:
        self.__group_dict = {'less_than_1_min':0,'between_1_and_5_min':0,'between_5_and_10_min':0,'greater_than_10_min':0}
        self.__duration_in_min = 0.0
        self.__file_path = ""
        self.__csv_file_name = ""
        self.__folder_path  = ""
        self.__wav_file = ""
        self.__csv_file = ""
        self.__wav_file_data = {}
        self.__minutes = 0.0

    def update_file_duration_count(self,duration_in_min):
        if ( self.__duration_in_min) < 1.0 :
            self.__group_dict['less_than_1_min'] +=1
        elif self.__duration_in_min < 5.0 :
            self.__group_dict['between_1_and_5_min'] +=1
        elif self.__duration_in_min < 10.0:
            self.__group_dict['between_5_and_10_min'] += 1
        else:
            self.__group_dict['greater_than_10_min'] +=1
        
    def iterate_over_wav_files(self,folder_path):
        self.__csv_file_name = self.generate_csv_file_name()
        for root, dirs, files in os.walk(self.__folder_path):
            for file in files:
                file = root + os.sep + file
                if file.endswith('.wav'):
                    self.process_file_info(file,self.__csv_file_name)

    def get_audio_duration(self,wav_file):
        '''Returns .wav file duration in minutes by taking the wav file as a parameter'''
        try:
            with wave.open(self.__wav_file, 'r') as f:
                frames = f.getnframes()
                rate = f.getframerate()
                duration_seconds = frames / float(rate)
                duration_minutes = duration_seconds / 60
            result = round(duration_minutes,2)
            return result
        except wave.Error:
            print(f"Error processing file {wav_file}")
            return None

    def get_folder_path(self):
        self.__folder_path = sys.argv[1]  
        print(f"The directory to iterate: {self.__folder_path} ")
        return self.__folder_path

    def process_file_info(self,wav_file,csv_file_name):
        self.__minutes = self.get_audio_duration(wav_file)
        if self.__minutes is not None:
            self.update_file_duration_count(self.__minutes)
            print(f"{wav_file} {self.__minutes} min")    
            duration_str = f"{self.__minutes}"
            self.write_to_csv({'File Name': wav_file, 'Duration (min)': duration_str},self.__csv_file_name)

    def take_path_and_iterate_over_files(self):
            self.__folder_path = self.get_folder_path()
            self.iterate_over_wav_files(self.__folder_path) 

class csv_file:
    def __init__(self) -> None:

    def generate_csv_file_name():
        from datetime import date
        today = date.today()
        return f"report_{today.day}_{today.month}_{today.year}.csv"
    
    def write_to_csv(self,wav_file_data:dict, csv_file):
        with open(self.__csv_file, 'w', newline='') as csvfile:
            if self.is_csv_empty(csvfile):
                fieldnames = ['File Name', 'Duration (min)']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
            writer.writerow(self.__wav_file_data)
    
    def is_csv_empty(self,file_path):
        with open(self.__file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader, None)
            for row in csv_reader:
                if row:
                    return False  
        return True  
if __name__=='__main__':   
    try:
        honey_singh = wav_file()

        honey_singh.take_path_and_iterate_over_files()
    except IndexError:
        print("The folder path to analyse has not been passed on command prompt")
        print("Correct Usage : python Audiotext.py <folder path from root>")