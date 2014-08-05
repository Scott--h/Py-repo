import threading
import atexit

from Debug import Debug
# if vlsDebugEnabled
if Debug.isDebugEnabled():
    javalcm = True
    from lcm.lcm import LCM
    from lcm.lcm import LCMSubscriber
    from VLS import VLSLauncher
else:
    import lcm
    javalcm = False

from asvlcm import motor_t, vehicleState_t, desired_t, controlState_t, auxAct_t, auxAdc_t, kill_t, kill_status_t, \
    console_t, processedScene_t, visionCommand_t, const_t, buoyMap_t, colorinit_t, desiredPath_t, pinger_t, controlSource_t
from asvPylib.timing import get_utime
from asvPylib import Location
from math import sin, cos, radians
from asvPylib.conversion import rotated

if javalcm:
    controllersuperclass = LCMSubscriber
else:
    controllersuperclass = object

class LCMreceiver(LCMSubscriber if javalcm else object):
    '''
    This is the LCM message handler for use in missions.
    Openchannel(self, channel_struct())


    Messages are listened for and returned.
    Internal ticker counts number of NaN, fucked up messages
    filters them out, returns X number of complete frames for
    mission analysis
    
    TODO:
    
    talk to steve about currently used lcm channels

    '''

    def __init__(self):
        #define master channel list here corresponding structs to channels
        #lcmChannels is a dictionary containing key:value pairs linking LCM channel
        #names to their corresponding structs.
        #TODO add in const_t() handler to open and close vision and color missions automatically

        lcmChannels = {}
        lcmChannels['SOUND'] = sound_t()
        lcmChannels['PINGER'] = pinger_t()
        lcmChannels['GPS'] = gps_t()
        lcmChannels['MOTOR STATUS'] = motorStatus_t()
        lcmChannels['MOTOR CONFIG'] = motorConfig_t()
        lcmChannels['BUOY MAP'] = buoyMap_t()
        lcmChannels['TRACKING_STATE'] = vehicleState_t()
        lcmChannels['PROCESSED_SCENE'] = processedScene_t()
        lcmChannels['MOTOR'] = motor_t()

    def openChannel(self, channel, data):
        openedChannel = self.lcm.subscribe(channel, self)

        _msgType = lcmChannels[channel]
        _msgOutput = _msgType.decode(data)

        print 'Returning message structure: ', _msgOutput

        return _msgOutput




    def closeChannel(self):
        #called to close all open LCM channels

    def checkChannel(self, channelStruct):


    def _registerChannels(self):
        # Register listening
        self.listenChannel("KILL_STATUS", kill_status_t)
        self.listenChannel("AUX_ADC", auxAdc_t)
        self.listenChannel("CONTROL_CMD", controlState_t)
        self.listenChannel("VEHICLE_STATE", vehicleState_t)
        self.listenChannel("SMOOTH_STATE", vehicleState_t)
        self.listenChannel("TRACKING_STATE", vehicleState_t)
        self.listenChannel("MOTOR", motor_t)
        self.listenChannel("AUX_ACT", auxAct_t)
        self.listenChannel("PROCESSED_SCENE", processedScene_t)
        self.listenChannel("BUOY_MAP", buoyMap_t)
        self.listenChannel("PINGER", pinger_t)

    def listenChannel(self, channel, msgType):
        else:
            self._lcm.subscribe(channel,self)
            self._channelTypes[channel] = msgType


    def getChannelMsg(self, channel):
        """ Get the last packet received on the specified channel.
        A number of channels are listened to by default and/or
        have convience methods defined by the get methods for this class.
        Additional channels may be subscribed to with listenChannel.
        Will return None if no message has been received """
        self._lock()
        ret = self._state.get(channel)
        #print "Getting message", ret
        self._unlock()
        return ret
