import pytest
from datetime import datetime, timedelta
from freezegun import freeze_time

from app.util.Parser import Parser

''' parseTimes '''
@freeze_time('2020-06-30 19:20:00')
def test_Parser_getTimes_single():
    times = Parser('+ @12:00 "Get coffee" #1234567899').getTimes()
    assert times == [datetime(2020, 7, 1, 12, 0, 0)]

@freeze_time('2020-04-20 07:07:07')
def test_Parser_getTimes_singleWSemicolon():
    times = Parser('+ @12:00; "Get coffee" #1234567899').getTimes()
    assert times == [datetime(2020, 4, 20, 12, 0, 0)]

@freeze_time('2020-02-14 13:03:00')
def test_Parser_getTimes_singleExtraAt():
    times = Parser('+ @12:00@ "Get coffee" #1234567899').getTimes()
    assert times == [datetime(2020, 2, 15, 12, 0, 0)]

@freeze_time('2020-11-22 11:12:00')
def test_Parser_getTimes_single_noAt():
    times = Parser('+ 12:00 "Get coffee" #1234567899').getTimes()
    assert times == []

@freeze_time('1993-09-28 21:45:00')
def test_Parser_getTimes_double_noAt():
    times = Parser('+ 12:0013:00 "Get coffee" #1234567899').getTimes()
    assert times == []

@freeze_time('1999-08-12 23:23:00')
def test_Parser_getTimes_space():
    times = Parser('+ @12:00 @13:00 "Get coffee" #1234567899').getTimes()
    assert times == [datetime(1999, 8, 13, 12, 0, 0), datetime(1999, 8, 13, 13, 0, 0)]

@freeze_time('2009-05-08 10:00:00')
def test_Parser_getTimes_noChar():
    times = Parser('+ @12:00@13:00 "Get coffee" #1234567899').getTimes()
    assert times == [datetime(2009, 5, 8, 12, 0, 0), datetime(2009, 5, 8, 13, 0, 0)]

@freeze_time('2020-12-29 12:30:00')
def test_Parser_getTimes_semicolon():
    times = Parser('+ @12:00;@13:00 "Get coffee" #1234567899').getTimes()
    assert times == [datetime(2020, 12, 30, 12, 0, 0), datetime(2020, 12, 29, 13, 0, 0)]

@freeze_time('2019-12-31 20:08:00')
def test_Parser_getTimes_diffOrder():
    times = Parser('+ "Get Coffee and Tea" #1231231234 @12:00').getTimes()
    assert times == [datetime(2020, 1, 1, 12, 0, 0)]

@freeze_time('2020-06-30 19:40:00')
def test_Parser_getTimes_diffOrderMultiple():
    times = Parser('+ #1231231234 "Get coffee and a tea." @1:00@19:50').getTimes()
    assert times == [datetime(2020, 7, 1, 1, 0, 0), datetime(2020, 6, 30, 19, 50, 0)]


''' parseRecipients '''
def test_Parser_getRecipients_single():
    assert Parser('+ @12:00 "Get coffee" #1234567899').getRecipients() == ['1234567899']

def test_Parser_getRecipients_single_extraPound():
    assert Parser('+ @12:00 "Get coffee" #1234567899#').getRecipients() == ['1234567899']

def test_Parser_getRecipients_double():
    assert Parser('+ @12:00 "Get coffee" #1234567899#2342342345').getRecipients() == ['1234567899', '2342342345']

def test_Parser_getRecipients_double_space():
    assert Parser('+ @12:00 "Get coffee" #1234567899 #2342342345').getRecipients() == ['1234567899', '2342342345']

def test_Parser_getRecipients_double_semicolon():
    assert Parser('+ @12:00 "Get coffee" #1234567899;#2342342345').getRecipients() == ['1234567899', '2342342345']

def test_Parser_getRecipients_double_noPound():
    assert Parser('+ @12:00 "Get coffee" 12345678993216549875').getRecipients() == []

def test_Parser_getRecipients_diffOrder():
    assert Parser('+ @12:00 #1234567899 "Get coffee"').getRecipients() == ['1234567899']

''' parseMessage '''
def test_Parser_parseMessage():
    Parser('+ @14:00@12:00@9:00 "Pick up cake and cheese" #2342342344#8578478574').getMessage() == ['"Pick up cake and cheese"']

def test_Parser_parseMessage_quotes():
    Parser('+ @14:00@12:00@9:00 "Pick up cake and \'cheese\'" #2342342344#8578478574').getMessage() == ['"Pick up cake and \'cheese\'"']

def test_Parser_parseMessage_multiple():
    Parser('+ @14:00@12:00@9:00 "Pick up cake and cheese" "Grab coffee for road" #2342342344#8578478574').getMessage() == ['"Pick up cake and cheese"', '"Grab coffee for road"']

def test_Parser_parseMessage_quotes_multiple():
    Parser('+ @14:00@12:00@9:00 "Pick up cake and \'cheese\'" "Get \'chicken\'" #2342342344#8578478574').getMessage() == ['"Pick up cake and \'cheese\'"', '"Get \'chicken\'"']


''' parseMissiveID '''


''' requestIsValid '''
def test_Parser_requestIsValid_noTime():
    assert Parser('+ "Get coffee" #1234567899').requestIsValid() == False

def test_Parser_requestIsValid_noMessage():
    assert Parser('+ @12:00 #1234567899').requestIsValid() == False

def test_Parser_requestIsValid_noRecipient():
    assert Parser('+ @12:00 "Get coffee"').requestIsValid() == False

def test_Parser_requestIsValid_true():
    assert Parser('+ @12:00 "Get coffee" #1234567899').requestIsValid() == True