import requests
import json
import pandas as pd
from models import *
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

class Results:

    def get_results(date,events):
        data = []
        for i in range(0, events, 100):
            url = 'https://api.fda.gov/drug/event.json?api_key=iQLpf10vDEd4qDbJfIXK9Tm9SYFXo2cCoy4Ghv62&search=receivedate:' + str(date) + '&limit=100'+'&skip='+str(i)
            r = requests.get(url)
            jsoning_data = r.json()
            data += list(jsoning_data['results'])
        return data

class Instantiating_Holidays:

    def holidays(event): #change to holiday_json later
            if event['receiptdate'] == '20171231':
                holiday = 'New Years Eve'
            elif event['receiptdate'] == '20171031':
                holiday = 'Halloween'
            elif event['receiptdate'] == '20170214':
                holiday = 'Valentine\'s Day'
            elif event['receiptdate'] == '20170228':
                holiday = 'Mardi Gras'
#             elif event['receiptdate'] == '20170317':
#                 holiday = 'St. Patrick\'s Day'
            elif event['receiptdate'] == '20170420':
                holiday = 'Cannabis Day'
            elif event['receiptdate'] == '20170505':
                holiday = 'Cinco de Mayo'
            elif event['receiptdate'] == '20170704':
                holiday = 'Independence Day'
            elif event['receiptdate'] == '20171123':
                holiday = 'Thanksgiving'
            elif event['receiptdate'] == '20171225':
                holiday = 'Christmas'

            holiday_name = Holidays(name=holiday,date=str(event['receiptdate']))
            return holiday_name

## GLOBAL FUNCTIONS

def sex(event):
    patients = []
    sex = []
    if 'patient' in event:
        sex.append(event['patient'])
    else:
        sex.append('None')
    for i in sex:
        if 'patientsex' in i:
            patients.append(int(i['patientsex']))
        else:
            patients.append("None")
    return patients[0]


def age(event):
    patients = []
    ages = []
#     if 'patient' in event:
#         ages.append(event['patient'])
#     else:
#         ages.append('None')
#     for i in ages:
#         if 'patientonsetage' in i:
#             patients.append(int(i['patientonsetage']))
#         else:
#             patients.append('None')
#     return patients[0]
    ages_list = []
    if 'patient' in event:
        ages.append(event['patient'])
    else:
        ages.append('None')
    for i in ages:
        if 'patientonsetage' in i:
            patients.append(i['patientonsetage'])
        else:
            patients.append(0)
    for x in patients:
        if x == None:
            ages_list.append(str(x))
        else:
            ages_list.append(int(x))

    return ages_list[0]


class Instantiating_Events:

    def event_object(date,events):
        holiday_json = Results.get_results(date,events)
        our_holiday = Instantiating_Holidays.holidays(holiday_json[0])

        for event in holiday_json:
            sex_func = sex(event)
            age_func = age(event)
            new_event = Adverse_Events(sex=sex_func, age=age_func, holidays = our_holiday)


            b = []
            if 'openfda' in event['patient']['drug'][0]:
                    if 'brand_name' in event['patient']['drug'][0]['openfda']:
                        b.extend(event['patient']['drug'][0]['openfda']['brand_name'])
                    else:
                        b.extend('None')

            brand_list = []
            for brand in b:
                brand_result = session.query(Brands).filter(Brands.name == brand).first()
                if brand_result:
                    brand_list.append(brand_result)
                else:
                    brand_list.append(Brands(name=brand))
            new_event.brands = brand_list




            reactions =  event['patient']['reaction']
            list_of_reactions = []
            for reaction in reactions:
                list_of_reactions.append(reaction['reactionmeddrapt'])

            reaction_list = []
            for reaction in list_of_reactions:
                reaction_result = session.query(Reactions).filter(Reactions.name == reaction).first()
                if reaction_result:
                    reaction_list.append(reaction_result)
                else:
                    reaction_list.append(Reactions(name=reaction))
            new_event.reactions = list(set(reaction_list))


            session.add(new_event)
            session.commit()



Instantiating_Events.event_object(20171231,400)


# new_years_eve = get_results(20171231, 400) #347
# valentines_day = get_results(20170214, 4100) #4063
# mardi_gras = get_results(20170228, 4400) #4317
# st_patricks_day = get_results(20170317, 3600) #3570
# cannabis_day = get_results(20170420, 5300) #5242
# cinco_mayo = get_results(20170505, 3900) #3805
# independence_day = get_results(20170704, 2700) #2617
# halloween = get_results(20171031, 4000) #3922
# thanksgiving = get_results(20171123, 3500) #3494
# christmas = get_results(20171225, 1000) #939
