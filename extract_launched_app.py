from com.android.monkeyrunner import MonkeyDevice, MonkeyRunner
import re
import time

device = MonkeyRunner.waitForConnection()
while True:
    out = device.shell("logcat -d -s ActivityManager && logcat -c")
    lines = out.split("\n")

    cmps = []
    for i, line in zip(range(len(lines)), lines):
        if line.find("android.intent.category.LAUNCHER") != -1:
            cmps.append(line)

    for cmp in cmps:
        print "package:", "".join(re.findall("cmp=([^/]*)/", cmp)[0])

    time.sleep(3)
