#!/usr/bin/env python3
import random
import datetime

from cliglue.utils.output import info, debug
from cliglue.utils.time import str2time, time2str
from cliglue.utils.shell import shell
from cliglue.utils.files import read_file, set_workdir, script_real_dir

"""
Tiles pattern made out of single days:
Sun 
Mon DD  U U PP   A 
Tue D D U U P P A A
Wed D D U U PP  AAA
Thu D D U U P   A A
Fri DD  UUU P   A A
Sat
Week123456789012345 - 15 weeks = 105 days < 4 months
"""
secret_art = [
    '               ',
    'DD  U U PP   A ',
    'D D U U P P A A',
    'D D U U PP  AAA',
    'D D U U P   A A',
    'DD  UUU P   A A',
    '               '
]
first_day = '2015-01-04'


def generate_commit_days():
    first_datetime = str2time(first_day, '%Y-%m-%d')
    commit_days = []
    # map commits schedule
    for w in range(len(secret_art[0])):  # for each week
        for d in range(7):  # for each day: 0 - 6
            if secret_art[d][w] is not ' ':  # if it's occupied
                days_count = w * 7 + d
                date = first_datetime + datetime.timedelta(days=days_count)
                commit_days.append(date)
    debug(f'commit days: {map(lambda c: time2str(c, "%Y-%m-%d"), commit_days)}')
    return commit_days


def make_commit(commit_date):
    feature_name = generate_feature_name()
    commit_message = 'Add %s feature' % feature_name
    # make a change
    shell('echo "%s" >> dupa/art.py' % generate_code_line(feature_name))
    # set random time
    r_datetime = set_random_time(commit_date)
    commit_with_fake_date(r_datetime, commit_message)


def generate_code_line(feature_name):
    return "\tprint('%s')" % feature_name


def generate_feature_name():
    words = read_file('dupa/words.txt').splitlines()
    message = ''
    for i in range(random.randint(2, 5)):
        message += random.choice(words) + ' '
    return message[:-1]


def commit_with_fake_date(fake_datetime, commit_message):
    # date format: Tue Aug 28 12:07:00 2018 +0200
    datetime_string = time2str(fake_datetime, "%a %b %d %H:%M:%S %Y +0200")
    shell('git commit --date "%s" -am "%s"' % (datetime_string, commit_message))
    info('commit has been made: %s - %s' % (datetime_string, commit_message))


def set_random_time(date):
    hour = random.randint(8, 21)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return date.replace(hour=hour, minute=minute, second=second)


def main():
    set_workdir(script_real_dir())
    # make commits
    for commitDay in generate_commit_days():
        make_commit(commitDay)
    # push commits
    shell('git push origin master')


if __name__ == '__main__':
    main()
