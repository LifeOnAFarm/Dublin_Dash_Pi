![alt tag](https://raw.githubusercontent.com/LifeOnAFarm/Dublin_Bus_Dash/master/pics/dash.png)


## Synopsis



This is a simple application that uses a Amazon Dash button to read out the due times of a dublin bus stop. Changes need to be made in the python files to pick which bus stop you want read out, the MAC address of your dash button and the absolute path names of your sound files. In a future update I'll add the choice of which bus is arriving at the bus stop.
This works using Python 3
 on the Raspberry Pi.

## Motivation



I made this project because I often find it a pain using the Dublin Bus app. This way I only need to press one simple button and the next bus time is read out to me. I also managed to get a Dash button and wanted to make some sort of projectt with it.



## License



MIT License - Have fun folks



## Link



[Here's](https://evolution.voxeo.com/library/audio/prompts/) where I got the sound files. These need to be saved as absolute paths in the python code if you want it to run at start up.

[This](http://www.raspberrypi-spy.co.uk/2013/07/running-a-python-script-at-boot-using-cron/) link will show you how to get a python script running at startup on the Raspberry Pi.