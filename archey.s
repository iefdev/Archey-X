#!/bin/bash
# ------------------------------------------------------------
#
# /usr/local/bin/archey
#
#
# Plugin for Archey :: OS X
#
# Description:  Built to add a screenshot feature to Archey-OS X,
#               but can run as a stand alone script.
#
# Usage:        archey -s    archey -sw
#               archey.s     archey.s -w
#
# Author:       Eric F (iEFdev)
# Copyright:	    (c) 2013, Eric F
# Licence:      The MIT License (MIT)
#


# Settings
# ------------------------------------------------------------
forceDir=0;         # Default: 0. Will force to use "our"
                    # directory rather than the normal one.

asDir="$HOME/ArcheyScreenshots";
asType='png';
asPrefix='ArcheyOSX';
asDate=`date "+_%Y-%m-%d_at_%H.%M.%S"`;


# Directory
# ------------------------------------------------------------
# Where to store the image

# Force it with a handler ("f"), when the setting is set to 0?
if [[ $forceDir == 0 ]] && [[ $@ =~ [f] ]]; then forceDir=1; fi

# First, get the user path to screenshots...
# If there's no default location. Create a folder and use it.
uDir=`defaults read com.apple.screencapture location | sed 's/[ \/]*$//'`;
if [[ $uDir != '' ]] && [[ $forceDir == 0 ]]; then
	asDir="$uDir";
elif [[ $uDir == '' ]] || [[ $forceDir == 1 ]]; then
	if [[ ! -d $asDir ]]; then
		mkdir -p $asDir;
	fi
fi


# Function _help()
# Perhaps someone find it useful :)
function _help() {
	if [[ $thisArchey == 'archey.s' ]]; then
			uUse='[-w]';
			hS='default';
			hSW='-w ';
	else
			uUse='[-sw]';
			hS='-s';
			hSW='-sw';
	fi

	cat <<EOF

Usage: $thisArchey $uUse[-f][--help]

	$hS	  Takes a screenshot of the full display

	$hSW	  Triggers a window mode.
	    	  (Unfortunately not automatically. Needs a click.)

	-f	  Will force to use the folder defined as: \"\$asDir=[DIR]\"
	    	  in the settings, if \"forceDir=0\". If the folder doesn't
	    	  exists, it will try to create it.

	- - - - -

	When the picture is taken it will be revealed in Finder.

EOF
}


# Function _counter
# 5.. 4.. 3.. 2.. 1..
function _counter() {
	echo -n "Taking a screenshot in: "
	for i in {5..1}.. '[Click!]'; do
		echo -n "$i ";
		sleep 1;
	done;
	echo;
}


# More variables
asImg="$asDir/$asPrefix$asDate.$asType";
asMode="$1";
asSec=1;
thisArchey=`basename "$0"`;


# Ok, who's who..?
# ------------------------------------------------------------

# archey.s
if [[ $asMode == '' ]] && [[ $thisArchey == 'archey.s' ]]; then
	_counter;
	asOpts='xo';
elif  [[ $asMode != '' ]]; then
	case $asMode in

		# archey, archey.s
		--help)
			_help;
			;;

		# archey
		-s)
			if [[ $thisArchey == 'archey.s' ]]; then $0 *;
			else
				_counter;
				asOpts='xo';
			fi
			;;

		# archey, archey.s
		-w|-sw)
			if [[ $thisArchey == 'archey.s' && $asMode != '-w' ]]; then $0 *;
			else
				asOpts='xow';
				asSec=0;
			fi
			;;

		# Oops
		*)
			if [[ $thisArchey == 'archey.s' ]]; then uUse='[-w][-f]'; else uUse='[-sw][-f]'; fi
			echo -e " :» $thisArchey:\tillegal option. ($@)";
			echo -e " :» usage:\t$thisArchey $uUse[--help]";
			exit;
			;;

	esac
fi

# ...and here we go.
if [[ $asOpts ]]; then
	asOpt="-T $asSec -t $asType -$asOpts";
	screencapture $asOpt $asImg && open -R $asImg;
fi

# Bye bye...
exit;
