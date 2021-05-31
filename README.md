# Cowin Vaccine Tracker


Python API wrapper for CoWin, for the vaccination drive by booking an appointment at the nearby vaccination centres

This wrapper supports Find vaccine availability by Pincode, District and booking of apointments is on the way.

[Vacine Notifier](http://t.me/VacineFinderBot "Named link title") a Telegram Bot which can be used to check vaccine availability status and recieve notification when registered for vaccine availability. 


## Installation
```pip install cowin-vaccine-api```

## Usage

### Get States
``` 
from cowin import CoWinAPI

cowin = CoWinAPI()

states = cowin.get_states()
print(states)
```

### Get Districts
``` 
from cowin import CoWinAPI
state_id=31
cowin = CoWinAPI()

districts = cowin.get_districts(state_id)
print(districts)
```

### Availability By Pin for a day
``` 
from cowin import CoWinAPI
pin_code = "642122"

cowin = CoWinAPI()
#pass date in method to get specific date or today's date is taken
available_centers = cowin.get_availability_by_pincode(pin_code)
print(available_centers)
```

### Availability By DistrictID for a day
``` 
from cowin import CoWinAPI
pin_code = "642122"

cowin = CoWinAPI()
#pass date in method to get specific date or today's date is taken
available_centers = cowin.get_availability_by_district(pin_code)
print(available_centers)
```

### Availability By Pincode for a week
``` 
from cowin import CoWinAPI
pin_code = "642122"

cowin = CoWinAPI()
#pass date in method to get specific date or today's date is taken
available_centers = cowin.get_availability_by_pincode_week(pin_code)
print(available_centers)
```

### Availability By DistrictID for a week
``` 
from cowin import CoWinAPI
pin_code = "642122"

cowin = CoWinAPI()
#pass date in method to get specific date or today's date is taken
available_centers = cowin.get_availability_by_pincode_week(pin_code)
print(available_centers)
```

## License

© 2021 Kishore

This repository is licensed under the MIT license. See LICENSE for details.
