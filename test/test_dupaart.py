from dupaart import *


def test_generate_commit_days():
    commit_days = list(map(lambda d: time2str(d, '%Y-%m-%d'), generate_commit_days()))
    assert commit_days == ['2015-01-05', '2015-01-06', '2015-01-07', '2015-01-08', '2015-01-09', '2015-01-12',
                           '2015-01-16', '2015-01-20', '2015-01-21', '2015-01-22', '2015-02-02', '2015-02-03',
                           '2015-02-04', '2015-02-05', '2015-02-06', '2015-02-13', '2015-02-16', '2015-02-17',
                           '2015-02-18', '2015-02-19', '2015-02-20', '2015-03-02', '2015-03-03', '2015-03-04',
                           '2015-03-05', '2015-03-06', '2015-03-09', '2015-03-11', '2015-03-17', '2015-03-31',
                           '2015-04-01', '2015-04-02', '2015-04-03', '2015-04-06', '2015-04-08', '2015-04-14',
                           '2015-04-15', '2015-04-16', '2015-04-17']


def test_generate_code_line():
    line = generate_code_line('jasna dupa')
    assert 'jasna dupa' in line
    assert len(line) > len('jasna dupa')


def test_generate_feature_name():
    feature = generate_feature_name()
    assert len(feature) >= 3


def test_set_random_time():
    date = str2time('2018-04-01', '%Y-%m-%d')
    assert time2str(date, '%H:%M:%S') == '00:00:00'
    random_date = set_random_time(date)
    assert time2str(random_date, '%H:%M:%S') != '00:00:00'
    assert time2str(random_date, '%Y-%m-%d') == '2018-04-01'
