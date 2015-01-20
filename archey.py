#!/usr/bin/env python
# ------------------------------------------------------------
#
# /usr/local/bin/archey
#
#
# Archey :: OS X
#
# Description:  Archey is a simple system information tool
#               written in Python.
#
# Version:      0.4.0
# Author:       Eric F (iEFdev)
# Copyright:    (c) 2015 Eric F
# Licence:      GNU General Public License v3
#
#
# Author notes:
# ------------------------------------------------------------
#
# This is a forked (ported) version of the original Archey by Melik Manukyan,
# rewritten for OS X.
#
# Original author and copyright:
#
# 	Copyright 2010 Melik Manukyan <melik@archlinux.us>
#
#	ASCII art by Brett Bohnenkamper <kittykatt@silverirc.com>
#	Changes Jerome Launay <jerome@projet-libre.org>
#	Fedora support by YeOK <yeok@henpen.org>
#
# Distributed under the terms of the GNU General Public License v3.
# See LICENSE or http://www.gnu.org/licenses/gpl.txt for the full license text.
#


# Settings
# ------------------------------------------------------------
# diskWarning            (default: 1) with green/red colors
# diskWarningThreshold   (default: 20) % of diskspace left
diskWarning = 1;
diskWarningThreshold = 20;


# OS / Dist (for colors)
# Match a name in in colorDict
brand = 'OS X'


# Import libraries
import os, sys, subprocess, optparse, re, linecache
from subprocess import Popen, PIPE
from optparse import OptionParser
from getpass import getuser
from time import ctime, sleep


# Output
# ------------------------------------------------------------
output = [
	'User',
	'Hostname',
	'Distro',
	'Kernel',
	'Uptime',
	'WindowManager',
	'DesktopEnvironment',
	'Shell',
	'Terminal',
	'Packages',
	'CPU',
	'RAM',
	'Disk'
]


# Dictionaries
# ------------------------------------------------------------
colorDict = {
	'OS X': ['\x1b[0;36m', '\x1b[1;36m'],
	'Arch Linux': ['\x1b[0;34m', '\x1b[1;34m'],
	'Ubuntu': ['\x1b[0;31m', '\x1b[1;31m', '\x1b[0;33m'],
	'Debian': ['\x1b[0;31m', '\x1b[1;31m'],
	'Mint': ['\x1b[0;32m', '\x1b[1;37m'],
	'Crunchbang': ['\x1b[0;37m', '\x1b[1;37m'],
	'Fedora': ['\x1b[0;34m', '\x1b[1;37m'],
	# Sensors: [<red>, <yellow>, <green>, <blinking red>]
	'Sensors': ['\x1b[0;31m', '\x1b[0;32m', '\x1b[0;33m', '\x1b[5;31m'],
	'Clear': ['\x1b[0m']
}

deDict = {
	'Finder': 'Finder'
}

# @todo: check up more on OS X window tiling programs. I think there are 3, 4 or more
wmDict = {
	'Xmonad': 'Xmonad',
	'ShiftIt': 'ShiftIt'
}

logosDict = {brand: '''{color[1]}
{color[1]}               +                {results[0]}
{color[1]}               #                {results[1]}
{color[1]}              ###               {results[2]}
{color[1]}             #####              {results[3]}
{color[1]}             ######             {results[4]}
{color[1]}            ; #####;            {results[5]}
{color[1]}           +##.#####            {results[6]}
{color[1]}          +##########           {results[7]}
{color[1]}         ######{color[0]}#####{color[1]}##;         {results[8]}
{color[1]}        ###{color[0]}############{color[1]}+        {results[9]}
{color[1]}       #{color[0]}######   #######        {results[10]}
{color[0]}     .######;     ;###;`\".      {results[11]}
{color[0]}    .#######;     ;#####.       {results[12]}
{color[0]}    #########.   .########`     {results[13]}
{color[0]}   ######'           '######    {results[14]}
{color[0]}  ;####                 ####;   {results[15]}
{color[0]}  ##'                     '##   {results[16]}
{color[0]} #'                         `#  {results[17]}
\x1b[0m'''
}

