import subprocess as sub
from datetime import datetime
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
    outfiles.append(open(ip, "w"))

while True:
    for ip, outfile in zip(ips, outfiles):
        args = ("adb -s " + ip + " shell cat /proc/meminfo").split()
        p = sub.Popen(args ,stdout=sub.PIPE ,stderr=sub.PIPE)
        out, error = p.communicate()
        outfile.write("--------------------------------------------------\n");
        outfile.write(str(datetime.now()) + "\n")
        outfile.write(out);
        outfile.write("--------------------------------------------------\n\n");

    time.sleep(3)
