from influxdb import InfluxDBClient
from time import *
import fcntl

client = InfluxDBClient(host='raspi3-emil.local',
                        port=8086, database='tempRainPi')


def send_data():
    unlock = 0
    file = open("/home/pi/tempRainPi/data.txt", "r")
    while unlock == 0:
        try:
            fcntl.flock(file, fcntl.LOCK_EX | fcntl.LOCK_NB)
            unlock = 1
        except:
            sleep(1)
    rawdata = file.read()
    fcntl.flock(file, fcntl.LOCK_UN)
    file.close()
    data = rawdata.split(";")

    last_rain = client.query(
        'select last("totalRain") from "weather"').raw['series'][0]['values'][0][1]

    if (float(data[3]) - last_rain) < 0 or (float(data[3]) - last_rain) > 20:
        raise Exception(
            f'The rain difference is {(float(data[3]) - last_rain)} and thereby a wrong value.')
        return

    json_body = [
        {
            "measurement": "weather",
            "tags": {},
            "time": int(data[0]),
            "fields": {
                "out": float(data[1]),
                "in": float(data[2]),
                "rain": (float(data[3]) - last_rain),
                "totalRain": float(data[3]),
                "pressure": float(data[4]),
                "humidityIn": float(data[5])
            }
        }
    ]

    client.write_points(json_body)


if __name__ == "__main__":
    try:
        send_data()
    except Exception as ex:
        print("error\n", ex)
        errorfile = open("/home/pi/tempRainPi/err.txt", "a")
        errorfile.write(str(ex) + str(time()) + "\n")
        sleep(150)
        send_data()
