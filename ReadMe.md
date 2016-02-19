# Archey :: OS X

Archey is a simple tool to display system information.


## archey

This is a (forked) ported version of the original script: [Archey][dja], by [djmelek][djm]. Keeping the **Arch** logo, but differs a bit due to that it is OS X we're dealing with. Also, some information is displayed in the way I made them in the bash version I initially made.


### Screenshot

![][scrap]

A few more Screenshots can be found in the [Wiki][scraps].

_Terminal theme: [myTerm][myterm]_



## Install

Copy the file to `/usr/local/bin`, and give it permission to execute.

	sudo install -m 0755 archey /usr/local/bin


_(make sure `/usr/local/bin` is in your `PATH`)_


The “shebang” is set to `python3`. If you don't have Python 3.* you can just change it to `python` _(manually)..._

	#!/usr/bin/env python3

	#!/usr/bin/env python


_...or using sed._

	sed -i '' '/env python3$/s/3//' archey   # OS X sed
	sed -i '/env python3$/s/3//' archey      # GNU sed



## Usage

To load at start. Add in your [.bashrc][brc] _(or .bash_profile)_. Example:

```
# Load archey (if installed)
[[ `which archey` && $UID != 0 ]] && archey
```


_The (old) plugin: `archey.s` is gone, but you can get it from the `bash-version`
 branch._



## Settings

In top of the file there are a few settings...


### Disk

	# Settings
	# ------------------------------------------------------------
	diskWarning = 1             # default: 1
	diskWarningThreshold = 20   # default: 20 (% of diskspace left)


The disk warning is just a visual blinking warning when the disk space left is below <span style="color: #900;"> 20%</span>.


### Colors

	# Custom color (match a name in in colorDict)
	# Must have one with 'None' (defaults to Darwin)
	brand = None
	#brand = 'Arch Linux'	# Note: blue is almost purple in OS X
	#brand = 'Darwin'		# OS X
	#brand = 'Mint'
	#brand = 'Fedora'
	# ------------------------------------------------------------
	# [End] Settings


`brand = None` will default to Darwin. You only need to change `brand` if you want a different color scheme. Like “Arch Linux” is all blue, “Mint” is green/white, and “Fedora” is blue/white.

_Note: The blue color in OS X is not that really good - almost purple'ish._


- - -


# Author notes

**[2016-02-17]**

“Archey :: OS X” will come in tags/releases now, and this is the “dev” version _(eg v1.2.3-yymmdd-git)_. You should use the releases.

I started a wiki... Not much there at the moment, but I'd guess a few pages will show up there later.

If you have any feedback, suggestions? Please, send an email or a tweet.

 · Eric


<!-- Markdown: Links & Images -->
[brc]: https://github.com/iEFdev/dotfiles/blob/master/osx/.bashrc#L67-L68

[dja]: https://github.com/djmelik/archey
[djm]: https://github.com/djmelik

[scrap]: https://raw.githubusercontent.com/iEFdev/Archey-OS-X/master/screenshot.png "Screenshot of Archey :: OS X"
[scraps]: https://github.com/iEFdev/Archey-OS-X/wiki/Screenshots "More Screenshots"
[myterm]: https://github.com/iEFdev/dotfiles/tree/master/myTerm "My Terminal theme"
[jy]: https://github.com/iEFdev/junkyard "iEFdev/Junkyard"