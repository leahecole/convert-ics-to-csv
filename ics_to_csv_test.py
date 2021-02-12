import ics_to_csv
import pytest
import ics
import subprocess
import os
import uuid

# Bare minimum tests to make sure my sample doesn't break as time goes on
UUID = uuid.uuid4().hex[:10]
OUTPUT_FILE = f"holidays-test-{UUID}.csv"
TEST_CALENDAR_STRING=(
    "BEGIN:VCALENDAR\n"
    "VERSION:2.0\n"
    "PRODID:-//Telerik Inc.//NONSGML RadScheduler//EN\n"
    "METHOD:PUBLISH\n"
    "BEGIN:VEVENT\n"
    "DTSTART:19970101\n"
    "DTEND:19970102\n"
    "UID:20210211T185111Z-05fe6751-ec1d-4532-b3a8-60e48e0eb064\n"
    "DTSTAMP:20210211T185111Z\n"
    "SUMMARY:New Year’s Day\n"
    "DESCRIPTION:\n"
    "END:VEVENT\n"
    "END:VCALENDAR\n"
)
# Test string is missing END:VCALENDAR and BEGIN: VEVENT lines
TEST_BAD_CALENDAR_STRING=(
    "BEGIN:VCALENDAR\n"
    "VERSION:2.0\n"
    "PRODID:-//Telerik Inc.//NONSGML RadScheduler//EN\n"
    "METHOD:PUBLISH\n"
    "DTSTART:19970101\n"
    "DTEND:19970102\n"
    "UID:20210211T185111Z-05fe6751-ec1d-4532-b3a8-60e48e0eb064\n"
    "DTSTAMP:20210211T185111Z\n"
    "SUMMARY:New Year’s Day\n"
    "DESCRIPTION:\n"
    "END:VEVENT\n"
)

TEST_EVENT_LIST = [['Date', 'Holiday'], ['1997-1-1', 'New Year’s Day']]


@pytest.fixture
def cleanup_csv_test():
    yield
    subprocess.run(["rm", OUTPUT_FILE])


def test_convert_ics_to_string_fails_bad_ics():
    with pytest.raises(Exception):
        assert(ics_to_csv.convert_ics_to_string("holidays-test-bad.ics"))
    with pytest.raises(Exception):
        assert(ics_to_csv.convert_ics_to_string("test.txt"))

def test_convert_ics_to_string():
    output = ics_to_csv.convert_ics_to_string("holidays-test.ics")
    assert "BEGIN:VCALENDAR" in output

def test_make_event_list():
   
    output = ics_to_csv.make_event_list(TEST_CALENDAR_STRING)
    assert "New Year’s Day" in output[1]
    assert len(output)==2

def test_make_event_list_fails():
    with pytest.raises(ics.grammar.parse.ParseError):
        
        ics_to_csv.make_event_list(TEST_BAD_CALENDAR_STRING)

def test_convert_list_to_csv(cleanup_csv_test):
    ics_to_csv.convert_list_to_csv(TEST_EVENT_LIST, OUTPUT_FILE)
    assert os.path.exists(OUTPUT_FILE)
