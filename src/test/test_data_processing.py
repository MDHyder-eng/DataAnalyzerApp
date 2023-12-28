import sys
sys.path.insert(0, '/absolute/path/to/src/directory')
from data_processing import data_processing as App
from datetime import date
from datetime import datetime

 


print("ReadCSV:")
print(App.readCSV('src\data\311_Service_Requests_small.csv'))
print("")

print("WriteCSV:")
print(
    App.writeCSV('output.csv', [{
        'abby': '51',
        'bell': '62',
        'dee': '33',
        'river': '97'
    }, {
        'abby': '54',
        'bell': '65',
        'dee': '26',
        'river': '71'
    }, {
        'abby': '45',
        'bell': '39',
        'dee': '88',
        'river': '22'
    }, {
        'abby': '57',
        'bell': '68',
        'dee': '39',
        'river': '62'
    }]))
print("")

print("KeepOnly:")
print(
    App.keepOnly([{
        'abby': '51',
        'bell': '62',
        'dee': '33',
        'river': '97'
    }, {
        'abby': '54',
        'bell': '65',
        'dee': '26',
        'river': '71'
    }, {
        'abby': '45',
        'bell': '39',
        'dee': '88',
        'river': '22'
    }, {
        'abby': '57',
        'bell': '68',
        'dee': '26',
        'river': '62'
    }], 'dee', '26'))
print("")

print("DiscardOnly:")
print(
    App.discardOnly([{
        'abby': '51',
        'bell': '62',
        'dee': '33',
        'river': '97'
    }, {
        'abby': '54',
        'bell': '65',
        'dee': '26',
        'river': '71'
    }, {
        'abby': '45',
        'bell': '39',
        'dee': '88',
        'river': '22'
    }, {
        'abby': '57',
        'bell': '68',
        'dee': '26',
        'river': '62'
    }], 'dee', '26'))
print("")

print("FilterRange:")
print(
    App.filterRange([{
        'abby': '51',
        'bell': '62',
        'dee': '33',
        'river': '97'
    }, {
        'abby': '54',
        'bell': '65',
        'dee': '26',
        'river': '71'
    }, {
        'abby': '45',
        'bell': '39',
        'dee': '88',
        'river': '22'
    }, {
        'abby': '57',
        'bell': '68',
        'dee': '26',
        'river': '62'
    }], 'bell', '39', '68'))
print("")

print("Duration:")
print(App.duration(date(2020, 12, 4), date(2020, 11, 8)))
print("")

print("Date:")
print(App.date("04/23/2016 11:37:00 AM"))
print("")

# print(App.data_by_subject({"year_start":2009 , "year_end":2010}))


