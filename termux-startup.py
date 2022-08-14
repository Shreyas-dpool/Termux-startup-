import os, json

breport = os.popen("termux-battery-status").read()
bReport = json.loads(breport)
bStatus = bReport['status']

nReport = os.popen("termux-notification-list").read()
nreport = json.loads(nReport)
lNoti = nreport[0]

if 'lines' in lNoti.keys():
    Obj = {"BatteryStaus":bStatus,"Battery%":bReport['percentage'],"NotificationFrom":lNoti['packageName'],"NotificationContent":lNoti['lines']}
else:
    Obj = {"BatteryStaus":bStatus,"Battery%":bReport['percentage'],"NotificationFrom":lNoti['packageName'],"NotificationContent":lNoti['content']}

print(Obj)