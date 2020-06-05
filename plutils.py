
raps = [ {'lbl':'eNB0',
          'x':-600, 
          'y':250,
          'RRU_Power_W' : 20,
          'BW_MHz':20,
          'AntGain_dB':16,
          'CblLoss_dB':-3 },
        {'lbl':'eNB1',
          'x':500, 
          'y':-600,
          'RRU_Power_W' : 20,
          'BW_MHz':20,
          'AntGain_dB':16,
          'CblLoss_dB':-3 }
       ]

#enbs = [ {'x':-600, 'y':250, 'lbl':'eNB0'}, {'x':500, 'y':-600, 'lbl':'eNB1'} ]

#%%

import numpy
def mW2dBm(mW):
    return 10*numpy.log10(mW)
def dBm2mW(dBm):
    return numpy.power(10, dBm/10 )
def PowerRatio2dB(pr):
    return 10*numpy.log10(pr)
def dB2PowerRatio(db):
    return numpy.power(10, db/10 )
# define BWMHz : RB dict
bwMHz_rb ={1.4:6,  3:15, 5:25, 10:50 , 15:75, 20:100 }
def getstats(x):
    return [min(x), max(x)]
#%%
assert bwMHz_rb[1.4]==6
assert bwMHz_rb[20]==100
assert mW2dBm(mW=100)==20
assert dBm2mW(30)==1000
assert PowerRatio2dB(10000)==40
assert dB2PowerRatio(10)==10
assert getstats(x=[1,2,3,4])==[1,4]

#%%

# BS parameters
#bs_pars = {'RRU_Power_W' : 20,
#           'BW_MHz':20,
#          'AntGain_dB':16,
#          'CblLoss_dB':-3}

def txpower_per_SC_dBm(ap):
    BW_MHz = ap['BW_MHz']
    RBs = bwMHz_rb[BW_MHz]
    SCs = RBs*12
    PwSC_mW = ap['RRU_Power_W']*1000/SCs
    PwSC_dBm = mW2dBm(PwSC_mW) + ap['AntGain_dB'] + ap['CblLoss_dB']
    return PwSC_dBm


# print("power_per_SC_dBm =", power_per_SC_dBm(bs_pars))    
assert  round( txpower_per_SC_dBm(raps[0]) )==25

#%%
'''
Assume Path Loss formula
 L_dB = 128.1 + 37.6*log10(d_km)
and  d_km = 3
So L_dB = 146.03
Calculate pathloss for a UE = -132 dB, so the 
RSRP = -132dB + 25dBm = -107dBm
RSRP = Reference Signal Received Power

SINR = ReceivedPower / (Noise + Interf)

Noise_dB = -125
'''
def ploss_km2db(d_km):
    L_dB = 128.1 + 37.6*numpy.log10(d_km)
    return L_dB

# compute RSRP for a UE with coordinates x and y served by Access Point ap
def rxpower_per_SC_dBm(ap, d_km):
    return  txpower_per_SC_dBm(ap) - ploss_km2db(d_km) 
     

#def power_received_by_UE_dBm(bspars, d_km):
#    PL_dBm = power_per_SC_dBm(bspars) - ploss_km2db(d_km) 
#    return PL_dBm

assert round( txpower_per_SC_dBm(raps[0]) )==25
assert round(ploss_km2db(d_km=3))==146
assert round(rxpower_per_SC_dBm(raps[0], d_km=1.1)) == -104
#%%
# compute SINR
# '''
# Ref: http://www.techplayon.com/signal-to-interference-and-noise-ratio-snir/
# Noise Power (dBm)= -174 +10*log(Bandwidth in Hz) = -174 + 10*log(15*1000) =-132.23 dBm
# '''
# Noise_dBm = -174 + 10*numpy.log10(BW_MHz*1000)
# Interferance_dBm = - 113
# print("Noise_dBm = ",    round(Noise_dBm,2) ,  " ; Interferance_dBm = ",  round(Interferance_dBm,2)   )
# print("Noise_mW = ", dBm2mW(-125.23))
# print("Interferance_mW = ", dBm2mW(-113))

# '''
# Noise_dBm = -125
# Lin SINR = lin (-107.34) / Lin(Noise = -125) + Lin(Interference = -113)
# SINR dB = 5.4
# '''
def SINR_dB(rxp_dBm, Noise_dBm, Interferance_dBm ):
    SINRlin = dBm2mW(rxp_dBm) / (   dBm2mW(Noise_dBm)  + dBm2mW(Interferance_dBm)    )
    SINR_dB = PowerRatio2dB(SINRlin)
    return SINR_dB

