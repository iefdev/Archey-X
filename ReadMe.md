Archey :: OS X
--------------

Simple bash script that displays the Apple logo and some basic information.

---

><span style="font-size: small; color: #555;">_Credits: This is a modified version of: "[archey-osx][jfa]" by [Josh Finnie][jfg], who made the original bash script. The name Archey is of course based on [Archey][dja], by [djmelek][djm]._</span>


### Install

Copy the files to `/usr/local/bin`, and give them execute permission.

```
sudo cp archey{,.s} /usr/local/bin
sudo chmod +x /usr/local/bin/archey{,.s}
```

### Usage

To load at start. Add in your [.bashrc][inst] _(or .bash_profile)_. Example:

```
# Load archey (if installed)
[[ `which archey` && $UID != 0 ]] && archey
```
In top of the file there are 2 settings...

```
diskWarning=1;             # bool
diskWarningThreshold=20;   # % left on disk left
```
_The disk warning is just a visual blinking warning (of <span style="color: #900;"> > 80%</span>)._ 



#### archey.s

`archey.s` is a screenshot-plugin I made xtra to use with `archey`, but can be used as a stand alone script as well.

To use it with `archey`:

```
archey -s		# screenshot ... countdown from 5 sec
archey -sw		# w = window mode.
```
As a stand alone script:

```
archey.s		# screenshot ... countdown from 5 sec
archey -w		# w = window mode.
```

In top of the file there are a few settings:

```
# Settings
# ------------------------------------------------------------
forceDir=0;         # Default: 0. Will force to use "our"
                    # directory rather than the normal one.

asDir="$HOME/ArcheyScreenshots";
asType='png';
asPrefix='ArcheyOSX';
asDate=`date "+_%Y-%m-%d_at_%H.%M.%S"`;
```

There's also an `-f` to force the use of `ArcheyScreenshots`.

```
archey.s -w -f    // example
```



### Screenshot

![][sc]

<span style="font-size: small; color: #555;">_* The picture has a slighlty pale tone since I'm using a semi transparent background in my Terminal (my theme/prefs (“myTerm”) can be found in [dotfiles][mt])_</span>



<!-- Markdown: Links & Images -->
[inst]: https://github.com/iEFdev/dotfiles/blob/master/.bashrc#L87-L88

[mt]: https://github.com/iEFdev/dotfiles
[jfa]: https://github.com/joshfinnie/archey-osx
[jfg]: http://joshfinnie.github.io/

[dja]: https://github.com/djmelik/archey
[djm]: https://github.com/djmelik

[sc]: https://raw.githubusercontent.com/iEFdev/Archey-OS-X/master/screenshot.png "Screenshot of Archey"