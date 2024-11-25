class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initialize default instance variables.
        """
        self._Television__volume = None
        self._Television__channel = None
        self._Television__mute = None
        self._Television__status = None
        self.__status = False
        self.__mute = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggle the power state of the TV.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Toggle mute state.
        """
        if self.__status:
            self.__mute = not self.__mute

    def channel_up(self) -> None:
        """
        Increase the channel value.
        Wrap around to the minimum if at the maximum.
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decrease the channel value.
        Wrap around to the maximum if at the minimum.
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Increase the volume.
        If muted, unmute the TV.
        Volume cannot exceed the maximum value.
        """
        if self.__status:
            if self.__mute:
                self.__mute = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decrease the volume.
        If muted, unmute the TV.
        Volume cannot go below the minimum value.
        """
        if self.__status:
            if self.__mute:
                self.__mute = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Return the current state of the TV.
        :return: A string showing the power, channel, and volume.
        """
        volume = 0 if self.__mute else self.__volume
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}'


