#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glue
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
firstDay = '2018-08-26'

datePattern = '%Y-%m-%d'

def calculateCommitDays():
	firstDatetime = str2datetime(firstDay)
	commitDays = []
	# map commits schedule
	for w in range(len(secretArt[0])): # for each week
		for d in range(7): # for each day: 0 - 6
			if secretArt[d][w] is not ' ': # if it's occupied
				daysCount = w * 7 + d
				date = firstDatetime + datetime.timedelta(days=daysCount)
				commitDays.append(glue.time2str(date.timetuple(), datePattern))
	glue.debug('commitDays: ' + str(commitDays))
	return commitDays

def str2datetime(strDate):
	return datetime.datetime.fromtimestamp(time.mktime(glue.str2time(strDate, datePattern)))

def isCommitDay():
	now = time.localtime()
	today = glue.time2str(now, datePattern)
	commitDays = calculateCommitDays()
	return today in commitDays

def commit():
	glue.info("it's commit day!")
	glue.setWorkdir(glue.getScriptRealDir())

	feature = generateFeature()
	line = generateCodeLine(feature)
	commitMessage = 'Add %s feature' % feature
	glue.info('random code line: %s' % line)
	glue.info('commit message: %s' % commitMessage)
	# make a change
	glue.shellExec('echo "%s" >> dupa/art.py' % line)
	# commit & push
	glue.shellExec('git commit -am "%s"' % commitMessage)
	glue.shellExec('git push origin master')
	glue.info('commit has been pushed')

def generateCodeLine(feature):
	length = random.randint(1, 32)
	code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
	return "\tprint('%s %s')" % (feature, code)

def generateFeature():
	words = glue.splitLines(glue.readFile('dupa/words.txt'))
	message = ''
	for i in range(random.randint(2, 5)):
		message += random.choice(words) + ' '
	return message[:-1]

# ----- Main
def main():
	if isCommitDay() or True:
		commit()
	else:
		glue.info('not today (%s)...' % glue.time2str(time.localtime(), datePattern))

if __name__ == '__main__': # testing purposes
	main()
