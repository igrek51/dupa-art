# -*- coding: utf-8 -*-
from dupaart import *

def test_calculateCommitDays():
    commitDays = calculateCommitDays()
    assert commitDays == ['2018-08-27', '2018-08-28', '2018-08-29', '2018-08-30', '2018-08-31', '2018-09-03', '2018-09-07', '2018-09-11', '2018-09-12', '2018-09-13', '2018-09-24', '2018-09-25', '2018-09-26', '2018-09-27', '2018-09-28', '2018-10-05', '2018-10-08', '2018-10-09', '2018-10-10', '2018-10-11', '2018-10-12', '2018-10-22', '2018-10-23', '2018-10-24', '2018-10-25', '2018-10-26', '2018-10-29', '2018-10-31', '2018-11-06', '2018-11-20', '2018-11-21', '2018-11-22', '2018-11-23', '2018-11-26', '2018-11-28', '2018-12-04', '2018-12-05', '2018-12-06', '2018-12-07']

def test_generateCodeLine():
    line = generateCodeLine('jasna dupa')
    assert 'jasna dupa' in line
    assert len(line) > len('jasna dupa')

def test_generateFeature():
    feature = generateFeature()
    assert len(feature) >= 3
