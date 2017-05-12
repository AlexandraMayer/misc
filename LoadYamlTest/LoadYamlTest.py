import os
import sys
from yaml import load
from yaml import CLoader as Loader
from scipy import constants as const

file_path = os.path.expanduser("~/testFileLoadYaml.yaml")

file_test = open(file_path,"w")

file_test.write("instrument:\n")
file_test.write("    name: DNS\n")
file_test.write("format:\n")
file_test.write("    units:\n")
file_test.write("        angle: deg\n")
file_test.write("        clearance: mm\n")
file_test.write("        current: A\n")
file_test.write("        duration: s\n")
file_test.write("        energy: eV\n")
file_test.write("        temperature: K\n")
file_test.write("        wavelength: A\n")
file_test.write("measurement:\n")
file_test.write("    unique_identifier: service/335361/0\n")
file_test.write("    history:\n")
file_test.write("        started: \"2017-01-26T03:03:30\"\n")
file_test.write("        stopped: \"2017-01-26T03:23:30\"\n")
file_test.write("        duration_counted: 1200.0\n")
file_test.write("    sample:\n")
file_test.write("        temperature:\n")
file_test.write("            setpoint:\n")
file_test.write("                mean: 3.0\n")
file_test.write("            T1:\n")
file_test.write("                mean: 290.001\n")
file_test.write("            T2:\n")
file_test.write("                mean: 0.0\n")
file_test.write("        orientation:\n")
file_test.write("            rotation_angle: 129.993560731\n")
file_test.write("    setup:\n")
file_test.write("        settings_for:\n")
file_test.write("            incident_wavelength: 4.2\n")
file_test.write("            incident_energy: 4.63742431973\n")
file_test.write("        flipper:\n")
file_test.write("            setting: \"off\"\n")
file_test.write("            precession_current: 0.0\n")
file_test.write("            z_compensation_current: 0.0\n")
file_test.write("        slit_i:\n")
file_test.write("            upper_clearance: 20.0000033\n")
file_test.write("            lower_clearance: -20.0000139\n")
file_test.write("            left_clearance: -10.0000427\n")
file_test.write("            right_clearance: 10.0000223\n")
file_test.write("        xyz_coil:\n")
file_test.write("            coil_a_current: 0.0\n")
file_test.write("            coil_b_current: 0.0\n")
file_test.write("            coil_c_current: 0.0\n")
file_test.write("            coil_zb_current: 0.0\n")
file_test.write("            coil_zt_current: 0.0\n")
file_test.write("        polarization: \"off\"\n")
file_test.write("        time_of_flight:\n")
file_test.write("            number_of_channels: 4\n")
file_test.write("            delay_duration: 0.35\n")
file_test.write("            channel_duration: 0.0004\n")
file_test.write("    detectors:\n")
file_test.write("    -   type: polarization_analyser_detector_bank\n")
file_test.write("        angle_tube0: -7.49793995077\n")
file_test.write("        counts:\n")
file_test.write("            0: [0, 1, 0, 1]\n")
file_test.write("            1: [1, 0, 2, 0]\n")
file_test.write("            2: [0, 0, 1, 0]\n")
file_test.write("            3: [0, 0, 0, 2]\n")

file_test.close()

file = open(file_path)
data = load(file, Loader)
file.close()

setup = data['measurement']['setup']

wavelength =   setup['settings_for']['incident_wavelength']
print wavelength

tof_delay_dur = setup['time_of_flight']['delay_duration']
print tof_delay_dur

tof_channel_dur = (setup['time_of_flight']['channel_duration'])*1e+06
print tof_channel_dur
    
L1 = 0.36325



def cal_x1(l1=None, ch_width=None, delay=None):
    print ch_width
    v = const.h/(const.m_n*wavelength*1e-10)
    if l1:
        tof1 = l1/v
    else:
        tof1 = L1/v
    if delay:
        x0 = tof1 + (tof_delay_dur*delay)
    else:
         x0= tof1 + tof_delay_dur
    if ch_width:
        x1 = x0 + (tof_channel_dur*ch_width)
    else:
        x1 = x0 + tof_channel_dur
    return x1

def end():
    Test.end()

def test_l1(l1=None):
    
    ws = LoadYaml(Filename= file_path, SourceSampleDistance=l1)
    x1_load = ws.dataX(0)[1]
    x1 = cal_x1(l1=l1)
    if not x1 == x1_load:
        logger.error("wrong calcutating with source sample distance")
        sys.exit()
        
    return x1_load

def test_channel_width(ch_width=None):
    
    ws = LoadYaml(Filename= file_path,ChannelWidthsFactor=ch_width)
    x1_load = ws.dataX(0)[1]
    print x1_load
    x1 = cal_x1(ch_width=ch_width)
    print x1
    print ch_width
    if not x1 == x1_load:
        logger.error("wrong calcutating with channel width")
        sys.exit()
        
    return x1_load
     
def test_delay(delay=None):
    
    ws = LoadYaml(Filename= file_path,TofDelayFactor=delay)
    x1_load = ws.dataX(0)[1]
    x1 = cal_x1(delay=delay)
    if not x1 == x1_load:
        logger.error("wrong calcutating with tof delay")
        sys.exit()
        
    return x1_load
        
def cleanUp():
     if os.path.exists(file_path):
        os.remove(file_path)
     if mtd.doesExist('ws'):
        mantid.api.AnalysisDataService.remove('ws')   

print
x_l1_n = test_l1()
x_l1 = test_l1(0.45)
print str(x_l1_n != x_l1)
if x_l1_n == x_l1:
    logger.error("no change in x if source sample distance changed")
    sys.exit()
print
x_ch_w_n = test_channel_width()
x_ch_w = test_channel_width(0.001)
if x_ch_w_n == x_ch_w:
    logger.error("no change in x if channel with factor changed")
    sys.exit()
    
print str(x_ch_w_n != x_ch_w)
print
x_delay_n = test_delay()
x_delay = test_delay(1e-06)
if x_delay_n == x_delay:
    logger.error("no change in x if channel with factor changed")
    sys.exit()
    
print str(x_delay_n != x_delay)
    

        

cleanUp()