def SINR_dB2( ap, d_km ):
    rxp_dBm =  txpower_per_SC_dBm(ap) - ploss_km2db(d_km)
    SINRlin = dBm2mW(rxp_dBm) / (   dBm2mW(Noise_dBm)  + dBm2mW(Interferance_dBm)    )
    SINR_dB = PowerRatio2dB(SINRlin)
    return SINR_dB

# http://www.techplayon.com/signal-to-interference-and-noise-ratio-snir/
# Noise Power (dBm)= -174 +10*log(Bandwidth in Hz)    
def noise_level_dBm(BW_Hz):
    return -174 +10*numpy.log10(BW_Hz)    

def SC_noise_level_dBm(ap):
    BW_MHz = ap['BW_MHz']
    RBs = bwMHz_rb[BW_MHz]
    SCs = RBs*12
    SCBW_Hz = ap['BW_MHz']*1000000/SCs
    return -174 +10*numpy.log10(SCBW_Hz)
#%%
SC_noise_level_dBm(raps[0])    
#%%
rxpower_per_SC_dBm(raps[0], d_km=0.5)

rxp_dBm=-91
Noise_dBm=-125
Interferance_dBm=-113

rxp_dBm=-91
Noise_dBm=-131
Interferance_dBm=-110

SINR_dB(rxp_dBm, Noise_dBm, Interferance_dBm )
'''
print(rxp_dBm, Noise_dBm, Interferance_dBm)
print(dBm2mW(rxp_dBm), dBm2mW(Noise_dBm), dBm2mW(Interferance_dBm))
print(dBm2mW(rxp_dBm), dBm2mW(Noise_dBm)+ dBm2mW(Interferance_dBm))
print(dBm2mW(rxp_dBm)/ (dBm2mW(Noise_dBm)+ dBm2mW(Interferance_dBm) ) )
print(  PowerRatio2dB( dBm2mW(rxp_dBm)/ (dBm2mW(Noise_dBm)+ dBm2mW(Interferance_dBm) )  )  )
'''

#%%
Interferance_dBm=-113
Noise_dBm=-125.23
rxp_dBm=-107.34
assert round(SINR_dB(rxp_dBm=-107.34, Noise_dBm=-125.23, Interferance_dBm=-113 ),1) == 5.4
#%%
import random
#import numpy
def gen_mobiles(B, N):
    x=[random.uniform(-B, B) for _ in range(N)]
    y=[random.uniform(-B, B) for _ in range(N)]
    return numpy.asarray(x),numpy.asarray(y)

# def gen_mobiles2(B, N):
#     x=[random.uniform(-B, B) for _ in range(N)]
#     y=[random.uniform(-B, B) for _ in range(N)]
#     d=numpy.power(numpy.square(x) + numpy.square(y), 0.5)/1000
#     return numpy.asarray(x),numpy.asarray(y),d

def compute_dist(x,y,enb):
    x=x-enb['x']
    y=y-enb['y']
    d=numpy.power(numpy.square(x) + numpy.square(y), 0.5)/1000
    d= [0.1 if dd<0.1 else dd for dd in d]
    return d

#%%

# '''
# BW=20MHz ==> 100 RBs = 12 SC/RB *100 RB = 1200 SC 
# RRU_Power_W = 20W (RRU Power 20W),  
# power_per_SC_mW = 20000/1200  =  100/6 = 16.6 mW/SC   ==>   in power_per_SC_dBm = 12.21 dBm
# Assuming 16dB antenna gain, 3dB cable loss 
# updated_power_per_SC_dBm = 12.21dBm + 16dB - 3dB  = 25.21 dBm
# '''

# # RRU_Power_W = 20
# # BW_MHz = 20
# # RBs = bwMHz_rb[BW_MHz]
# # SCs = RBs*12
# # print("BW_MHz =",BW_MHz, ";  RBs =", RBs, ";  SCs =",SCs)
# # PwSC_mW = RRU_Power_W*1000/SCs
# # PwSC_dBm = mW2dBm(PwSC_mW)

# # AntGain_dB = 16
# # CableLoss_dB = -3
# # print( "antenna gain ratio = ",  dB2PowerRatio(AntGain_dB))
# # print( "cable loss ratio = ",  dB2PowerRatio(CableLoss_dB))

