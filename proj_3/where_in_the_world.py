#Samuel Terry
#Etude 3, Where in the World
import re 
import sys
import math
from operator import and_, or_, contains

#Helper method for directions recogniser that deals with compass_directions and reverses.
def get_directions(a,b):
    if b == 'N':
        return abs(float(a))
    elif b == 'S':
        return -abs(float(a))
    elif b == 'W':
        return -abs(float(a))
    elif b == 'E':
        return abs(float(a))

#Replaces commas in input string with white space and then splits by white space.
def split_line(line):
    tokens = line.rstrip()
    tokens = line.replace(',', ' ')
    tokens = tokens.split()
    return tokens

#If a recogniser was successful then it is converted into standard form.
def convert(lat, lon, label):
    lat = format(lat, '.6f')
    lon = format(lon, '.6f')
    ok = lat + lon + label   
    print("{} {} ".format(lat, lon))

#Helper method - Checks d/m/s for in range
def in_range_dms(d,m,s):
    d = get_float(d)
    m = get_float(m)
    s = get_float(s)
    if (math.floor(d) in range(361)) and (math.floor(m) in range(61)) and (math.floor(s) in range(61)):
        return True
    else:
        return False

#Helper method - Checks lat/lon for in range
def in_range_lat_lon(lat, lon):  
    lat = get_float(lat)
    lon = get_float(lon)
    if (lat >= -90 and lat <= 90) and (lon >= -180 and lon <= 180):
        return True
    else:
        return False

#Tries to convert something to a float, if it cannot be casted to a float it returns None type.
def get_float(s):
    try:
        return float(s)
    except:
        return None

def calculate(d,m,s):
    d = get_float(d)
    m = get_float(m)
    s = get_float(s)
    decimal_degrees = d + (m/60) + (s/3600)
    return decimal_degrees

def convert_degrees_minute_decimal_to_normal(dm_list):
    if dm_list[1] == 'd' and dm_list[3] == 'm' and 's' not in dm_list:
        d = get_float(dm_list[0])
        s = 60 * (get_float(dm_list[2]) - math.floor(get_float(dm_list[2])))
        m = get_float(dm_list[2]) - s
        orientation = dm_list[4]
        if in_range_dms(d,m,s):
            converted_dms = calculate(d,m,s)
            return converted_dms, orientation
        else:
            return False
    else:
        return False

def convert_degrees_minutes_seconds_to_normal(dms_list):
    if dms_list[1] == 'd' and dms_list[3] == 'm' and dms_list[5] =='s' and (get_float(dms_list[2]) % 1) ==0 :
        d = get_float(dms_list[0]) 
        m = get_float(dms_list[2])
        s = get_float(dms_list[4])
        orientation = dms_list[6]
        if in_range_dms(d,m,s):
            converted_dms = calculate(d,m,s)
            return converted_dms, orientation
        else:
            return False
    else:
        return False

#Recogniser deals with compass directions and reversals.
def recognise_compass_directions(line):
    try: 
        tokens = split_line(line)
        lat_list = ['N', 'S']
        lon_list =  ['E', 'W'] 
        if len(tokens) >= 4 and ((get_float(tokens[0]) and get_float(tokens[2])) != None) and (tokens[1] in lat_list and tokens[3] in lon_list):
            lat = get_directions(tokens[0], tokens[1])
            lon = get_directions(tokens[2], tokens[3])
            if in_range_lat_lon(lat,lon):
                return float(lat), float(lon), "", True
            else:
                return None, None, None, False
        elif len(tokens) >= 4 and ((get_float(tokens[0]) and get_float(tokens[2])) != None) and tokens[1] in lon_list and tokens[3] in lat_list:
            lon = get_directions(tokens[0], tokens[1])
            lat = get_directions(tokens[2], tokens[3])
            if in_range_lat_lon(lat,lon):
                return float(lat), float(lon), "", True
            else:
                return None, None, None, False   
        else:
                return None, None, None, False
    except:
        return None, None, None, False

#Recogniser for input resembling standard form OR two numbers.
def recognise_standard_form(line):
    try :
        tokens = split_line(line)
        if len(tokens) < 2:
            return None, None, None, False
        lat = get_float(tokens[0])
        lon = get_float(tokens[1])
        if (lat != None and lon != None) and (in_range_lat_lon(lat,lon) == True) and (len(tokens) >= 2):                                             
            return lat, lon, "", True
        else:
            return None, None, None, False  
    except:
        return None, None, None, False      

def recognise_degrees_minutes_seconds_form(line):
    try :
        tokens = split_line(line)
        middle_index = (len(tokens)//2)
        lat = tokens[:middle_index]
        lon = tokens[middle_index:]
        if len(tokens) == 14 and convert_degrees_minutes_seconds_to_normal(lat) and convert_degrees_minutes_seconds_to_normal(lon):
            lat,orientation_lat = convert_degrees_minutes_seconds_to_normal(lat)
            lon,orientation_lon = convert_degrees_minutes_seconds_to_normal(lon)
            if orientation_lat != orientation_lon:
                lat = get_directions(lat,orientation_lat)
                lon = get_directions(lon,orientation_lon)
                if in_range_lat_lon(lat,lon):
                    return lat, lon, "" , True        
                else:
                    return None, None, None, False
            else:
                return None, None, None, False
        else:
            return None, None, None, False
    except:
        None, None, None, False
def recognise_degrees_minutes_decimal_form(line):
    try :
        tokens = split_line(line)
        middle_index = (len(tokens)//2)
        lat = tokens[:middle_index]
        lon = tokens[middle_index:]
        if convert_degrees_minute_decimal_to_normal(lat) and convert_degrees_minute_decimal_to_normal(lon) and len(tokens) == 10:
            lat,orientation_lat = convert_degrees_minute_decimal_to_normal(lat)
            lon,orientation_lon = convert_degrees_minute_decimal_to_normal(lon)
            if (orientation_lat != None or orientation_lat != None) and orientation_lat != orientation_lon:
                lat = get_directions(lat,orientation_lat)               
                lon = get_directions(lon,orientation_lon)
                if (lat != None and lon != None) and in_range_lat_lon(lat,lon):           
                    return lat, lon, "", True   
                else:
                    return None, None, None, False    
            else:
                return None, None, None, False 
        else:
            return None, None, None, False
    except:
        return None, None, None, False
def main():
    for line in sys.stdin:
        lat,lon,label, success = recognise_compass_directions(line)
        if success:
            convert(lat,lon,label)
            continue
        lat,lon,label, success = recognise_standard_form(line)
        if success:
            convert(lat,lon,label)
            continue
        lat,lon,label, success = recognise_degrees_minutes_decimal_form(line)
        if success:
            convert(lat,lon,label)
            continue
        lat,lon,label, success = recognise_degrees_minutes_seconds_form(line)
        if success:
            convert(lat,lon,label)
            continue
        else:
            print("Unable to process: {} ".format(line))


main()
