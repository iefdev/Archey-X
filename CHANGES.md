# Changes

Changes that have been made between the versions.

- - -

> **Latest version:** v0.5.0



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
