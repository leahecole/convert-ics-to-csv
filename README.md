# convert-ics-to-csv

Source Data in [`holidays.ics`](./holidays.csv) is from the [US Open Government Federal Holiday Webpage](https://www.opm.gov/about-us/open-government/Data/Apps/Holidays/Index.aspx)

## Testing

There are a few tests that act as a confidence check and to ensure that my code will remain not-stale for as long as possible. To execute them, first install the dependencies and test dependencies, then run pytest.

```bash
  pip install -r requirements.txt 
  pip install -r requirements-test.txt
  python -m pytest ics_to_csv_test.py
```
  