# Get processes/names
processes = str(subprocess.check_output(('ps', '-u', getuser(), '-o', 'comm')).split('/')).replace('\\n', '').rstrip('\n')


# Classes
# ------------------------------------------------------------
class Output:
	results = []
	results.extend(['']*(18-len(output)))

	def __init__(self):
		self.distro = self.__detectDistro()

	def __detectDistro(self):
		# OS X file
		if os.path.exists('/System/Library/LaunchDaemons/bootps.plist'):
			return brand
		else:
			sys.exit(1)

	def append(self, display):
		self.results.append('%s%s: %s%s' % (colorDict[self.distro][1], display.key, colorDict['Clear'][0], display.value))

	def output(self):
		print(logosDict[self.distro].format(color = colorDict[self.distro], results = self.results))


class User:
	def __init__(self):
		self.key = 'User'
		self.value = os.getenv('USER')


class Hostname:
	def __init__(self):
		hostname = Popen(['uname', '-n'], stdout=PIPE).communicate()[0].decode('Utf-8').rstrip('\n')
		self.key = 'Hostname'
		self.value = hostname


class Distro:
	def __init__(self):
		if os.path.exists('/System/Library/LaunchDaemons/bootps.plist'):
			productName = Popen(['sw_vers', '-productName'], stdout=PIPE).communicate()[0].decode('Utf-8').rstrip('\n')
			productVersion = Popen(['sw_vers', '-productVersion'], stdout=PIPE).communicate()[0].decode('Utf-8').rstrip('\n')
			buildVersion = Popen(['sw_vers', '-buildVersion'], stdout=PIPE).communicate()[0].decode('Utf-8').rstrip('\n')

			distro = '%s %s (%s)' % (productName, productVersion, buildVersion)

		self.key = 'Distro'
		self.value = distro


class Kernel:
	def __init__(self):
		kernel = Popen(['uname', '-srm'], stdout=PIPE).communicate()[0].decode('Utf-8').rstrip('\n')
		self.key = 'Kernel'
		self.value = kernel


class Uptime:
	def __init__(self):
		getUptime = Popen(['uptime'], stdout=PIPE).communicate()[0].decode('Utf-8').rstrip('\n')
		uptime = re.compile(r'(, )(\d )(.*)').sub(r"", getUptime)
		uptime = re.compile(r'(.*)up (.*)').sub(r"\2 ", uptime)

		self.key = 'Uptime'
		self.value = uptime


class WindowManager:
    def __init__(self):
        wm = ''
        for key in wmDict.keys():
            if key in processes:
                wm = wmDict[key]
                break
        self.key = 'Window Manager'
        self.value = wm


class DesktopEnvironment:
	def __init__(self):
		de = ''

		for key in deDict.keys():

			if key in processes:
				de = deDict[key]
				break

		self.key = 'Desktop Environment'
		self.value = de


class Shell:
    def __init__(self):
        self.key = 'Shell'
        self.value = os.getenv('SHELL')


class Terminal:
    def __init__(self):
        self.key = 'Terminal'
        self.value = os.getenv('TERM')


class Packages:
    def __init__(self):
		checkBrew = Popen(['which', 'brew'], stdout=PIPE).communicate()[0].decode('Utf-8').rstrip('\n')

		p1 = Popen(['which', 'brew', '-l'], stdout=PIPE).communicate()[0].decode('Utf-8').rstrip('\n')
		packages = len(p1.rstrip('\n').split('\n'))

		self.key = 'Packages'

		if checkBrew:
			self.value = packages
		else:
			self.value = 'n/a'


class CPU:
	def __init__(self):
		cpuinfo = Popen(['sysctl', '-n', 'machdep.cpu.brand_string'], stdout=PIPE).communicate()[0].decode('Utf-8').rstrip('\n')
		cpuinfo = re.sub('  +', ' ', cpuinfo.replace('CPU ', '').rstrip('\n'))
		self.key = 'CPU'
		self.value = cpuinfo


