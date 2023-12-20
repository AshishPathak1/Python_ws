# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 19:16:17 2023

@author: rahul

        Initializes a TV object with default settings.

        parameter channel: The initial channel (default is 1).
        parameter volume_level: The initial volume level (default is 1).
        parameter ON/OFF:The initial condition (Default is False)
 """

class TV:
    from typing import Final
    #class data
    __MAX_CHANNEL:Final[int] = 120
    __MIN_CHANNEL:Final[int] = 1
    __MAX_VOLUME :Final[int] = 7
    __MIN_VOLUME :Final[int] = 1
    
    @staticmethod
    def __is_data_of_integer_type(data)->bool:
        return isinstance(data, int)
    
    @staticmethod
    def __is_data_of_bool_type(data)->bool:
        return isinstance(data, bool)
    
    @classmethod
    def __is_channel_number_in_valid_range(cls,channel: int) -> bool:
        return (cls.__MIN_CHANNEL <= channel <= cls.__MAX_CHANNEL)
    
    @classmethod      
    def __is_volume_in_valid_range(cls,volume: int) -> bool:
        return (cls.__MIN_VOLUME <= volume <= cls.__MAX_VOLUME)
              
    
    def __init__(self,channel:int = 1,volumeLevel:int = 1,isOn:bool = False):
        if not TV.__is_data_of_integer_type(channel):
            raise TypeError("Channel value should be of integer type")
        
        if not TV.__is_data_of_integer_type(volumeLevel):
            raise TypeError("VolumeLevel value should be of integer type")
            
        if not TV.__is_data_of_bool_type(isOn):
            raise TypeError("TV state value should be of Boolean type")
        
        if not TV.__is_channel_number_in_valid_range(channel):
            raise ValueError(f"Channel should be in the range of {TV.__MIN_CHANNEL} to {TV.__MAX_CHANNEL}")
        
        if not TV.__is_volume_in_valid_range(volumeLevel):
            raise ValueError(f"Volume level should be in the range of {TV.__MIN_VOLUME} to {TV.__MAX_VOLUME}")
        #Instance data
        self.__channel     = channel
        self.__volumeLevel = volumeLevel
        self.__isOn        = isOn

    def turnOn(self)->None:
        self.__isOn = True

    def turnOff(self)->None:
        self.__isOn = False

    def getTvPowerState(self):
        return self.__isOn
    
    def getChannel(self)->int:
        return self.__channel

    def setChannel(self, channel:int)->None:
      if not TV.__is_data_of_integer_type(channel):
          raise TypeError("Channel value should be of integer type")
       
      if not self.__isOn:
         raise RuntimeError("TV is off, cannot change the channel")
              
      if not TV.__is_channel_number_in_valid_range(channel):
          raise ValueError(f"Channel should be in the range of {TV.__MIN_CHANNEL} to {TV.__MAX_CHANNEL}")
      
      self.__channel = channel
     
 
    def getVolume(self)->int:
        return self.__volumeLevel

    def setVolume(self, volumeLevel:int)->None:
        if not TV.__is_data_of_integer_type(volumeLevel):
            raise TypeError("VolumeLevel value should be of integer type")
        
        if not self.__isOn:
            raise ValueError("TV is off, cannot change the volume")
        
        if not TV.__is_volume_in_valid_range(volumeLevel):
            raise ValueError(f"Volume level should be in the range of {TV.__MIN_VOLUME} to {TV.__MAX_VOLUME}")
        
        self.__volumeLevel = volumeLevel
            
    def channelUp(self)->None:
        if not self.__isOn:
            raise ValueError("TV is off, cannot change the channel")

        if not TV.__is_channel_number_in_valid_range(self.__channel+1):
            raise ValueError(f"Channel number cannot exceed {TV.__MAX_CHANNEL}")
      
        self.__channel =  self.__channel + 1
 
    def channelDown(self)->None:
        if not self.__isON:
            raise ValueError("TV is off, cannot change the channel")

        if not TV.__is_channel_number_in_valid_range(self.__channel-1):
            raise ValueError(f"Channel number cannot go below {TV.__MIN_CHANNEL}")
      
        self.__channel =  self.__channel - 1
    
    def volumeUp(self)->None:
        if not self.__isON:
            raise ValueError("TV is off, cannot change the volume")
         
        if not TV.__is_volume_in_valid_range(self.__volumeLevel+1):
            raise ValueError(f"Channel number cannot exceed {TV.__MAX_VOLUME}")
          
        self.__volumeLevel =  self.__volumeLevel + 1


    def volumeDown(self)->None:
        if not self.__isON:
            raise ValueError("TV is off, cannot change the volume")
         
        if not TV.__is_volume_in_valid_range(self.__volumeLevel-1):
            raise ValueError(f"Volume cannot cannot go below {TV.__MIN_VOLUME}")
          
        self.__volumeLevel =  self.__volumeLevel - 1
        
    def __str__(self):
        # self.__class__.__MAX_CHANNEL = 89
        return f"""TV info:
    Channel Number : {self.__channel}
    Volume Level   : {self.__volumeLevel}
    Is the TV on ? : {self.__isOn}
    MAX CHANNEL    : {TV.__MAX_CHANNEL}""" 
     
    @classmethod       
    def getMaxChannel(cls):
       return cls.__MAX_CHANNEL
    
    @classmethod       
    def setMaxChannel(cls,channel):
       cls.__MAX_CHANNEL = channel 
    
    @classmethod     
    def getMinChannel(cls):
        return cls.__MIN_CHANNEL
    
    @classmethod     
    def getMaxVolumeLevel(cls):
        return cls.__MAX_VOLUME
    @classmethod     
    def getMinVolumeLevel(cls):
        return cls.__MIN_VOLUME
    
if __name__ == '__main__':
    try:
        print(f"Maximum Channel :{TV.getMaxChannel()}")
       
        my_tv = TV(100,5,True)
        print(my_tv)
        print(f"Maximum Channel :{TV.getMaxChannel()}")
        # TV.setMaxChannel(55)
        print(f"Maximum Channel :{TV.getMaxChannel()}")
        # my_tv.setMaxChannel(99)
        print(f"Maximum Channel :{TV.getMaxChannel()}")
        
        # my_tv = TV(13,5,False)
        # print(my_tv)
        
        # my_tv = TV(13,1,True)
        # print(my_tv)
        
        # my_tv.turnOn()
        # print(f"TV is on:{ my_tv.getTvPowerState()}")
        # my_tv.__isOn = complex(34,5)
        # print(f"TV is on:{ my_tv.__isOn}")
        # print(f"Current Channel:{my_tv.__channel}")
        # print(f"Current Channel:{my_tv.getChannel()}")
        # my_tv.setChannel(11)
        # print(f"Current Channel:{my_tv.getChannel()}")
     
        # my_tv.volumeDown()
        # print(f"Current Volume after volume up and down:{ my_tv.getVolume()}")
        
        # my_tv.setChannel(7)
        # print(f"Current Channel:{my_tv.getChannel()}")
        # my_tv.setVolume(3)
        # print(f"Current Volume Level:{ my_tv.getVolume()}")
        
        
        # my_tv.channelUp()
        # my_tv.channelDown()
        # print(f"Current Channel :{my_tv.getChannel()}")
        
        
        # my_tv.volumeUp()
        # my_tv.volumeDown()
        # print(f"Current Volume after volume up and down:{ my_tv.getVolume()}")
        
        
        # my_tv.turnOff()
        # print(f"TV is on:{ my_tv.isOn}")
    except (ValueError,TypeError) as err:
        print(f"{type(err).__name__} : {err}")