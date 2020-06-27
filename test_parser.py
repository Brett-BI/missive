import pytest

from app.util.Parser import Parser

''' parseTimes '''
def test_Parser_getTimes_single():
    assert Parser.getTimes('+ @12:00 "Get coffee" #1234567899') == ['12:00']

def test_Parser_getTimes_singleWSemicolon():
    assert Parser.getTimes('+ @12:00; "Get coffee" #1234567899') == ['12:00']

def test_Parser_getTimes_singleExtraAt():
    assert Parser.getTimes('+ @12:00@ "Get coffee" #1234567899') == ['12:00']

def test_Parser_getTimes_single_noAt():
    assert Parser.getTimes('+ 12:00 "Get coffee" #1234567899') == []

def test_Parser_getTimes_double_noAt():
    assert Parser.getTimes('+ 12:0013:00 "Get coffee" #1234567899') == []

def test_Parser_getTimes_space():
    assert Parser.getTimes('+ @12:00 @13:00 "Get coffee" #1234567899') == ['12:00', '13:00']

def test_Parser_getTimes_noChar():
    assert Parser.getTimes('+ @12:00@13:00 "Get coffee" #1234567899') == ['12:00', '13:00']

def test_Parser_getTimes_semicolon():
    assert Parser.getTimes('+ @12:00;@13:00 "Get coffee" #1234567899') == ['12:00', '13:00']

def test_Parser_getTimes_diffOrder():
    assert Parser.getTimes('+ "Get Coffee and Tea" #1231231234 @12:00') == ['12:00']


''' parseRecipients '''
def test_Parser_getRecipients_single():
    assert Parser.getRecipients('+ @12:00 "Get coffee" #1234567899') == ['1234567899']

def test_Parser_getRecipients_single_extraPound():
    assert Parser.getRecipients('+ @12:00 "Get coffee" #1234567899#') == ['1234567899']

def test_Parser_getRecipients_double():
    assert Parser.getRecipients('+ @12:00 "Get coffee" #1234567899#2342342345') == ['1234567899', '2342342345']

def test_Parser_getRecipients_double_space():
    assert Parser.getRecipients('+ @12:00 "Get coffee" #1234567899 #2342342345') == ['1234567899', '2342342345']

def test_Parser_getRecipients_double_semicolon():
    assert Parser.getRecipients('+ @12:00 "Get coffee" #1234567899;#2342342345') == ['1234567899', '2342342345']

def test_Parser_getRecipients_double_noPound():
    assert Parser.getRecipients('+ @12:00 "Get coffee" 12345678993216549875') == []

def test_Parser_getRecipients_diffOrder():
    assert Parser.getRecipients('+ @12:00 #1234567899 "Get coffee"') == ['1234567899']

''' parseMessage '''
def test_Parser_parseMessage():
    Parser.getMessage('+ @14:00@12:00@9:00 "Pick up cake and cheese" #2342342344#8578478574') == ['"Pick up cake and cheese"']

def test_Parser_parseMessage_quotes():
    Parser.getMessage('+ @14:00@12:00@9:00 "Pick up cake and \'cheese\'" #2342342344#8578478574') == ['"Pick up cake and \'cheese\'"']

def test_Parser_parseMessage_multiple():
    Parser.getMessage('+ @14:00@12:00@9:00 "Pick up cake and cheese" "Grab coffee for road" #2342342344#8578478574') == ['"Pick up cake and cheese"', '"Grab coffee for road"']

def test_Parser_parseMessage_quotes_multiple():
    Parser.getMessage('+ @14:00@12:00@9:00 "Pick up cake and \'cheese\'" "Get \'chicken\'" #2342342344#8578478574') == ['"Pick up cake and \'cheese\'"', '"Get \'chicken\'"']


''' parseMissiveID '''


''' requestIsValid '''
def test_Parser_requestIsValid_noTime():
    assert Parser.requestIsValid('+ "Get coffee" #1234567899') == False

def test_Parser_requestIsValid_noMessage():
    assert Parser.requestIsValid('+ @12:00 #1234567899') == False

def test_Parser_requestIsValid_noRecipient():
    assert Parser.requestIsValid('+ @12:00 "Get coffee"') == False

def test_Parser_requestIsValid_true():
    assert Parser.requestIsValid('+ @12:00 "Get coffee" #1234567899') == True