# Memory information
# ------------------------------------------------------------
# Display: (used = red) (free = green) total
#
class RAM:
	def __init__(self):
		memSize = Popen(['sysctl', '-n', 'hw.memsize'], stdout=PIPE).communicate()[0].decode('Utf-8').rstrip('\n')
		memTotalRam = int(memSize) / int(1000000000)

		vmStat = Popen(['vm_stat'], stdout=PIPE).communicate()[0].decode('Utf-8').rstrip('\n')
		vmStat = re.sub('  +', ' ', vmStat.replace('.', '').rstrip('\n'))

		# Using vm_stat to get all the memory
		memFree = vmStat.splitlines()[1].split()[2]
		memActive = vmStat.splitlines()[2].split()[2]
		memInactive = vmStat.splitlines()[3].split()[2]
		memSpeculative = vmStat.splitlines()[4].split()[2]
		memWired = vmStat.splitlines()[5].split()[3]

		# Used memory
		# These 3 are matching "1234M used" in: top (and Activity Monitor)
		memUsed = (int(memWired) + int(memActive) + int(memInactive)) * int(4096) / int(1024) / int(1024)

		# Total free
		memTotalFree = (int(memFree) + int(memSpeculative)) * int(4096) / int(1024) / int(1024)

		usedpercent = ((float(memUsed) / int(memTotalRam * 10)))

		# Red = used, Green = free
		ucolor = 0
		if diskWarning == 1 and usedpercent >= 80:
			ucolor = 3

		# [note]
		# I's a little bit of a mess, and slightly confusing.
		# Size of total memory (memTotalRam) is easy to get, but adding up what's
		# used seems it's using MiB instead of MB. Haven't figured out a way to solve it.
		# Did try a few different settings, but any ideas/suggestions/improvements are welcome.

		# RAM:	(used) (free) / total
		ramdisplay = '%s(%s MB) %s(%s MB)%s / %s GB' % (colorDict['Sensors'][ucolor], memUsed, colorDict['Sensors'][1], memTotalFree, colorDict['Clear'][0], memTotalRam)

		self.key = 'RAM'
		self.value = ramdisplay


# Disk information
# ------------------------------------------------------------
# Display: used/N% of total (N available) (disk)
#
class Disk:
	def __init__(self):
		p1 = Popen(['df', '-lH'], stdout=PIPE).communicate()[0].decode("Utf-8")
		total = p1.splitlines()[1]
		used = total.split()[2]
		size = total.split()[1]
		available = total.split()[3]
		capacity = total.split()[4]
		disknr = total.split()[0].replace('/dev/', '')
		usedpercent = int(capacity.replace('%', ''))
		leftpercent	= (100 - int(usedpercent))

		if usedpercent <= 33:
			diskcolor = 1
		if usedpercent > 33 and usedpercent < 67:
			diskcolor = 2
		if usedpercent >= 67:
			diskcolor = 0
		if diskWarning == 1 and leftpercent <= int(diskWarningThreshold):
			diskcolor = 3

		disk = '%s/%s%s%s of %s (%s available) (%s)' % (used, colorDict['Sensors'][diskcolor], capacity, colorDict['Clear'][0], size, available, disknr)

		self.key = 'Disk'
		self.value = disk


classes = {
	'User': User,
	'Hostname': Hostname,
	'Distro': Distro,
	'Kernel': Kernel,
	'Uptime': Uptime,
	'WindowManager': WindowManager,
	'DesktopEnvironment': DesktopEnvironment,
	'Shell': Shell,
	'Terminal': Terminal,
	'Packages': Packages,
	'CPU': CPU,
	'RAM': RAM,
	'Disk': Disk
}

out = Output()
for x in output:
	out.append(classes[x]())
out.output()
