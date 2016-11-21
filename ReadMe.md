# Archey X

Archey X is a simple tool to display system information.

- - - 


This is a (forked) ported version of the original script: [Archey][dja], by [djmelek][djm]. It was first made as a bash script version for OS X. Later on the original `archey` script was ported to OS X. Now it's been re-worked to be X compatible with both OS X and misc GNU/Linux distributions - hence the name: _Archey **X**_.


### Screenshot

![][scrap]
_(v0.7.0-beta on OS X)_

OS X Terminal theme: [myTerm][myterm]. A few more Screenshots can be found in the [Wiki][scraps].



## Install

Copy the file to `/usr/local/bin`, and give it permission to execute.

	sudo install -m 0755 archey /usr/local/bin

_(make sure `/usr/local/bin` is in your `PATH`)_



## Python version

Archey X is written and tested with `pylint (1.6.4)` with `python3 (3.5.2)`. If you don't have Python 3.* - you need to change the _shebang_ to `python`...

	#!/usr/bin/env python3

	#!/usr/bin/env python

_...or using sed._

	sed -i '' '/env python3$/s/3//' archey   # OS X sed
	sed -i '/env python3$/s/3//' archey      # GNU sed

You will also need to comment or remove the line with: _(~[L302][super])_

```python
super().__init__()
```



## Usage

    archeyX

To load at start. Add to your `.bashrc` _(or `.bash_profile`)_:

```bash
# Load archey (if installed)
[[ `type archey 2> /dev/null` && $UID != 0 ]] && archey
```

When using `scp` over the network and logging into amachin with `archeyX` loading up... It _might_ cause an error about output. To avoid that issue, use this instead:

```bash
# Load archey (if installed)
# If not running interactively, don't do anything
[[ -n "$PS1" && `type archey 2> /dev/null` && $UID != 0 ]] && archey
```



## Settings

In top of the file there are a few settings...


### Disk

```python
# Settings
DISK_WARNING = 1                # default: 1
DISK_WARNING_THRESHOLD = 20     # default: 20 (% of diskspace left)
```

The disk warning is just a visual blinking warning when the disk space left is below <span style="color: #900;"> 20%</span>.


### Colors

```python
# Custom color (match a name in in COLOR_DICT)
# You can manually change color here by adding a new line with 'brand'.
BRAND = None                    # Must have one with 'None' (don't change)
#BRAND = 'Arch Linux'
#BRAND = 'Darwin'                # OS X
```

You only need to add (a new line with) `BRAND` if you want a different color scheme. A way to _hard-code_ the color if your ditribution isn't in `DIST_DICT`.


- - -


# Author notes

-	**[2016-11-21]**

	This repo has been renamed from: “Archey :: OS X” -> “Archey X”, since it will be X-compatible. Initial version(s) will be `v0.7.0-YYYMMDD-beta` until it's been tested/verified more to work with _N_ distributions.


-	**[2016-02-17]**

	“Archey :: OS X” will come in tags/releases now, and this is the “dev” version _(eg v1.2.3-yymmdd-git)_. You should use the releases.

	I started a wiki... Not much there at the moment, but I'd guess a few pages will show up there later.


If you have any feedback, suggestions? Please, send an email or a tweet.


· Eric


<!-- Markdown: Links & Images -->
[super]: https://github.com/iEFdev/Archey-X/blob/master/archeyX#L302

[dja]: https://github.com/djmelik/archey
[djm]: https://github.com/djmelik

[scrap]: https://raw.githubusercontent.com/iEFdev/Archey-X/master/screenshot.png "Screenshot of Archey X"
[scraps]: https://github.com/iEFdev/Archey-X/wiki/Screenshots "More Screenshots"
[myterm]: https://github.com/iEFdev/dotfiles/tree/master/myTerm "My Terminal theme"
[jy]: https://github.com/iEFdev/junkyard "iEFdev/Junkyard"