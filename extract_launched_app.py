import subprocess as sub
import re
import time
import os

#Read configuration.
ips = []
file = open("config", "r")
line = file.readline()
while line != "":
    line = line.rstrip() + ":5555"
    ips.append(line)
    line = file.readline()

#Adb connect
for ip in ips:
    os.system("adb connect " + ip)

outfiles = []
for ip in ips:
    outfiles.append(open(ip, "a"))

while True:
    for ip, outfile in zip(ips, outfiles):
        args = ("adb -s " + ip + " logcat -d && adb -s " + ip + " logcat -c").split()
        p = sub.Popen(args ,stdout=sub.PIPE ,stderr=sub.PIPE)
        out, error = p.communicate()

        lines = out.split("\n")
        cmps = []
        for i, line in zip(range(len(lines)), lines):
            if line.find("android.intent.category.LAUNCHER") != -1:
                cmps.append(line)
        for cmp in cmps:
            outfile.write("package:" +  "".join(re.findall("cmp=([^/]*)/", cmp)[0]) + "\n")

    time.sleep(3)
