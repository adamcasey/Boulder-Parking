import csv

'''
Crime File : INCIDENT_ID	OFFENSE_ID(1)	OFFENSE_CODE(2)	OFFENSE_CODE_EXTENSION(3)	OFFENSE_TYPE_ID(4)	OFFENSE_CATEGORY_ID(5)	FIRST_OCCURRENCE_DATE(6)
LAST_OCCURRENCE_DATE(7)	REPORTED_DATE(8)	INCIDENT_ADDRESS(9)	GEO_X(10)	GEO_Y	(11)
GEO_LON(12)	GEO_LAT(13)	DISTRICT_ID	PRECINCT_ID(14)	NEIGHBORHOOD_ID(15)	IS_CRIME(16)	IS_TRAFFIC(17)

offense_codes.csv: OFFENSE_CODE(1)	OFFENSE_CODE_EXTENSION(2)	OFFENSE_TYPE_ID(3)	OFFENSE_TYPE_NAME(4)	OFFENSE_CATEGORY_ID(5)
	OFFENSE_CATEGORY_NAME(6)	IS_CRIME(7)	IS_TRAFFIC(8)

'''
#print ("check solution")

def readCrimeFile(filename):
    crimeFile = open(filename,'r')
    for line in crimeFile:
        crimeList.append(line) #adds line to list as a string

def sortCrimeFile():
    tempCrimeList = [] #holder for comma sep. values of orignial list
    for line in crimeList:
        line = line.strip()
        tempCrimeList = line.split(',') #each value seperated by a comma is put into a list
        try: #first line of the file is a string = 'IS TRAFFIC'
            isTraffic = int(tempCrimeList[-1])
            if (isTraffic == 0): #checks to see if offense was a traffic or criminal crime, 0 means 'no', if 'IS TRAFFIC = 0' then it is a real crime
                hoodList.append(tempCrimeList[-3].strip()) #tempCrimeList holds all the comma seperated values
                offenseList.append(tempCrimeList[4].strip())
				offenseCodeOne.append(int(tempCrimelist[2].strip()))
        except: #do nothing
            pass

    #print(len(crimeList)) #395,978
    #print(len(hoodList))    #287,339
    #print(len(offenseList)) #287,339

#count the number of crimes in a neighborhood --> you need to have a smaller list that contains only one instance of each neighborhood
def hoodCount():
	totalHoodList = set(hoodList) #this should create a new list that contains each neighborhood only once --> much smaller list

#open second .csv file to read in offense codes that further clarify crimes
def readOffenseCodes(filename):
	tempList = []
	for line in filename:
		line = line.strip()
		tempList = line.split(',')
		offenseCodeTwo.append(int(tempList[0].strip()))

		

#Global variables/lists/whatever
crimeFile = "crime.csv"
codeFile = "offense_codes.csv"

crimeList = [] #original list of crimes that aren't parsed
offenseCodeOne = [] #list to hold offense code reference for crime.csv file
offenseCodeTwo = [] #list to hold offense code reference for offense_codes.csv file
hoodList = [] #neighborhood of each cirme committted, listed multiple times
offenseList = [] #name of each crime
totalHoodList = [] #list to hold single neighborhood names
codeList = [] #list to hold offense codes 

#Call the functions
readCrimeFile(crimeFile)
sortCrimeFile()
hoodCount()
readOffenseCodes(codeFile)

#print (hoodList)
#print (offenseList)
