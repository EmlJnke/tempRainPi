path=/home/pi/tempRainPi/influx_backup/backup-$(date +%F)
mkdir $path
influxd backup -portable $path