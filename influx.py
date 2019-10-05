from influxdb import InfluxDBClient
from time import sleep

client = InfluxDBClient(host='raspi3-emil.local',
                        port=8086, database='tempRainPi')


def send_data():
    file = open("/home/pi/tempRainPi/data.txt", "r")

    rawdata = file.read()
    data = rawdata.split(";")

    last_rain = client.query(
        'select last("totalRain") from "weather"').raw['series'][0]['values'][0][1]

    json_body = [
        {
            "measurement": "weather",
            "tags": {},
            "time": int(data[0]),
            "fields": {
                "out": float(data[1]),
                "in": float(data[2]),
                "rain": (float(data[3]) - last_rain),
                "totalRain": float(data[3])
            }
        }
    ]

    client.write_points(json_body)


if __name__ == "__main__":
    try:
        send_data()
    except Exception as ex:
        print("error\n", ex)
