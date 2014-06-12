import lcm
import numpy as np
from asvlcm import sound_t
from asvPylib import get_utime


def phasediff(sig, deltaT, hydrod):
    sound_speed = 1497
    pdiff = np.arcsin((deltaT * sound_speed) / hydrod)
    return pdiff

def timediff(sig, sigpulselength, sigsample):

    J = []
    for n in range(sigsample):
        J.append(jEval(sig,sigpulselength,n))
    return J

def jEval(sig, sigpulselength, delta):

    jsum = 0
    for i in range(sigpulselength):

        jsum = sig(delta + i) * ideal(i)
    return jsum



class soundD:

    def __init__(self):

        self.lcm = lcm.LCM()
        self.sound = sound_t()
        self.utime = get_utime()


    def sound_handler(self, channel, data):

        msg = sound_t().decode(data)
        self.raw = [msg.]