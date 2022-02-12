import pandas as pd
import numpy as np
import flood_predictor as fp
import geocoder

tables = pd.read_csv("input.csv")

states = {'ANDAMAN & NICOBAR ISLANDS': 0, 'ARUNACHAL PRADESH':2, 'ASSAM':	4, 'MEGHALAYA':	23,'NAGALAND': 25,'MANIPUR':22,'MIZORAM':24,'TRIPURA': 33,
'SIKKIM':30,'WEST BENGAL':	36,'ORISSA':	26,'JHARKHAND':	15,'BIHAR'	:5,'UTTAR PRADESH':	34,'UTTARAKHAND':	35,'HARYANA':	12,'DELHI'	:9,'CHANDIGARH':6,
'PUNJAB':28,'HIMACHAL PRADESH':	13,'JAMMU & KASHMIR':14,'LADAKH':18,'RAJASTHAN':29,'MADHYA PRADESH':20,'DAMAN AND DIU':8,'GUJARAT':11,'GOA':10,
'MAHARASHTRA':21,'CHHATTISGARH':7,'ANDHRA PRADESH':1,'TELANGANA':32,'TAMIL NADU':31,'PUDUCHERRY':27,'KARNATAKA':	16,'KERALA':17,'LAKSHADWEEP':19}

tables=np.array(tables[1:])
# print(tables)
def get_location():
    g = geocoder.ip('103.103.52.40')
    state_cur=g.state
    # print(g.state)
    state_cur=state_cur.upper()
    # print(str(state_cur))
    return state_cur
def get_rain():
    a=max(tables[tables[:,0]==get_location()][:,1].flatten())
    return a
#print(get_location)
def predict():
    # print(states[get_location()])
    # print(get_rain())
    return fp.prediction1([[states[get_location()],get_rain()]])
def alert():
    var=predict()
    if(var==0):
        return "You are completely safe"
    elif(var==1):
        return "Moderate rain falling, keep your umbrella with you, but you're safe"
    elif(var==2):
        return "Heavy raining, chances of floods increasing. Please take necessary precations "
    else:
        return "Flood chances are at peak.Stay in your house"



