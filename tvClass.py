class   TV:
    from typing import Final
    MIN_CHANNEL_NUM:Final[int] = 1
    MIN_VOLUME_LEVEL:Final[int] = 1
    MAX_CHANNEL_NUM:Final[int] = 120
    MAX_VOLUME_LEVEL:Final[int] = 7

    def turnOn(self)->None:
        if not self.on:
            self.on = True
        else:
            raise ValueError("The TV is on already")

    def turnOff(self)->None:
        if self.on:
            self.on = False
        else:
            raise ValueError('The TV is already off')
        
    def setVolume(self,volumelevel:int)->None:
        if self.on :
            if TV.MIN_VOLUME_LEVEL<=volumelevel<=TV.MAX_VOLUME_LEVEL :
                self.volumelevel = volumelevel
            else:
                raise ValueError("The volume level should be in the range (1,7)")
        else:
            raise ValueError("To set the volume TV should be on ")

    def setState(self,is_on:bool)->None:
        if is_on:
            self.turnOn()
        else:
            self.turnOff()

    def setChannel(self,channel:int)->None:
        if self.on :
            if TV.MIN_CHANNEL_NUM<=channel<=TV.MAX_CHANNEL_NUM:
                self.channel = channel
            else:
                raise ValueError("The channel num should be in the range (1,120)")
        else:
            raise ValueError("To set the channel TV should be on ")
        
    def __init__(self,channel:int = MIN_CHANNEL_NUM,volume :int = MIN_VOLUME_LEVEL,is_on:bool = False):
        if not isinstance(channel,int):
            raise TypeError('Passed channel_num is not an integer')
        else:
            self.setChannel(channel)
        if not isinstance(volume,int):
            raise TypeError('Passed volume is not an integer')
        else:
            self.setVolume(volume)
        if not isinstance(is_on,bool):
            raise TypeError('Passed state is not a boolean value')
        else:
            self.setState(is_on)      

    def getChannel(self)->int:
        if self.on:
            return self.channel
        else:
            raise('tv should be on')

    def getVolume(self)->int:
        if self.on:
            return self.volumelevel
        else:
            raise ValueError('The tv should be on ')
        
    def channelUp(self)->None:
        if self.on :
            if TV.MIN_CHANNEL_NUM<=self.channel<TV.MAX_CHANNEL_NUM:
                self.channel = self.channel + 1
            else:
                raise ValueError("The channel num should be in the range (1,120)")
        else:
            raise ValueError(" TV should be on ")

    def channelDown(self)->None:
        if self.on :
            if TV.MIN_CHANNEL_NUM<self.channel<=TV.MAX_CHANNEL_NUM:
                self.channel = self.channel - 1
            else:
                raise ValueError("The channel num should be in the range (1,120)")
        else:
            raise ValueError("TV should be on ")

    def volumeUp(self)->None:
        if self.on :
            if TV.MIN_VOLUME_LEVEL<=self.volumelevel<TV.MAX_VOLUME_LEVEL :
                self.volumelevel = self.volumelevel + 1
            else:
                raise ValueError("The volume level should be in the range (1,7)")
        else:
            raise ValueError("To set the volume TV should be on ")

    def volumeDown(self)->None:
        if self.on :
            if TV.MIN_VOLUME_LEVEL<self.volumelevel<=TV.MAX_VOLUME_LEVEL :
                self.volumelevel = self.volumelevel - 1
            else:
                raise ValueError("The volume level should be in the range (1,7)")
        else:
            raise ValueError("To set the volume TV should be on ")

if __name__ == '__main__':
    try:
        lg = TV()
        print(lg.on)
        # lg.turnOn()
        # lg.turnOff()
        # channel_num = lg.getChannel()
        # lg.setChannel(89)
        # channel_num = lg.getChannel()
        # print(channel_num)
        # volume = lg.getVolume()
        # print(volume)
        # lg.setVolume(24)
        # volume = lg.getVolume()
        # print(volume)
        # lg.channelUp()
        # channel_num = lg.getChannel()
        # print(channel_num)
        # lg.channelDown()
        # channel_num = lg.getChannel()
        # print(channel_num)
        # lg.volumeDown()
        # volume = lg.getVolume()
        # print(volume)
        # lg.volumeUp()
        # volume = lg.getVolume()
        # print(volume)
    except (ValueError,TypeError) as err:
        print(f"{type(err).__name__} : {err}")