# PHONE FORMAT CLASS
Phone number formatting class

Will format phone number with selected country code, based on list of country codes provided

## Ussage

### Fromat phone number
```python
#!python
from bphoneformat import bPhoneFormat

pf = bPhoneFormat()
print(pf.format_phone('Venezuela', '055899889'))
```

### Get country keys used in **format_phone** function
```python
#!python
from bphoneformat import bPhoneFormat

pf = bPhoneFormat()
print(pf.get_country_keys())
```

### Get country names
```python
#!python
from bphoneformat import bPhoneFormat

pf = bPhoneFormat()
print(pf.get_country_names())
```
