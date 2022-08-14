import os, json

try:
    bReport = os.popen("termux-battery-status").read()
    bReport = json.loads(bReport)
    bStatus = bReport['status']

    nReport = os.popen("termux-notification-list").read()
    nReport = json.loads(nReport)
    lNoti = nReport[0]

    if 'lines' in lNoti.keys():
        Obj = {"BatteryStaus":bStatus,"Battery%":bReport['percentage'],"NotificationFrom":lNoti['packageName'],"NotificationContent":lNoti['lines']}
    else:
        Obj = {"BatteryStaus":bStatus,"Battery%":bReport['percentage'],"NotificationFrom":lNoti['packageName'],"NotificationContent":lNoti['content']}
except:
    print('An error occured')