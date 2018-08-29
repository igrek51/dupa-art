#!/usr/bin/env python
# -*- coding: utf-8 -*-
from glue import *
import random
import time
import string
import datetime

'''
Sun 
Mon DD  U U PP   A 
Tue D D U U P P A A
Wed D D U U PP  AAA
Thu D D U U P   A A
Fri DD  UUU P   A A
Sat
Week123456789012345 - 15 weeks = 105 days < 4 months
'''
secretArt = [
	'               ',
	'DD  U U PP   A ',
	'D D U U P P A A',
	'D D U U PP  AAA',
	'D D U U P   A A',
	'DD  UUU P   A A',
	'               '
]
firstDay = '2015-01-04'

def generateCommitDays():
	firstDatetime = str2time(firstDay, '%Y-%m-%d')
	commitDays = []
	# map commits schedule
	for w in range(len(secretArt[0])): # for each week
		for d in range(7): # for each day: 0 - 6
			if secretArt[d][w] is not ' ': # if it's occupied
				daysCount = w * 7 + d
				date = firstDatetime + datetime.timedelta(days=daysCount)
				commitDays.append(date)
	debug('commitDays: %s' % map(lambda d: time2str(d, '%Y-%m-%d'), commitDays))
	return commitDays

def makeCommit(commitDate):
	featureName = generateFeatureName()
	commitMessage = 'Add %s feature' % featureName
	# make a change
	shellExec('echo "%s" >> dupa/art.py' % generateCodeLine(featureName))
	# set random time
	datetime = setRandomTime(commitDate)
	commitWithFakeDate(datetime, commitMessage)

def generateCodeLine(featureName):
	return "\tprint('%s')" % featureName

def generateFeatureName():
	words = splitLines(readFile('dupa/words.txt'))
	message = ''
	for i in range(random.randint(2, 5)):
		message += random.choice(words) + ' '
	return message[:-1]

def commitWithFakeDate(datetime, commitMessage):
	# date format: Tue Aug 28 12:07:00 2018 +0200
	datetimeString = time2str(datetime, "%a %b %d %H:%M:%S %Y +0200")
	shellExec('git commit --date "%s" -am "%s"' % (datetimeString, commitMessage))
	info('commit has been made: %s - %s' % (datetimeString, commitMessage))

def setRandomTime(date):
	hour = random.randint(8, 21)
	minute = random.randint(0, 59)
	second = random.randint(0, 59)
	return date.replace(hour=hour, minute=minute, second=second)

# ----- Main
def main():
	setWorkdir(getScriptRealDir())
	# make commits
	for commitDay in generateCommitDays():
		makeCommit(commitDay)
	# push commits
	shellExec('git push origin master')

if __name__ == '__main__': # testing purposes
	main()
