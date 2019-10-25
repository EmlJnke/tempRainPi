# Fork of untergasser/tempRainPi

This is a Fork of the original [tempRainPi](https://github.com/untergasser/tempRainPi) to further develop the great work of Andreas Untergasser to fit all my purposes.

Almost all C++ Code is written by him so credits go to [Untergasser](https://github.com/untergasser)!

## TempRainPi

This is a proof of concept project to decode wireless weather sensors with simple modules running on a Raspberry Pi. Currently, it only supports the Alecto WS 1200. As the receiver is responsible for decoding the frequency, it should work with 868Mhz as well as 433Mhz depending on the device used. The Raspberry Pi does  
not handle any high frequency decoding and just reads the signal on one pin 10000 times per second.  
In principle, it could work for any frequency if decoders are available and the output signal is digital. Cheap modules supporting on/off keying (OOK) modulation are available. The code only requires the [WiringPi library](http://wiringpi.com/). It consumes low amounts of energy and is computationally cheap.

## Prerequisites

- [Raspberry Pi](https://www.raspberrypi.org/)
- [Generic 433Mhz reciver](https://github.com/milaq/rpi-rf) or (not used here) [RX868 receiver for 868.35Mhz](http://www.elv.de/output/controller.aspx?cid=74&detail=10&detail2=42432)
- [WiringPi library](http://wiringpi.com/)

The transmitter can be used to send an identical signal, which can be recorded with an SDR:

`rtl_fm -M am -f 433.9M -s 10k > rtl.dat`

And visualized with audacity (import raw data, Signed 16 bit PCM, Little-endian and Mono).
The station displays do not respond to the signal yet, probably due to the low amplitude.

## History and Credits

The whole idea and the basic source code were inspired by the [TempHygroRX868](https://github.com/skaringa/TempHygroRX868) which [Martin Kompf](https://github.com/skaringa), whose [web page](https://www.kompf.de/tech/rxdec.html) I also really enjoy, developed.

The hardware setup is identical to [rpi-rf](https://github.com/milaq/rpi-rf). I furthermore use the same sensors and wiring of the sensors
and Raspberry Pi, but no code provided. It inspired the idea to send data back to the display.

A great project to deal with weather sensors is [rtl_433](https://github.com/merbanan/rtl_433).

Many thanks to Benjamin Larsson and especially to Christian W. Zuckschwerdt for their support [decoding the Alecto WS-1200 signals](https://github.com/merbanan/rtl_433_tests/tree/master/tests/alecto_ws_1200/01).

After all that I still depend on code from [tfrec (SDR for TFA KLIMALOGG Pro sensors)](https://github.com/baycom/tfrec).

## License

Copyright 2019 Andreas Untergasser (+Emil Jahnke)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
