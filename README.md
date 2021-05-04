# Cowin Vaccine Tracker


Python API wrapper for CoWin, for the vaccination drive by booking an appointment at the nearby vaccination centres

This wrapper supports Find vaccine availability by Pincode, District and booking of apointments is on the way.
This wrapper is meant to enable folks to build their own versions of a system to lookup for vaccine availablity either in a district or in a particular pin code.



## Installation
```pip install cowin-vaccine-api```

## Usage
``` from cowin_api import CoWinAPI
    pin_code = "400080"

    cowin = CoWinAPI()
    available_centers = cowin.get_availability_by_pincode(pin_code)
    print(available_centers)```

## License

© 2021 Kishore

This repository is licensed under the MIT license. See LICENSE for details.
