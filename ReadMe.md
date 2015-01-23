Archey :: OS X
==============

Archey is a simple tool to display system information.

This one comes in 2 versions:

- A Python version (`archey.py`)
- and a bash script (`archey.bash`)

_[#install][local-inst]_
 

archey.py
---------

This is a (forked) ported version of the original script: [Archey][dja], by [djmelek][djm]. Keeping the Arch logo, but differs a bit due to that it is OS X we're dealing with. Also, some information is displayed in the way I made them in the bash version (`archey.bash`).


### Screenshot

![][scrap_py]

<span style="font-size: small; color: #555;">_* The picture has a slighlty pale tone since I'm using a semi transparent background in my Terminal (my theme/prefs (“myTerm”) can be found in [dotfiles][mt])._</span>

 

archey.bash
-----------

This was the first script (I made) of the two. It's a modified version of: "[archey-osx][jfa]" by [Josh Finnie][jfg], who made the original bash script.

To this one I also wrote the screenshot plugin _(see below)_, but that one can be used as a stand alone script.


### Screenshot

![][scrap_bash]

<span style="font-size: small; color: #555;">_* The picture has a slighlty pale tone since I'm using a semi transparent background in my Terminal (my theme/prefs (“myTerm”) can be found in [dotfiles][mt])._</span>

 

Install
-------

Copy the file/version you want to `/usr/local/bin`, give it permission to execute.

	# Example: Python version
	sudo cp archey.py /usr/local/bin/archey
	sudo chmod +x /usr/local/bin/archey

 
...or copy all the files/versions to `/usr/local/bin`, give them permission to execute, and make a symlink to the one you'd like to use.

	sudo cp archey.{py,bash,s} /usr/local/bin
	sudo chmod +x /usr/local/bin/archey.{py,bash,s}

	# Ex: symlink to python
	sudo ln -s /usr/local/bin/archey{.py,}


_(make sure `/usr/local/bin` is in your `PATH`)_

 

Usage
-----

To load at start. Add in your [.bashrc][inst] _(or .bash_profile)_. Example:

```bash
# Load archey (if installed)
[[ `which archey` && $UID != 0 ]] && archey
```
In top of the file there are 2 settings...

```bash
diskWarning=1;             # bool
diskWarningThreshold=20;   # % left on disk left
```

_The disk warning is just a visual blinking warning when the disk space left is below <span style="color: #900;"> 20%</span>._ 


### Colors

In the **python** version... You can change the color scheme by changing the `brand` in top of the file. It says `OS X` _(default)_, but using the names of the other distributions listed in `colorDict` _(Fedora, Mint etc...)_ will use “their colors”. Though, it'll still show OS X in the information displayed.


 

archey.s
--------

`archey.s` is a screenshot-plugin I made xtra to use with `archey.bash`, but can be used as a stand alone script as well. It has a 5 second count down _(5.. 4.. 3.. etc)_ which is useful when you need to make a screenshot but need to press a few keys at the same tim, for example.

To use it with `archey` (bash version):

```bash
archey -s		# screenshot ... countdown from 5 sec
archey -sw		# w = window mode.
```

 

As a stand alone script: _(the only option when using the python version of archey)_

```bash
archey.s		# screenshot ... countdown from 5 sec
archey -w		# w = window mode.
```

 

In top of the file there are a few settings:

```bash
# Settings
# ------------------------------------------------------------
forceDir=0;         # Default: 0. Set to 1 will force to use
                    # "our" directory rather than the normal one.

asDir="$HOME/ArcheyScreenshots";
asType='png';
asPrefix='Archey-OSX';
asDate=`date "+_%F_at_%X" | sed 's/\:/\./g'`;
```

 

There's also an `-f` option to force the use of the folder: `ArcheyScreenshots`.

```bash
archey.s -w -f    // example
```




<!-- Markdown: Links & Images -->
[inst]: https://github.com/iEFdev/dotfiles/blob/master/.bashrc#L115-L116

[mt]: https://github.com/iEFdev/dotfiles
[jfa]: https://github.com/joshfinnie/archey-osx
[jfg]: http://joshfinnie.github.io/

[dja]: https://github.com/djmelik/archey
[djm]: https://github.com/djmelik

[scrap_py]: https://raw.githubusercontent.com/iEFdev/Archey-OS-X/master/screenshot_py.png "Screenshot of Archey (python version)"
[scrap_bash]: https://raw.githubusercontent.com/iEFdev/Archey-OS-X/master/screenshot_bash.png "Screenshot of Archey (bash version)"

[local-inst]: #install "Install instructions"