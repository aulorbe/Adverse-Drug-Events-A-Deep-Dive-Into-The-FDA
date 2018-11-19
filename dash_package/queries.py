from sqlalchemy import create_engine, func, or_
from dash_package import app,db
from sqlalchemy.orm import sessionmaker
import numpy as np
import operator
from dash_package.models import Adverse_Events, Brands, Brands_Events, Reactions, Reactions_Events, Holidays





engine = create_engine('sqlite:///adverse-events.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

def find_total_number_of_events_one_holiday(holiday): # format of holiday input = 'Christmas' format
    all = db.session.query(Adverse_Events).join(Holidays).filter(Holidays.name==holiday).all()
    return len(all)


def male_events_in_one_holiday(holiday): # format of holiday input = 'Christmas' format
    all_holidays = db.session.query(Adverse_Events).join(Holidays).filter(Holidays.name==holiday).all()
    sex = []
    for i in all_holidays:
        if i.sex==1:
            sex.append(i)
    return len(sex)

def female_events_in_one_holiday(holiday): # format of holiday input = 'Christmas' format
    all_holidays = db.session.query(Adverse_Events).join(Holidays).filter(Holidays.name==holiday).all()
    sex = []
    for i in all_holidays:
        if i.sex==2:
            sex.append(i)
    return len(sex)


def find_all_brands_in_one_holiday(holiday):
    return db.session.query(Brands.name).join(Brands_Events).join(Adverse_Events).join(Holidays).filter(Holidays.name==holiday).all()

def top_five_brands_names_in_one_holiday(holiday):
    all_brands = db.session.query(Brands.name).join(Brands_Events).join(Adverse_Events).join(Holidays).filter(Holidays.name==holiday).all()
    counter = {}
    for i in all_brands:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    sorted_list_of_tupes = sorted(counter.items(), key=operator.itemgetter(1), reverse=True)
    output = []
    counter_2 = 0
    for i in sorted_list_of_tupes:
        if counter_2 > 4:
            break
        output.append(i)
        counter_2 += 1
    brand_names = []
    for i in output:
        brand_names.append(i[0])

    return brand_names

def top_five_brands_count_in_one_holiday(holiday):
    all_brands = db.session.query(Brands.name).join(Brands_Events).join(Adverse_Events).join(Holidays).filter(Holidays.name==holiday).all()
    counter = {}
    for i in all_brands:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    sorted_list_of_tupes = sorted(counter.items(), key=operator.itemgetter(1), reverse=True)
    output = []
    counter_2 = 0
    for i in sorted_list_of_tupes:
        if counter_2 > 4:
            break
        output.append(i)
        counter_2 += 1
    brand_names = []
    for i in output:
        brand_names.append(i[1])

    return brand_names

def top_five_reactions_count_in_one_holiday(holiday):
    all_reactions = db.session.query(Reactions.name).join(Reactions_Events).join(Adverse_Events).join(Holidays).filter(Holidays.name==holiday).all()
    counter = {}
    for i in all_reactions:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    sorted_list_of_tupes = sorted(counter.items(), key=operator.itemgetter(1), reverse=True)
    output = []
    counter_2 = 0
    for i in sorted_list_of_tupes:
        if counter_2 > 4:
            break
        output.append(i)
        counter_2 += 1
    reaction_names = []
    for i in output:
        reaction_names.append(i[1])

    return reaction_names


def top_five_reaction_names_in_one_holiday(holiday):
    all_reactions = db.session.query(Reactions.name).join(Reactions_Events).join(Adverse_Events).join(Holidays).filter(Holidays.name==holiday).all()
    counter = {}
    for i in all_reactions:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    sorted_list_of_tupes = sorted(counter.items(), key=operator.itemgetter(1), reverse=True)
    output = []
    counter_2 = 0
    for i in sorted_list_of_tupes:
        if counter_2 > 4:
            break
        output.append(i)
        counter_2 += 1
    reaction_names = []
    for i in output:
        reaction_names.append(i[0])

    return reaction_names




def find_count_of_brands_in_one_holiday(holiday):
    return len(db.session.query(Brands.name).join(Brands_Events).join(Adverse_Events).join(Holidays).filter(Holidays.name==holiday).all())


def find_all_reactions_in_one_holiday(holiday):
    return  db.session.query(Reactions.name).join(Reactions_Events).join(Adverse_Events).join(Holidays).filter(Holidays.name==holiday).all()
#
#
def find_count_of_reactions_in_one_holiday(holiday):
    return  len(db.session.query(Reactions.name).join(Reactions_Events).join(Adverse_Events).join(Holidays).filter(Holidays.name==holiday).all())

# def average_age_of_all_events():
#     age_results = session.query(Adverse_Events.age).filter(Adverse_Events.age != 'None').all()
#     list_of_ages = []
#     for i in age_results:
#         for y in i:
#             list_of_ages.append(y)
#     for i in list_of_ages:
#     #     if i > 24:
    #         list_of_ages.remove(i)
    # return list_of_ages
    # round(80.23456, 2)

def men():
    return len(db.session.query(Adverse_Events.sex).filter(Adverse_Events.sex == 1).all())

def women():
    return len(db.session.query(Adverse_Events.sex).filter(Adverse_Events.sex == 2).all())

def percent_men_and_women_across_all_events():
    men = len(db.session.query(Adverse_Events.sex).filter(Adverse_Events.sex == 1).all())
    women = len(db.session.query(Adverse_Events.sex).filter(Adverse_Events.sex == 2).all())
    total = men+women
    percent_men = round((men/total)*100,2)
    percent_women = round((women/total)*100,2)
    return f'Men make up {percent_men}% of total events, while women make up {percent_women}% of total events'

def holiday_with_most_events():

    num_christmas_events = len(db.session.query(Adverse_Events.id).join(Adverse_Events.holidays).filter(Holidays.name == 'Christmas').all())

    num_new_years_eve_events = len(db.session.query(Adverse_Events.id).join(Adverse_Events.holidays).filter(Holidays.name == 'New Years Eve').all())

    num_valentines_day = len(db.session.query(Adverse_Events.id).join(Adverse_Events.holidays).filter(Holidays.name == 'Valentine\'s Day').all())

    num_mardi_gras = len(db.session.query(Adverse_Events.id).join(Adverse_Events.holidays).filter(Holidays.name == 'Mardi Gras').all())

    num_cannabis_day = len(db.session.query(Adverse_Events.id).join(Adverse_Events.holidays).filter(Holidays.name == 'Cannabis Day').all())

    num_cinco_mayo = len(db.session.query(Adverse_Events.id).join(Adverse_Events.holidays).filter(Holidays.name == 'Cinco de Mayo').all())

    num_independence_day = len(db.session.query(Adverse_Events.id).join(Adverse_Events.holidays).filter(Holidays.name == 'Independence Day').all())

    num_halloween = len(db.session.query(Adverse_Events.id).join(Adverse_Events.holidays).filter(Holidays.name == 'Halloween').all())

    thanksgiving = len(db.session.query(Adverse_Events.id).join(Adverse_Events.holidays).filter(Holidays.name == 'Thanksgiving').all())

    events_dict = {'Christmas': num_christmas_events, 'New Years Eve': num_new_years_eve_events, 'Valentine\'s Day': num_valentines_day, 'Mardi Gras': num_mardi_gras, 'Cannabis Day': num_cannabis_day, 'Cinco de Mayo': num_cinco_mayo,'Independence Day': num_independence_day, 'Halloween': num_halloween, 'Thanksgiving': thanksgiving}

    most_events_holiday = max(events_dict, key=events_dict.get)
    return 'The holiday with the highest number of adverse events was ' + most_events_holiday + ', with ' + str(events_dict[most_events_holiday]) + ' adverse events.'


def deaths_per_holiday(holiday):
    return len(db.session.query(Reactions.name).join(Reactions_Events).join(Adverse_Events).join(Holidays).filter(Holidays.name==holiday,
    or_(Reactions.name=='Death', Reactions.name=='Sudden death')).all())


def attempted_suicides_per_holiday(holiday):
    return len(db.session.query(Reactions.name).join(Reactions_Events).join(Adverse_Events).join(Holidays).filter(Holidays.name==holiday,Reactions.name == 'Suicide attempt', Adverse_Events.age > 6).all())


def suicides_per_holiday(holiday): # how to filter out weird gigantic numbers that aren't ages, but are in our dataset?
    return len(db.session.query(Reactions.name).join(Reactions_Events).join(Adverse_Events).join(Holidays).filter(Holidays.name==holiday,Reactions.name == 'Completed suicide', Adverse_Events.age > 6).all())


def most_common_reaction():
    list_of_all_reactions_in_all_events = db.session.query(Reactions.name).join(Reactions_Events).join(Adverse_Events).all()
    list_of_cleaned_reactions = []
    for i in list_of_all_reactions_in_all_events:
        for y in i:
            list_of_cleaned_reactions.append(y)
    dict_of_reactions = {}
    for i in list_of_cleaned_reactions:
        if i in dict_of_reactions:
            dict_of_reactions[i] += 1
        else:
            dict_of_reactions[i] = 1
    maximum = max(dict_of_reactions, key=dict_of_reactions.get)
    return (maximum, dict_of_reactions[maximum])


def top_five_most_common_reactions():
    list_of_all_reactions_in_all_events = db.session.query(Reactions.name).join(Reactions_Events).join(Adverse_Events).all()
    list_of_cleaned_reactions = []
    for i in list_of_all_reactions_in_all_events:
        for y in i:
            list_of_cleaned_reactions.append(y)
    dict_of_reactions = {}
    for i in list_of_cleaned_reactions:
        if i in dict_of_reactions:
            dict_of_reactions[i] += 1
        else:
            dict_of_reactions[i] = 1
    sorted_list_of_tupes = sorted(dict_of_reactions.items(), key=operator.itemgetter(1))
    return sorted_list_of_tupes[-5:]


def most_common_brands():
    list_of_all_brands_in_all_events = db.session.query(Brands.name).join(Brands_Events).join(Adverse_Events).all()
    list_of_cleaned_brands = []
    for i in list_of_all_brands_in_all_events:
        for y in i:
            list_of_cleaned_brands.append(y)
    dict_of_brands = {}
    for i in list_of_cleaned_brands:
        if i in dict_of_brands:
            dict_of_brands[i] += 1
        else:
            dict_of_brands[i] = 1
    maximum = max(dict_of_brands, key=dict_of_brands.get)
    return (maximum, dict_of_brands[maximum])


def top_five_most_common_brands():
    list_of_all_brands_in_all_events = db.session.query(Brands.name).join(Brands_Events).join(Adverse_Events).all()
    list_of_cleaned_brands = []
    for i in list_of_all_brands_in_all_events:
        for y in i:
            list_of_cleaned_brands.append(y)
    dict_of_brands = {}
    for i in list_of_cleaned_brands:
        if i in dict_of_brands:
            dict_of_brands[i] += 1
        else:
            dict_of_brands[i] = 1
    sorted_list_of_tupes = sorted(dict_of_brands.items(), key=operator.itemgetter(1))
    return sorted_list_of_tupes[-5:]


def death_top_five_brands():
    list_of_all_brands_in_all_events = db.session.query(Brands.name).join(Brands_Events).join(Adverse_Events).join(Reactions_Events).join(Reactions).filter(or_(Reactions.name=='Death', Reactions.name=='Sudden death')).all()
    list_of_cleaned_brands = []
    for i in list_of_all_brands_in_all_events:
        for y in i:
            list_of_cleaned_brands.append(y)
    dict_of_brands = {}
    for i in list_of_cleaned_brands:
        if i in dict_of_brands:
            dict_of_brands[i] += 1
        else:
            dict_of_brands[i] = 1
    sorted_list_of_tupes = sorted(dict_of_brands.items(), key=operator.itemgetter(1))
    return sorted_list_of_tupes[-5:]




# def holiday_with_most_males():
#     pass

# def holiday_with_most_females():
#     pass
#
# def holiday_with_oldest_person():
#     pass
#
# def holiday_with_youngest_person():
#     pass

# def men_and_women_per_holiday(holiday):
#     pass
#
# def age_groups_per_holiday(holiday):
#     pass

# def find_all_sex():
#     return session.query(Adverse_Events.sex).all()
#
# def find_all_age():
#     return session.query(Adverse_Events.age).all()
#
# def find_how_many_female():
#     return session.query(Adverse_Events).filter_by(Adverse_Events.age = 1).all()
#
# def find_how_many_male():
#     return session.query(Adverse_Events).filter_by(Adverse_Events.age = 2).all()
