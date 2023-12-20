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
    MAX_CHANNEL:Final[int] = 120
    MIN_CHANNEL:Final[int] = 1
    MAX_VOLUME :Final[int] = 7
    MIN_VOLUME :Final[int] = 1
    
    def is_data_of_integer_type(data)->bool:
        return isinstance(data, int)
    
    def is_data_of_bool_type(data)->bool:
        return isinstance(data, bool)
        
    def is_channel_number_in_valid_range(channel: int) -> bool:
        return (TV.MIN_CHANNEL <= channel <= TV.MAX_CHANNEL)
            
    def is_volume_in_valid_range(volume: int) -> bool:
        return (TV.MIN_VOLUME <= volume <= TV.MAX_VOLUME)
              
    
    def __init__(self,channel:int = 1,volumeLevel:int = 1,isOn:bool = False):
        if not TV.is_data_of_integer_type(channel):
            raise TypeError("Channel value should be of integer type")
        
        if not TV.is_data_of_integer_type(volumeLevel):
            raise TypeError("VolumeLevel value should be of integer type")
            
        if not TV.is_data_of_bool_type(isOn):
            raise TypeError("TV state value should be of Boolean type")
        
        if not TV.is_channel_number_in_valid_range(channel):
            raise ValueError(f"Channel should be in the range of {TV.MIN_CHANNEL} to {TV.MAX_CHANNEL}")
        
        if not TV.is_volume_in_valid_range(volumeLevel):
            raise ValueError(f"Volume level should be in the range of {TV.MIN_VOLUME} to {TV.MAX_VOLUME}")
        
        self.channel     = channel
        self.volumeLevel = volumeLevel
        self.isOn        = isOn

    def turnOn(self)->None:
        self.isOn = True

    def turnOff(self)->None:
        self.isOn = False

    def getChannel(self)->int:
        return self.channel

    def setChannel(self, channel:int)->None:
      if not self.isOn:
         raise RuntimeError("TV is off, cannot change the channel")
      
      if not TV.is_channel_number_valid(channel):
          raise ValueError(f"Channel should be in the range of {TV.MIN_CHANNEL} to {TV.MAX_CHANNEL}")
      
      self.channel = channel
     
 
    def getVolume(self)->int:
        return self.volumeLevel

    def setVolume(self, volumeLevel:int)->None:
        if not self.isOn:
            raise ValueError("TV is off, cannot change the volume")
        if not TV.is_volume_in_valid_range(volumeLevel):
            raise ValueError(f"Volume level should be in the range of {TV.MIN_VOLUME} to {TV.MAX_VOLUME}")
        self.volumeLevel = volumeLevel
            
    def channelUp(self)->None:
        if not self.isOn:
            raise ValueError("TV is off, cannot change the channel")

        if not TV.is_channel_number_in_valid_range(self.channel+1):
            raise ValueError(f"Channel number cannot exceed {TV.MAX_CHANNEL}")
      
        self.channel =  self.channel + 1
      

    def channelDown(self)->None:
        if not self.isOn:
            raise ValueError("TV is off, cannot change the channel")

        if not TV.is_channel_number_in_valid_range(self.channel-1):
            raise ValueError(f"Channel number cannot go below {TV.MIN_CHANNEL}")
      
        self.channel =  self.channel - 1
    
    def volumeUp(self)->None:
        if not self.isOn:
            raise ValueError("TV is off, cannot change the volume")
         
        if not TV.is_volume_in_valid_range(self.volumeLevel+1):
            raise ValueError(f"Channel number cannot exceed {TV.MAX_VOLUME}")
          
        self.volumeLevel =  self.volumeLevel + 1


    def volumeDown(self)->None:
        if not self.isOn:
            raise ValueError("TV is off, cannot change the volume")
         
        if not TV.is_volume_in_valid_range(self.volumeLevel-1):
            raise ValueError(f"Volume cannot cannot go below {TV.MIN_VOLUME}")
          
        self.volumeLevel =  self.volumeLevel - 1
        
    def __str__(self):
        return f"""TV info:
    Channel Number : {self.channel}
    Volume Level   : {self.volumeLevel}
    Is the TV on ? : {self.isOn}""" 
                
if __name__ == '__main__':
    try:
        my_tv = TV(1)
        print(my_tv)
        
        # my_tv = TV(13,5,False)
        # print(my_tv)
        
        # my_tv = TV(13,1,True)
        # print(my_tv)
        
        my_tv.turnOn()
        print(f"TV is on:{ my_tv.isOn}")
        # my_tv.isOn = complex(34,5)
        # print(f"TV is on:{ my_tv.isOn}")
        
        # my_tv.volumeDown()
        # print(f"Current Volume after volume up and down:{ my_tv.getVolume()}")
        
        # my_tv.setChannel(7)
        # print(f"Current Channel:{my_tv.getChannel()}")
        # my_tv.setVolume(3)
        # print(f"Current Volume Level:{ my_tv.getVolume()}")
        
        
        # my_tv.channelUp()
        # my_tv.channelDown()
        print(f"Current Channel :{my_tv.getChannel()}")
        
        
        # my_tv.volumeUp()
        # my_tv.volumeDown()
        # print(f"Current Volume after volume up and down:{ my_tv.getVolume()}")
        
        
        # my_tv.turnOff()
        # print(f"TV is on:{ my_tv.isOn}")
    except (ValueError,TypeError) as err:
        print(f"{type(err).__name__} : {err}")