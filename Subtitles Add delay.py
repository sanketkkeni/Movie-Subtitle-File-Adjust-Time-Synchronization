import re
import datetime
from datetime import timedelta

########Inputs#########
subtitle_filepath = 'C:\\Users\\sanke\\Downloads\\sub.srt'
output_file = 'C:\\Users\\sanke\\Downloads\\sub_python.srt'
adjust_seconds = -20
#######################

####Calling the main function#####
create_outputFile()
###############################

#Helper functions
def read_file():
    with open(subtitle_filepath,'r') as f:
        Lines = f.readlines()
    return Lines

def adj_time(time_obj, incr_sec):
    incr_millisec = incr_sec * 1000
    out_time_obj = time_obj + timedelta(milliseconds = incr_millisec)
    return out_time_obj

def two_digitize(num):
    out = '00'+ str(int(num))[:2]
    return out[-2:]

def three_digitize(num):
    out = '000'+ str(int(num))[:3]
    return out[-3:]

def print_time(time_obj):
    if (time_obj.year == 1899):
        return '00:00:00,000 --> 00:00:00,000'    
    millisec = (time_obj.microsecond/1000)
    sec = time_obj.second
    minute = time_obj.minute
    hr = time_obj.hour
    return two_digitize(hr) + ':' + two_digitize(minute) + ':' + two_digitize(sec) + ',' + three_digitize(millisec)

def add_time(time_string):
        result = re.search('(.*) --> (.*)', time_string)
        
        start_time_obj = datetime.datetime.strptime(result.group(1), '%H:%M:%S,%f')
        end_time_obj = datetime.datetime.strptime(result.group(2), '%H:%M:%S,%f')
        
        adj_start_time_obj = adj_time(start_time_obj, adjust_seconds)
        adj_end_time_obj = adj_time(end_time_obj, adjust_seconds)
        
        
        out = print_time(adj_start_time_obj) + ' --> ' + print_time(adj_end_time_obj) + '\n'
        return out
    
def create_outputFile():
    Lines = read_file()
    srt_out = ''
    regexp = re.compile(r'[0-9]:[0-9]:*')
    for i in Lines:
        if (regexp.search(i)): 
            srt_out += add_time(i)
        else:
            srt_out += i

    with open(output_file,'w') as f:
        f.write(srt_out)

