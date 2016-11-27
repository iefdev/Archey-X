![][masterBadge] [![GitHub release][latestBadge]][latest]


# Archey X

Archey X is a simple tool to display system information.

- - -

This is a forked/ported version of the original script: [Archey][dja], by [djmelek][djm] - made to be X compatible with both OS X and misc GNU/Linux distributions - hence the name: Archey **X**. _(Previously an OS X port of Archey.)_ […»][about]


### Screenshots

v0.7.0-beta on OS X. (Terminal theme: [myTerm][myterm].)

![][scrap]


v0.X-beta _(early version)_ of Fedora and Debian in Vagrant boxes.

![][x2]

_A few more Screenshots can be found in the [Wiki …»][scraps]._


## Installation

Copy the file to `/usr/local/bin`, and give it permission to execute.

	sudo install -m 0755 archeyX /usr/local/bin

_(make sure `/usr/local/bin` is in your `PATH`)_


## Usage

    archeyX

To load at start. Add to your `.bashrc` _(or `.bash_profile`)_:

```bash
# Load archey (if installed)
[[ `type archeyX 2> /dev/null` && $UID != 0 ]] && archeyX
```

**Note:** When using `scp` over the network and logging into a machine with `archeyX` loading up... It _might_ cause an error about output. To avoid that issue, use this instead:

```bash
# Load archey (if installed)
# If not running interactively, don't do anything
[[ -n "$PS1" && `type archeyX 2> /dev/null` && $UID != 0 ]] && archeyX
```


## Settings and Colors

See [Settings and Colors][prefs] in the Wiki


## Python 3

“Archey X” is written and tested with `pylint (1.6.4)`, with `python3 (3.5.2)`. If you don't have Python 3.* —  you _(really)_ should upgrade. But, there is a _work-around_ in the [FAQ][py2].


## Tested distros

- [ ] Arch Linux
- [x] Darwin/OS X
- [x] Debian Jessie 8.3 (“may” work with other, like Mint, *buntu. `dpkg`)
- [x] Fedora 23 (“may” work with CentOS and Red Hat. `dnf|yum`)

_Please, report working distributions [here][iss1]._

## Credits and copright

See [Credits][credits] in the Wiki


## Contributing

1. Fork it (<https://github.com/iEFdev/Archey-X/fork>)
2. Create your feature branch (`git checkout -b feature/foo-bar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/foo-bar`)
5. Create a new Pull Request


## Author notes

-	**[2016-11-23]** This repo has been renamed from: “Archey :: OS X” -> “Archey X”, since it will be X-compatible. Initial version(s) will be `v0.7.0-YYYYMMDD-beta` until it's been tested/verified more to work with _N_ distributions.

If you have any feedback, suggestions? Please, send an email or a tweet.

· Eric

<!-- Markdown: Links & Images -->
[masterBadge]: https://img.shields.io/badge/master-v0.7.0--beta-778899.svg?style=plastic
[latestBadge]: https://img.shields.io/github/release/iEFdev/Archey-X.svg?style=plastic
[latest]: https://github.com/iEFdev/Archey-X/releases/latest "Latest release"
[super]: https://github.com/iEFdev/Archey-X/blob/master/archeyX#L303
[dja]: https://github.com/djmelik/archey "Archey"
[djm]: https://github.com/djmelik "Melik Manukyan"
[scrap]: https://raw.githubusercontent.com/iEFdev/Archey-X/master/screenshot.png "Screenshot of Archey X"
[scraps]: https://github.com/iEFdev/Archey-X/wiki/Screenshots "More Screenshots"
[x2]: https://github.com/iEFdev/Archey-X/wiki/_Images/screenshot_x2.png "Screenshot(s) of Archey X"
[myterm]: https://github.com/iEFdev/dotfiles/tree/master/myTerm "My Terminal theme"
[jy]: https://github.com/iEFdev/junkyard "iEFdev/Junkyard"
[py2]: https://github.com/iEFdev/Archey-X/wiki/FAQ#q-can-i-use-python-2 "Python 2 :: FAQ"
[about]: https://github.com/iEFdev/Archey-X/wiki/About "About Archey X"
[credits]: https://github.com/iEFdev/Archey-X/wiki/Credits "Credits and copyright"
[prefs]: https://github.com/iEFdev/Archey-X/wiki/Settings-and-Colors "Settings and Colors"
[iss1]: https://github.com/iEFdev/Archey-X/issues/1#issue-191799189 "Verify distributions"
