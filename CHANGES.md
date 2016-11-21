# Changes

Changes that have been made between the versions.

- - -

> **Latest version:** v0.6.1 _(Last version before merging `neXtgen`)_


### Changes since: v0.6.0
-	Misc cleaning, detabbing, and small fixes
-	Added 10.12 Sierra.


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
