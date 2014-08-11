Archey :: OS X
--------------

Simple bash script that displays the Apple logo and some basic information.

### Install

```
#
```

### Usage

To load at start. Add in your [.bashrc][inst] (or .bash_profile). Example:

```
# Load archey (if installed)
[[ `which archey` && $UID != 0 ]] && archey
```

### Screenshot

![][sc]

<span style="font-size: small; color: #555;">_* The picture has a slighlty pale tone since I'm using a semi transparent background in my Terminal (my theme/prefs (“myTerm”) can be found in [dotfiles][mt])_</span>



<!-- Markdown: Links & Images -->
[inst]: https://github.com/iEFdev/dotfiles/blob/master/.bashrc#L87-L88

[mt]: https://github.com/iEFdev/dotfiles

[sc]: https://raw.githubusercontent.com/iEFdev/Archey-OS-X/master/screenshot.png "Screenshot of Archey"