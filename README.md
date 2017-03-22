# Sites Monitoring Utility

The script takes a path to a list of URLs and checks the expiration date and a status code for each one of them. If a domain is responding with code 200 and is prepaid for at least 30 days in advance the script outputs `OK`, otherwise it prints out the status code and (or) indicates whether the domain is expired or not. 
Before using install the modules from the requirements.txt:
```#!bash
$ pip install -r requirements.txt
```

# Usage
```#!bash
$ python check_sites_health.py urls.txt
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
