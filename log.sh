#!/opt/bin/sh
LOGFILE=/opt/root/log_restart.txt

log(){
   message="$(date +"%y-%m-%d %T") $@"
   #echo $message 
   echo $message >> $LOGFILE

}

log $(/opt/etc/init.d/S51tpws restart 2>&1)
