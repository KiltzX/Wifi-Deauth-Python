# Wifi-Deauth-Python

Wifi-Deauth-Python is a Python library for automate wifi deauth attack.

## Installation

You need airmon-ng and airodump installed in your machine
I tested using Kali-Linux 2021.2

```bash
git clone https://github.com/KiltzX/Wifi-Deauth-Python
```

## Usage


```bash
sudo python3 start.py #Get wifi interfaces and enable monitor mode
sudo python3 deauth.py [interface] #To start from deauth attack
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)