import pytest
from television import Television


def test_init():
    """Test that the Television initializes with default values."""
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_power():
    """Test that the power method turns the TV on and off."""
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_mute():
    """Test that muting works correctly."""
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"  # Muted
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"  # Unmuted


def test_channel_up():
    """Test channel_up functionality for both off and on."""
    tv = Television()
    tv.channel_up()  # Should do nothing when TV is off
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"  # Wrap around


def test_channel_down():
    """Test channel_down functionality for both off and on."""
    tv = Television()
    tv.channel_down()  # Should do nothing when TV is off
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"  # Wrap around
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 2, Volume = 0"


def test_volume_up():
    """Test volume_up functionality for both off and on."""
    tv = Television()
    tv.volume_up()  # Should do nothing when TV is off
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()  # Should stop at max volume
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"


def test_volume_down():
    """Test volume_down functionality for both off and on."""
    tv = Television()
    tv.volume_down()  # Should do nothing when TV is off
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"  # Already at min volume
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

