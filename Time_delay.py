import lcm
import numpy as np
from asvlcm import sound_t
from asvPylib import get_utime
'''Hydrophone Signal Processing'''
'''Scott Hara'''


class soundD:

    def __init__(self):

        self.lcm = lcm.LCM()
        self.lcm.subscribe("SOUND", self.sound_handler)
        self.utime = get_utime()

    def sound_handler(self, channel, data):
        self.msg = self.sound.decode(data)

    def peakorient(sig_1, sig_2, samplerate):
        peak_1 = peakindex(sig_1)
        peak_2 = peakindex(sig_2)

        peakdiff = peak_1 - peak_2

        if peakdiff >= 0:
            #return turn right
        else if peakdiff < 0:
            #return turn left
        else:
            #return wat

    def peakindex(sig, samplerate):
        '''
        determines the index location of the peak sum found with jSum, jEval
        '''
        j_sig = jSum(sig, samplerate)
        sig_max = max(j_sig)
        sig_max_index = j_sig.index(sig_max)

        return sig_max_index

    def phasediff(sig, deltaT, hydrod):
        '''
        Finds the phase difference between signals. Needs work.
        '''
        sound_speed = 1497
        pdiff = np.arcsin((deltaT * sound_speed) / hydrod)
        return pdiff

    def jSum(sig, samplerate):
        '''
        sig: signal data from hydrophone
        samplerate: sampling rate of recorded data

        J: an array containing the signal sum at each sample
        '''
        J = []
        for n in range(samplerate):
            J.append(jEval(sig,samplerate,n))
        return J

    def jEval(sig, samplerate, delta):
        '''
        sig: signal data from hydrophone
        samplerate: sampling rate of supplied signal. Should be 96k
        delta: offset which moves the 

        total: summation of each part of a sample offset by delta.
        ideal: 
        '''
        total = 0
        for i in range(samplerate):
            check = total + delta
            if check > samplerate:
                break
            else:
                total = sig(delta + i)
        return total



