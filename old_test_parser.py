import pytest

from app.sms.functions.Parser import AddParser, RemoveParser, InfoParser

def test_AddParser_getElements():
    ap = AddParser('+ @12:00;@13:00 "Get coffee" #1234567899')
    assert ap.getElements() == ['@12:00', '@13:00', '"Get coffee"', '#1234567899']

def test_AddParser_parseReminder():
    ap = AddParser('+ @14:00@12:00@9:00 "Pick up cake and cheese" #2342342344#8578478574')
    assert ap.parseReminder() == ['"Pick up cake and cheese"']

def test_AddParser_parseReminder_quotes():
    ap = AddParser('+ @14:00@12:00@9:00 "Pick up cake and \'cheese\'" #2342342344#8578478574')
    print(ap.msg_body)
    assert ap.parseReminder() == ['"Pick up cake and \'cheese\'"']

def test_AddParser_parseReminder_multiple():
    ap = AddParser('+ @14:00@12:00@9:00 "Pick up cake and cheese" "Grab coffee for road" #2342342344#8578478574')
    assert ap.parseReminder() == ['"Pick up cake and cheese"', '"Grab coffee for road"']

def test_AddParser_parseReminder_quotes_multiple():
    ap = AddParser('+ @14:00@12:00@9:00 "Pick up cake and \'cheese\'" "Get \'chicken\'" #2342342344#8578478574')
    assert ap.parseReminder() == ['"Pick up cake and \'cheese\'"', '"Get \'chicken\'"']

def test_AddParser_parseReceivers_nospace():
    ap = AddParser('+ @14:00@12:00@9:00 "Pick up cake and \'cheese\'" #2342342344#8578478574')
    assert ap.parseReceivers() == ['#2342342344', '#8578478574']

def test_AddParser_parseReceivers_semicolon():
    ap = AddParser('+ @14:00@12:00@9:00 "Pick up cake and \'cheese\'" #2342342344;#8578478574')
    assert ap.parseReceivers() == ['#2342342344', '#8578478574']

def test_AddParser_parseReceivers_space():
    ap = AddParser('+ @14:00@12:00@9:00 "Pick up cake and \'cheese\'" #2342342344 #8578478574')
    assert ap.parseReceivers() == ['#2342342344', '#8578478574']

def test_AddParser_parseTimes_nospace():
    ap = AddParser('+ @14:00@12:00@9:00 "Pick up cake and \'cheese\'" #2342342344#8578478574')
    assert ap.parseTimes() == ['@14:00', '@12:00', '@9:00']

def test_AddParser_parseTimes_space():
    ap = AddParser('+ @14:00 @12:00 @9:00 "Pick up cake and \'cheese\'" #2342342344#8578478574')
    assert ap.parseTimes() == ['@14:00', '@12:00', '@9:00']

def test_AddParser_parseTimes_semicolon():
    ap = AddParser('+ @14:00;@12:00;@9:00 "Pick up cake and \'cheese\'" #2342342344#8578478574')
    assert ap.parseTimes() == ['@14:00', '@12:00', '@9:00']

def test_AddParser_repr():
    ap = AddParser('+ @12:00;@13:00 "Get coffee" #1234567899')
    assert ap.__repr__() == '+ @12:00;@13:00 "Get coffee" #1234567899'


""" RemoveParser """
def test_RemoveParser_getElements():
    rp = RemoveParser('- 123456')
    assert rp.getElements() == ['123456']

def test_RemoveParser_getMissiveID():
    rp = RemoveParser('- 123456')
    assert rp.parseMissiveID() == ['123456']

def test_RemoveParser_getMissiveID_space():
    rp = RemoveParser('- 123456 098765')
    assert rp.parseMissiveID() == ['123456', '098765']

def test_RemoveParser_getMissiveID_semicolon():
    rp = RemoveParser('- 123456;098765')
    assert rp.parseMissiveID() == ['123456', '098765']

def test_RemoveParser_repr():
    rp = RemoveParser('- 123456')
    assert rp.__repr__() == '- 123456'


""" Info Parser """
def test_InfoParser_getElements():
    ip = InfoParser('! @12:30@14:00')
    assert ip.getElements() == ['@12:30', '@14:00']

def test_InfoParser_getElements_noTime():
    ip = InfoParser('!')
    assert ip.getElements() == []

def test_InfoParser_parseTimes():
    ip = InfoParser('! @12:30')
    assert ip.parseTimes() == ['@12:30']

def test_InfoParser_parseTimes_noTimes():
    ip = InfoParser('!')
    assert ip.parseTimes() == []

def test_InfoParser_parseTimes_space():
    ip = InfoParser('! @12:30 @14:00')
    assert ip.parseTimes() == ['@12:30', '@14:00']

def test_InfoParser_parseTimes_semicolon():
    ip = InfoParser('! @12:30;@14:00')
    assert ip.parseTimes() == ['@12:30', '@14:00']

def test_InfoParser_parseTimes_nospace():
    ip = InfoParser('! @12:30@14:00')
    assert ip.parseTimes() == ['@12:30', '@14:00']

def test_InfoParser_repr():
    ip = InfoParser('! @12:30@14:00')
    assert ip.__repr__() == '! @12:30@14:00'