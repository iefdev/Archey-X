# Changes

Changes that have been made between the versions.

- [ ] _todo: move this file to Wiki: Changelog._

- - -

> **Latest version:** v0.7.0-beta

### Changes since: `v0.6.1` (Nov 21, 2016)

-	Fixed better compare of floats in version nr (`free`).
-	Replaced `optparse` (deprecated) with `argparse`.
-   Code has been rn with pylint. Only 1 report left, and that's the filename - which I intend to keep.
-   Optimized/refactored some code
-   Removed `platform.linux_distribution()`. It's deprecated
    and flagged for removal, so...
-   A new function to detect distro name and full distro name. No using `/etc/{{os,lsb}-release,issue}` and `lsb_release [-si|-sd]`. In that way everything can take place in on function.
-   A new function to parse the release files
-   New (xtra) dict - separating distros and colors, to 1 color for multiple dists
-   RAM and Disk output is formatted a bit different
-   Changed the %-levels for disk-colors
-   Added `simfs` and `tmpfs` as mentioned here:
    - <https://github.com/djmelik/archey/pull/38>
    - <https://github.com/djmelik/archey/issues/39>


> **Note:** v0.6.1 = last version of Archey-OS-X. _Next version is “Archey X” (X compatible)_


### Changes since: v0.6.0
-	Misc cleaning, detabbing, and small fixes
-	Added 10.12 Sierra.
-   _Note: v0.6.1 was the last version that is OS X-only._


### Changes since: v0.5.0

-	New additions in wmDict. “Quartz” will be displayed as default, and any other will be picked up if installed.
-	Macports and Fink was added to Packages, ~~and 'pkgutil' for OS X programs (installer)~~. The combined number of all will be displayed.
-	New feat: Fancy Names. Displaying version names instead of build number _(with a fallback to buildnumber if not in dict)_.
-	Rewrote the Uptime class, using the built in timedelta to format the code.
-	Reduced the usage of Popen, and using the built in libraries instead (username, hostname etc).
-	Better output of RAM. Used/free sumup exactly as Activiy Monitor now (was a small diff before).



### Changes since: v0.4.0

-	Script is detecting “Darwin” with `uname -s`, not by checking if a file exists.
-	`logosDict` moved to the end, and to pick up value from variable (`distro`)
-	New class (`Utils`), to clean up the code.
-	Made to work with `python` and `python3`. Original script is using `python3` but standard version in OS X is `python` _(2.7)_ for those who doesn't have a newer one.
-	Removed som redundant code.
-	Added a simple option with  using `optparse`: `--version`
	_(incl the standard: `-h` and `--help`)_..
-	`brand` defaults to “None”. Self detecting. Only needed to use when changing color scheme.
-	Fixed an issue with decimals in RAM, which showed up when testing different versions of python. _(Used `math.trunc()`)_
-	With `archey.bash` gone, there's an xtra logo with the Apple to use. Default is the “Arch” logo.
-	`archey.{bash,s}` is removed and branched off to `bash-version`.
