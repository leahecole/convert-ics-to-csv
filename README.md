# convert-ics-to-csv

This script takes an [iCalendar file](https://icalendar.org/) as input and outputs a CSV with two columns: **Date** and **Holiday**. **Date** is the date of the holiday in "YEAR-MONTH-DAY" format, and **Holiday** is the name of the holiday, found in the `SUMMARY` field of the original file.

## Running the code
To execute the script on a calendar file with United States Federal Holidays from 1997-2021, run the following commands:

Install dependencies:
`pip install -r requirements.txt`

Run the script
`python ics_to_csv.py`

If the script executes successfully, a CSV file, `holidays.csv`, will be created.

## Data Source
Source Data in [`holidays.ics`](./holidays.csv) is from the [US Open Government Federal Holiday Webpage](https://www.opm.gov/about-us/open-government/Data/Apps/Holidays/Index.aspx)

## Testing

There are a few tests that act as a confidence check and to ensure that my code will remain not-stale for as long as possible. To execute them, first install the dependencies and test dependencies, then run pytest.

```bash
  pip install -r requirements.txt 
  pip install -r requirements-test.txt
  python -m pytest ics_to_csv_test.py
```

## Caveats

In case you choose to adapt this script for your own purposes, I wanted to include a few caveats:

* I wrote this script specifically based on the included [`holidays.ics` file](holidays.ics). It has not yet been tested against other iCalendar files
* As of February 2021, no United States Federal Holidays last longer than one day. As a result, I only look at the start date in the script, not the end date. For events lasting longer than one day, this would need to be adapted. 

## Contributions

I welcome any additional contributions but request that if you add additional functionality, you add accompanying tests. 
  
