#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Nov 30 22:12:18 2021

@author: pi
"""
#-----------------------------------------------------------------------------
#imports used in this program
#-----------------------------------------------------------------------------
import os
import sys
import matplotlib.pyplot as plt
from time import sleep

#------------------------------------------------------------------------------
"""
class MyStruct():
    def __init__(self, app, category, rating, reviews, installs, price):
        self.app = app
        self.category = category
        self.rating = rating
        self.reviews = reviews
        self.installs = installs
        self.price = price
"""
#-----------------------------------------------------------------------------
#Globals
#-----------------------------------------------------------------------------

app = []
category = []
rating = []
reviews = []
installs = []
price = []
uniqueCat = []
global InstSet
InstSet = False
global RevSet
RevSet = False
global RatingSet
RatingSet = False
global catSet
catSet = False
global catFilter
catFilter = ''


#-----------------------------------------------------------------------------
#
#   Function screen_clear()
#   - obs
#
#-----------------------------------------------------------------------------

def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
   
   print('Data Analyst toolkit\n') 

#-----------------------------------------------------------------------------
#
#   using Dictonaries to define the Menu's used in the applicaiton
#
#-----------------------------------------------------------------------------

file_menu_options = {
    1: 'Load a file',
    2: 'Exit'
}

app_menu_options = {
    1: 'Add filters',
    2: 'Print App Names',
    3: 'Graph app',
    4: 'Reset Filters',
    5: 'Exit'
}

filter_menu_options = {
    1: 'Category',
    2: 'Ratings',
    3: 'Reviews',
    4: 'Installs',
    5: 'Exit seting filters'
}

graphing_menu_options = {
    1: 'Category',
    2: 'Ratings',
    3: 'Reviews',
    4: 'Installs',
    5: 'Price',
    6: 'Exit Graphing'
}

#-----------------------------------------------------------------------------
#
#   Printing the various Menus
#
#-----------------------------------------------------------------------------

def print_file_menu():
    for key in file_menu_options.keys():
        print(key, '--', file_menu_options[key])

#-----------------------------------------------------------------------------


def print_app_menu():
    for key in app_menu_options.keys():
        print(key, '--', app_menu_options[key])
#-----------------------------------------------------------------------------


def print_filter_menu():
    for key in filter_menu_options.keys():
        print(key, '--', filter_menu_options[key])
#-----------------------------------------------------------------------------

def print_graphing_menu():
    for key in graphing_menu_options.keys():
        print(key, '--', graphing_menu_options[key])
        
#-----------------------------------------------------------------------------

def print_cat_filter_list():
   #    category
    uniqueCat = list(dict.fromkeys(category))
    for i in range(len(uniqueCat)):
        print(str(i).rjust(2, ' '), '-', uniqueCat[i])

    return uniqueCat
#-----------------------------------------------------------------------------
#   
#   Function to reset filters to run Multiple quieres 
#
#-----------------------------------------------------------------------------

def resetFilters():
    global InstSet
    InstSet = False
    global RevSet
    RevSet = False
    global RatingSet
    RatingSet = False
    global catSet
    catSet = False
    global catFilter
    catFilter =''

#-----------------------------------------------------------------------------
#   
#   Function 
#
#-----------------------------------------------------------------------------

def process_cat_filter():
    uniqueCat = print_cat_filter_list()
    option = 0
    global catSet 
    global catFilter
    try:
        option = int(input('please select a category to filter: '))
    except:
        print('Wrong input. Please enter a number ...')
    if option >= 0 and option <= len(uniqueCat):
        catFilter = uniqueCat[option]
        catSet = True
    else:
        print('Invalid option. Please enter a number between 1 and', len(uniqueCat))
#-----------------------------------------------------------------------------
#   
#   Function 
#
#------------------------------------------------------------------------------

def checkFileExists(fileName):
    fileExists = False
    if os.path.isfile(fileName):
        fileExists=True
    return fileExists
    
    
#-----------------------------------------------------------------------------
#
#   Function LoadFile (Filename)
#   Reads data from a file
#   Returns the data object from the file
#    
#-----------------------------------------------------------------------------

def loadFile(fileName):
        # Open in Read Only Mode
       appFile = open(fileName, "r")
       appData = appFile.readlines()
       appFile.close()
       screen_clear()
       print('File Loaded Successfully')
       sleep(3)
       screen_clear()
       return appData

#-----------------------------------------------------------------------------
#
#   processFileDataForFilters(appData)
#   Processes the data object from a file
#   and loads the filter categories
#   
#   Design Decision:
#       - Missing rating data is set to 3 as a Medium Rating
#         We don't know if it is good or bad  
#    
#-----------------------------------------------------------------------------

def processFileDataForFilters(appData):
    recCounts = 0
    for line in appData:
        splitline = line.strip().split(',')
        if len(splitline) == 1:
            continue
        recCounts = recCounts+1
        if (recCounts > 1):
            app.append(splitline[0])
            category.append(splitline[1])
            reviews.append(splitline[3])
            installs.append(splitline[4])
            price.append(splitline[5])
            if splitline[2] != "":
                rating.append(splitline[2])
            else:
                rating.append(3)
#-----------------------------------------------------------------------------
#
#   Function setlowRating():
#   - This sets the lower rating search value
#     Which must be between 0 and 5
#   - The rating data of the file is a float and thus validating the user
#     data input
#    
#-----------------------------------------------------------------------------


def setlowRating():
    invalid = True
    global lowRating
    while(invalid):
        try:
            lowRating = float(input('please enter low rating: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if lowRating >= 0 and lowRating <= 5:
            invalid = False
        else:
            print('input must be between 0 and 5')

    return lowRating
#-----------------------------------------------------------------------------
#
#   Function sethighRating():
#   - This sets the Higher rating search value
#     Which must be between 0 and 5
#   - The rating data of the file is a float and thus validating the user
#     data input
#    
#-----------------------------------------------------------------------------

def sethighRating():
    invalid = True
    global highRating
    while(invalid):
        try:
            highRating = float(input('please enter high rating: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if highRating >= 0 and highRating <= 5:
            invalid = False
        else:
            print('input must be between 0 and 5')
    return highRating

#-----------------------------------------------------------------------------
#
#   Function setRating()
#   - This function is used to get the lowest and highest ratings for
#     filtering
#     
#   - Function validates to ensure lower rating variable is lower then 
#     the highests so is valid for the filter.
#
#   - The Function sets the filter flag to include in the filter process
#    
#-----------------------------------------------------------------------------


def setRating():
    invalidRating = True
    global RatingSet
    while(invalidRating):
        screen_clear()
        lowRating = setlowRating()
        highRating = sethighRating()

        if highRating < lowRating:
            print('Please ensure high rating is above or equal to low rating')
        else:
            invalidRating = False
            # sets the flag to incldue in the filter processing
            RatingSet = True


#-----------------------------------------------------------------------------
#   
#   Function 
#
#-----------------------------------------------------------------------------

def setLowReviews(maxRevs):
    invalid = True
    global lowReviews
    while(invalid):
        try:
            lowReviews = int(input('please enter lowest number of reviews: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if lowReviews >= 0 and lowReviews <= int(maxRevs):
            invalid = False
        else:
            print('input must be between 0 and', maxRevs)

    return lowReviews

#-----------------------------------------------------------------------------
#   
#   Function 
#
#-----------------------------------------------------------------------------


def setHighReviews(maxRevs):
    invalid = True
    global highReviews
    while(invalid):
        try:
            highReviews = float(input('please enter highest number of reviews: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if highReviews >= 0 and highReviews <= float(maxRevs):
            invalid = False
        else:
            print('input must be between 0 and', maxRevs)
    return highReviews


def getMaxReviews():

    uniqueratings = list(dict.fromkeys(reviews))
    uniqueratings.sort()

    retval = uniqueratings[-1]

    return retval


#-----------------------------------------------------------------------------
#   
#   Function 
#
#-----------------------------------------------------------------------------
def setReviews():
    invalidRating = True
    MaxNumReviews = 0
    global RevSet
    while(invalidRating):
        screen_clear()
        MaxNumReviews = getMaxReviews()
        lowReviews = setLowReviews(MaxNumReviews)
        highReviews = setHighReviews(MaxNumReviews)

        if highReviews < lowReviews:
            print('Please ensure highest rating is above or equal to lowest rating')
        else:
            invalidRating = False
            RevSet = True


#-----------------------------------------------------------------------------
#   
#   Function 
#
#-----------------------------------------------------------------------------

def setLowInstalls(maxInst):
    invalid = True
    global lowInstalls
    while(invalid):
        try:
            lowInstalls = int(input('please enter lowest limit: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if lowInstalls >= 0 and lowInstalls <= int(maxInst):
            invalid = False
        else:
            print('input must be between 0 and', maxInst)

    return lowInstalls

#-----------------------------------------------------------------------------
#   
#   Function 
#
#-----------------------------------------------------------------------------


def setHighInstalls(maxInst):
    invalid = True
    global highInstalls
    while(invalid):
        try:
            highInstalls = int(input('please enter high limit: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if highInstalls >= 0 and highInstalls <= int(maxInst):
            invalid = False
        else:
            print('input must be between 0 and', maxInst)
    return highInstalls

#-----------------------------------------------------------------------------
#   
#   Function 
#
#-----------------------------------------------------------------------------

def getMaxInstalls():

    uniqueratings = list(dict.fromkeys(installs))
    uniqueratings.sort()

    retval = uniqueratings[-1]

    return retval


#-----------------------------------------------------------------------------
#   
#   Function 
#
#-----------------------------------------------------------------------------
def setInstalls():
    invalidRating = True
    MaxNumInstalls = 0
    global InstSet
    while(invalidRating):
        screen_clear()
        MaxNumInstalls = getMaxInstalls()
        lowInstalls = setLowInstalls(MaxNumInstalls)
        highInstalls = setHighInstalls(MaxNumInstalls)

        if highInstalls < lowInstalls:
            print('Please ensure Maximum install number is above or equal to lowest')
        else:
            invalidRating = False
            InstSet = True


#-----------------------------------------------------------------------------
#   
#   Function 
#
#-----------------------------------------------------------------------------

    
    

def setFilters():
    settingFilers = True
    while(settingFilers):
        print_filter_menu()
        option = ''
        try:
            option = int(input('please select a filter: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
            process_cat_filter()
        elif option == 2:
            setRating()
        elif option == 3:
            setReviews()
        elif option == 4:
            setInstalls()
        elif option == 5:
            print('The program will now exit')
            settingFilers = False
        else:
            print('Invalid option. Please enter a number between 1 and 5.')

#-----------------------------------------------------------------------------
#   
#   Function 
#
#-----------------------------------------------------------------------------

def filterCatData(filterData):
    tempData = []
    for line in filterData:
        splitline = line.strip().split(',')
        if len(splitline) >= 1:
            #true if it has been set
            if splitline[1] == catFilter:
                tempData.append(line)
    return tempData
#-----------------------------------------------------------------------------
#   
#   Function 
#
#-----------------------------------------------------------------------------

def filterRatingsData(filterData):
    tempData = []
    for line in filterData:
        splitline = line.strip().split(',')
        if len(splitline) >= 1:
            #true if it has been set
            try:
                if float(splitline[2]) >= lowRating and float(splitline[2]) <= highRating:
                    tempData.append(line)
            except:
                tempData.append(line)
    return tempData

#-----------------------------------------------------------------------------

def filterRevData(filterData):
    tempData = []
    for line in filterData:
        splitline = line.strip().split(',')
        if len(splitline) >= 1:
            continue
            #true if it has been set
            if float(splitline[3]) >= lowReviews and float(splitline[3]) <= highReviews:
                tempData.append(line)
    return tempData

#-----------------------------------------------------------------------------
#   
#   Function 
#
#-----------------------------------------------------------------------------

def filterDataSet():
    #-- Take a copy of the data read from the file
    filterData = appData.copy()
    tempData = []
    if catSet:
        # filter Category Data
        tempData = filterCatData(filterData)
        filterData.clear()
        filterData = tempData
    if RatingSet:
        #filter Ratings Data
        tempData = filterRatingsData(filterData)
        filterData.clear()
        filterData = tempData
    if RevSet:
        # filter review data
        tempData = filterRevData(filterData)
        filterData.clear()
        filterData = tempData
    if InstSet:
        # filter install data
        tempData = filterRevData(filterData)
        filterData.clear()
        filterData = tempData

    return filterData


#-----------------------------------------------------------------------------
#   
#   Function 
#
#-----------------------------------------------------------------------------
def printAppNames():
    screen_clear()
    recCounts = 0
    filteredData = filterDataSet()
    for line in filteredData:
        splitline = line.strip().split(',')
        recCounts = recCounts+1
        if (recCounts >= 1):
            print(splitline[0])
        
    print(recCounts,'Records Found')

  #  for i in range(len(app)):
  #      print(app[i])

    input("Press Enter to return to main menu...")
#-----------------------------------------------------------------------------
#   
#   Function 
#
#-----------------------------------------------------------------------------


def filemenu():
    ans = True
    global fileName
    global appData
    while(ans):
        screen_clear()
        print_file_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
            fileName = input('Enter a file name: ')
            if checkFileExists(fileName):
                appData = loadFile(fileName)
                processFileDataForFilters(appData)
                ans = False
            else:
                print('File:',fileName,'does not exist')
                input("Press Enter to return to try again...")
        elif option == 2:
            print('The program will now exit')
            ans = False
            os._exit(0)
        else:
            print('Invalid option. Please enter a number between 1 and 2.')
#-----------------------------------------------------------------------------
#   
#   Function 
#
#-----------------------------------------------------------------------------            
def graphCategories():
    print('stub Graph Cat')
    sleep(3)
    time = [0, 1, 2, 3]
    position = [0, 100, 200, 300]

    plt.plot(time, position)
    plt.xlabel('Time (hr)')
    plt.ylabel('Position (km)')
    
    input("Press Enter to return to main menu...")
    
#-----------------------------------------------------------------------------
#   
#   Function 
#
#-----------------------------------------------------------------------------    
def graphRatings():
    print('stub Graph Rating')
    sleep(3)
#-----------------------------------------------------------------------------
#   
#   Function 
#
#-----------------------------------------------------------------------------
def graphReviews():
    print('stub Graph Reviews')
    sleep(3)
#-----------------------------------------------------------------------------
#   
#   Function 
#
#-----------------------------------------------------------------------------
def graphInstalls():
    print('stub Graph Installs')
    sleep(3)
#-----------------------------------------------------------------------------
#   
#   Function 
#
#-----------------------------------------------------------------------------
def graphPrices():
    print('Stub Graph Prices')
sleep(3)     
            
#-----------------------------------------------------------------------------
#   
#   Function 
#
#-----------------------------------------------------------------------------
def graphMenu():
    graphLoop = True
    while(graphLoop):
        screen_clear()
        print('Please select the x-axis for the graph\n')
        print_graphing_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
            graphCategories()
        elif option == 2:
            graphRatings()
        elif option == 3:
            graphReviews()
        elif option == 4:
            graphInstalls()
        elif option ==5:
            graphPrices()
        elif option ==6:
            # exit the Menu
            graphLoop = False
        else:
            print('Invalid option. Please enter a number between 1 and 6.')
                
            
    

#-----------------------------------------------------------------------------
#   
#   Function 
#
#-----------------------------------------------------------------------------

def appmenu():
    menuLoop = True
    while(menuLoop):
        screen_clear()
        print_app_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
            # set Filters for listing
            setFilters()
        elif option == 2:
            print('Print a list of apps names')
            printAppNames()
        elif option == 3:
            graphMenu()
        elif option == 4:
            resetFilters()
        elif option == 5:
            menuLoop = False
            os._exit(0)
            print('exit')
        else:
            print('Invalid option. Please enter a number between 1 and 5.')
#-----------------------------------------------------------------------------
#
# Main
#
#-------------------------------------------------------


def Main():
    #--- filter params
    resetFilters()
    screen_clear()
    filemenu()
    appmenu()
    sys.exit


Main()


#-----------------------------------------------------------------------------
