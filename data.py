from datetime import datetime
from time import sleep
from os import remove

logging = 1


def main():
    rawData = 0
    try:
        f = open("/home/pi/tempRainPi/rawdata.txt", "r")
        rawData = f.read()
    except:
        sleep(1)

    if rawData and len(str(rawData)) > 98:
        wf = open("/home/pi/tempRainPi/data.txt", "w")
        #data = "11111110011000001010010010000110101011000000011111111110011010101101110011100101110001100101111"
        data = rawData[0:88]
        time = int(rawData[89:99])
        temp_in = round(float(rawData[100:105]) / 1000, 1)
        d = []
        dd = []
        i = 0
        while i < 87:
            d.append(data[i:i+8])
            i += 8

        check = 0
        index = 0
        for i in d:
            val = '0b' + i
            dd.append(int(val, 2))

        for i in d:
            val = '0b' + i
            check += int(val, 2)

            if index == 6:
                break
            else:
                index += 1

        temp = round((((dd[1] & 0x7) << 8 | dd[2]) - 400) * 0.1, 1)
        rain = round((dd[4] << 8 | dd[3]) * 0.3)

        if (check - int("0b" + str(d[7]), 2) & 255) and logging == 1:
            print("checksum err: IS '" + str(check -
                                             int("0b" + str(d[7]), 2) & 255) + "', SHOULD BE '0' - " + str(datetime.fromtimestamp(time)))
        elif (check - int("0b" + str(d[7]), 2) & 255) == 0:
            if logging == 1:
                print("Zeit: " + str(datetime.fromtimestamp(time)))
                print("Niederschlag: " + str(rain) + " mm")
                print("Temperatur OUT: " + str(temp) + " °C")
                print("Temperatur IN: " + str(temp_in) + " °C\n")
            wf.write(str(time) + "000000000" + ";" + str(temp) +
                     ";" + str(temp_in) + ";" + str(rain))
        remove("/home/pi/tempRainPi/rawdata.txt")
        rawData = 0
    else:
        0


if __name__ == "__main__":
    rawData = 0
    try:
        while True:
            try:
                main()
            except KeyboardInterrupt:
                print("\naus")
                break
            except:
                if logging == 1:
                    print("error")
                sleep(1)
    except:
        print("error")