# # def power_per_SC_dBm(BW_MHz, RRU_Power_W):
# #     RBs = bwMHz_rb[BW_MHz]
# #     SCs = RBs*12
# #     PwSC_mW = RRU_Power_W*1000/SCs
# #     PwSC_dBm = mW2dBm(PwSC_mW)
# #     return PwSC_dBm
#%%
import matplotlib.pyplot as plt    
def show_mobiles2(x,y,  uecolorstr, B=1000):
    x = numpy.asarray(x)
    y = numpy.asarray(y)
    plt.plot(x,y, 'ro', color=uecolorstr)
    plt.axis([-B, B, -B, B])
    plt.show()

#def show_mobiles(x,y, center_x, center_y, uecolorstr, B=1000):
#    x = numpy.asarray(x) + center_x
#    y = numpy.asarray(y) + center_y
#    plt.plot(x, y, 'ro', color=uecolorstr)
#    plt.axis([center_x-B, center_x+B, center_y-B, center_y+B])
#    plt.show()
    
def mark_bs(center_x, center_y, txtmark, bscolorstr='red' ):
    plt.text(center_x, center_y, s=txtmark, bbox=dict(facecolor=bscolorstr, alpha=0.5))

def mark_bs2( enbs, k ):
    mark_bs(center_x=enbs[k]['x'], center_y=enbs[k]['y'], txtmark=enbs[k]['lbl'], bscolorstr='red' )

def mark_ap( ap, colorstr ):
    plt.text( ap['x'], ap['y'], s=ap['lbl'], bbox=dict(facecolor = colorstr, alpha=0.5))
    
    
# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.grid.html
def get_ecdf(x, xlabelstr, colorstr):
    x = numpy.sort(x)
    y = numpy.arange(1, len(x)+1) / len(x)
    _ = plt.plot(x, y, marker='.', linestyle='none', color=colorstr)
    _ = plt.grid(True)
    _ = plt.xlabel(xlabelstr)
    _ = plt.ylabel('CDF')
    plt.margins(0.02)
    plt.show()    
    
#%%
    
import pandas as pd    
def show_three_aps(x,y, raps):

    df = pd.DataFrame({'x':x, 
                       'y':y, 
                       'd0':compute_dist(x,y,raps[0]), 
                       'd1':compute_dist(x,y,raps[1]),
                       'd2':compute_dist(x,y,raps[2])
                      }) 
    df['rpdBm0']=rxpower_per_SC_dBm(ap=raps[0], d_km=df['d0'])
    df['rpdBm1']=rxpower_per_SC_dBm(ap=raps[1], d_km=df['d1'])
    df['rpdBm2']=rxpower_per_SC_dBm(ap=raps[2], d_km=df['d2'])
    
    sinr0 = SINR_dB( rxp_dBm=df['rpdBm0'], 
                    Noise_dBm = SC_noise_level_dBm(raps[0])  , 
                    Interferance_dBm = df['rpdBm1'] + df['rpdBm2'] )
    
    sinr1 = SINR_dB( rxp_dBm=df['rpdBm1'], 
                    Noise_dBm=SC_noise_level_dBm(raps[1]), 
                    Interferance_dBm = df['rpdBm0'] + df['rpdBm2'] )
    
    sinr2 = SINR_dB( rxp_dBm=df['rpdBm2'], 
                    Noise_dBm=SC_noise_level_dBm(raps[2]), 
                    Interferance_dBm = df['rpdBm0'] + df['rpdBm1'] )
    
    df['sinr0']=sinr0
    df['sinr1']=sinr1
    df['sinr2']=sinr2
    df['best']=0
    
    for i in range(len(sinr0)):
        a=[sinr0[i], sinr1[i], sinr2[i]]
        df['best'][i] = a.index(max(a))    
        
    df0=df[df['best']==0]
    df1=df[df['best']==1]
    df2=df[df['best']==2]        

    #%matplotlib notebook
    #import matplotlib.pyplot as plt
    plt.rcParams["figure.figsize"] = (10,4)
    plt.subplot(121)
    show_mobiles2(x=df0['x'],y=df0['y'], uecolorstr='green',  B=1000)
    show_mobiles2(x=df1['x'],y=df1['y'], uecolorstr='cyan',  B=1000)
    show_mobiles2(x=df2['x'],y=df2['y'], uecolorstr='pink',  B=1000)
    
    mark_ap( ap=raps[0], colorstr='red' )
    mark_ap( ap=raps[1], colorstr='red' )
    mark_ap( ap=raps[2], colorstr='red' )
    
    plt.show()
    
    plt.subplot(122)
    
    get_ecdf(x=df0['sinr0'], xlabelstr='SINR', colorstr='green')
    get_ecdf(x=df1['sinr1'], xlabelstr='SINR', colorstr='cyan')
    get_ecdf(x=df2['sinr2'], xlabelstr='SINR', colorstr='pink')
    
    plt.show()        
