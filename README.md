physicalShutdownRPI
===================

A Physical Shutdown Button For raspberry pi B.

Download the code.

Give excutable permission to both the file by chmod +x

open lunchshutdown.sh file and give the path of the .py file


open crontab by "sudo crontab -e" to add the lunchshutdown.sh to startup

copy the bellow line into end of crontab
@reboot sh /home/pi/yourfilepath/lunchshutdown.sh

save crontab and reboot 

Power one th RPI again. Push tht shutdown to halt the system. 

Thanks

Keep Visiting for more tutorials.
www.embeddedhacks.in 



