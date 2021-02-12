import ics
import csv


def convert_ics_to_string(filename: str) -> str:
    # open the ICS file and write contents to string
    with open(filename, 'r') as calendar_file:
        lines = calendar_file.readlines()
        if lines[0] != "BEGIN:VCALENDAR\n" or lines[len(lines)-1]!="END:VCALENDAR\n":
            raise Exception("This isn't a valid ICS file")
        calendar_string = ''
        for line in lines:
            calendar_string += line
    return calendar_string

def make_event_list(calendar_string: str) -> list:
    #uses ics library to turn calendar string into object
    try:
        calendar = ics.Calendar.parse_multiple(calendar_string)
    except ics.grammar.parse.ParseError:
        raise

    # calling with [0] because calendar is a list with a single Calendar object
    events = calendar[0].events 

    # create list where each item will be a line in the csv output
    events_csv_list = [["Date", "Holiday"]] 

    # loop through event set
    # get date of holiday (in this case, holidays are all one day so the begin date is enough)
    # get the holiday name
    for event in events:
        start = event.begin
        date = f"{start.year}-{start.month}-{start.day}"
        name = event.name
        events_csv_list.append([date, name])
    return events_csv_list

def convert_list_to_csv(events_csv_list: list, output_name: str,) -> None:
    # write the list to csv output
    with open(output_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(events_csv_list)

if __name__ == "__main__":
    calendar_string = convert_ics_to_string('holidays.ics')
    event_list = make_event_list(calendar_string)
    convert_list_to_csv(event_list, "holidays.csv")




