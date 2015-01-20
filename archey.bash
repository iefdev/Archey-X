#!/usr/bin/env bash
# ------------------------------------------------------------
#
# /usr/local/bin/archey
#
#
# Archey :: OS X
#
# Description:  Tool (bash script) to display system information.
#               Includes an option/plugin to take screenshots.
#
# Version:      1.0.0
# Author:       Eric F (iEFdev)
# Copyright:    (c) 2015 Eric F
# Licence:      GNU General Public License v3
#
# Author notes: This is a modified version of: "archey-osx"
#               by Josh Finnie.
#                   ↳ https://github.com/joshfinnie/archey-osx
#                   ↳ http://joshfinnie.github.io/
#


# Settings
# ------------------------------------------------------------
# diskWarning            (default: 1) with green/red colors
# diskWarningThreshold   (default: 20) % of diskspace left
diskWarning=1;
diskWarningThreshold=20;


# Colors
# ------------------------------------------------------------
# 2 first lines = the apple and the labels

b_c="\033[1;36m";		# b_c = ascii:bold color
n_c="\033[0;36m";		# n_c = ascii:normal color
g_c="\033[0;32m";		# g_c = green color
r_c="\033[0;31m";		# r_c = red color
w_c="\033[5;31m";		# w_c = red color (warning) (5; = blinking)
e_c="\033[0m";			# e_c = empty color (eg reset)


# Archey variables
# ------------------------------------------------------------

# User
user=$(whoami);

# Hostname
hostname=$(uname -n);

# Distro
distro="$(sw_vers -productName) $(sw_vers -productVersion) ($(sw_vers -buildVersion))";

# Kernel
kernel=$(uname -srm);

# Uptime: Example: "35 min" or "1 day, 12:35" or "1 day, 10 min"
uptime=$(uptime | sed 's/  / /g' | sed 's/.*up \([^,].*\),.*/\1/' | sed 's/\([^,].*\),.*/\1/');

# Shell and Terminal
shell="$SHELL";
terminal="$TERM";

# Packages
# Display nice if Homebrew isn't installed
if [[ `which brew` ]] && return 1; then
	packages="`brew list -l | wc -l | awk '{ print $1 }'`";
else
	packages="n/a";
fi

# CPU (info)
cpu=$(sysctl -n machdep.cpu.brand_string | sed -e 's/  */ /g' | sed 's/CPU\ //');


# Memory section
# ------------------------------------------------------------
# Display: (used = red) (free = green) total
#
memSize=$(sysctl -n hw.memsize);
memTotalRam="$((memSize/1000000000)) GB";

# Using vm_stat to get all the memory
memFree=$(vm_stat | grep "free" | awk '{ print $3 }' | sed 's/\.//');
memInactive=$(vm_stat | grep "Pages inactive" | awk '{ print $3 }' | sed 's/\.//');
memSpec=$(vm_stat | grep "speculative" | awk '{ print $3 }' | sed 's/\.//');
memWired=$(vm_stat | grep "wired" | awk '{ print $4 }' | sed 's/\.//');
memActive=$(vm_stat | grep "Pages active" | awk '{ print $3 }' | sed 's/\.//');

# Used memory
# These 3 are matching "1234M used" in: top (and Activity Monitor)
memUsed=$((($memWired+$memActive+$memInactive)*4096/1024/1024));

# Total free
memTotalFree=$((($memFree+$memSpec)*4096/1024/1024));

# [note]
# I's a little bit of a mess, and slightly confusing. Size of total memory ($memTotalRam) is easy to
# get, but adding up what's used seems it's using MiB instead of MB. Haven't figured out
# a way to solve it. Did try a few different settings, but any ideas/suggestions/improvements
# are welcome.

# RAM:	(used) (free) total
ram=`echo -e "$r_c($memUsed MB)$e_c $g_c($memTotalFree MB)$e_c / $memTotalRam"`;


# Function _disk()
# ------------------------------------------------------------
# Display: used/N% of total (N available) (disk)
#
function _disk() {

	if [[ $diskWarning == 0 ]]; then

		# Without colors...
		disk=`df -Hl | head -2 | tail -1 | awk '{print $3"/"$5 " of " $2 " (" $4 " available) (" $1 ")"}'  | sed 's/\/dev\///g'`;
	else
		# DiskWarning will show some red text when the space
		# left on disk is below the setting.

		# used size
		uSize=`df -Hl | head -2 | tail -1 | awk '{ print $3}'`;

		# used size (%)
		pSize=`df -Hl | head -2 | tail -1 | awk '{ print $5}'`;

		# total size
		totSize=`df -Hl | head -2 | tail -1 | awk '{ printf "of %-1s", $2}'`;

		# available size
		aSize=`df -Hl | head -2 | tail -1 | awk '{ printf "(%-1s available)", $4}'`;

		# diskNsN
		mPoint=`df -Hl | head -2 | tail -1 | awk '{printf "(%-1s)", $1}'  | sed 's/\/dev\///g'`;

		# Ok... If the disk is more than 80% full?
		if [[ $pSize > $((100-$diskWarningThreshold)) ]]; then
			pSize="$w_c$pSize$e_c";		# Blink % + red color
			aSize="$r_c$aSize$e_c";		# red color
		else
			pSize="$g_c$pSize$e_c";		# % in green color
		fi

		# Sum up ...
		disk="$uSize/$pSize $totSize $aSize $mPoint";
	fi
}
# load
_disk;


# Archey :: OS X
# ------------------------------------------------------------
echo -e "
$b_c                        ##  $n_c         User:$e_c      $user
$b_c                     #####  $n_c         Hostname:$e_c  $hostname
$b_c                    #####   $n_c         Distro:$e_c    $distro
$b_c                  #####     $n_c         Kernel:$e_c    $kernel
$b_c                  ###       $n_c         Uptime:$e_c    $uptime
$b_c           #####      ##### $n_c         Shell:$e_c     $shell
$b_c       #####################$n_c#        Terminal:$e_c  $terminal
$b_c     ###################$n_c#######      Packages:$e_c  $packages
$b_c    ################$n_c#########        CPU:$e_c       $cpu
$b_c    #############$n_c###########         RAM:$e_c       $ram
$b_c    ##########$n_c#############          Disk:$e_c      $disk
$b_c    #######$n_c#################   $e_c
$b_c    #####$n_c##################### $e_c
$b_c     ###$n_c#######################$e_c
$b_c      #$n_c####################### $e_c
$n_c        #####################  $e_c
$n_c         ##################    $e_c
$n_c           ####      ####      $e_c
";


# Plugins
# ------------------------------------------------------------

# Import the archey.s plugin (if installed)
# The plugin will add a screenshot feature
if [ -f `which archey.s` ] && [[ $1 != '' ]]; then
	. `which archey.s`;
fi

exit;
