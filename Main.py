import WeatherPi
from time import sleep

def main():
    while True:
        WeatherPi.main()
        sleep(300)

if __name__ == '__main__':
	main()
