import lcm
from asvlcm import sound_t
from asvPylib import get_utime


lcm = lcm.LCM()
sound = sound_t()
sound.utime = get_utime()


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

