# Archey X

> Archey X is a simple tool to display system information.

[![][masterBadge]][master] [![GitLab release][latestBadge]][latest]

![][pythonVersion]


This is a forked and ported version of the original script: [Archey][dja], by [djmelek][djm] - made to be X compatible with both OS X/macOS and misc GNU/Linux distributions – hence the name: Archey **X**.


### Demo and Screenshots

Here's a small demo you can watch at [Vimeo][vimeo].

[![][vimeo_poster]][vimeo]

- - -

v0.7.0-beta on OS X.

![][scrap]

- - -

v0.X-beta _(early version)_ of Fedora and Debian in Vagrant boxes.

![][x2]

_A few more Screenshots can be found in the [Wiki …»][scraps]._


## Installation

```bash
sudo install -v -m 0755 -o 0 -g 0 archeyX /usr/local/bin
```

_(make sure `/usr/local/bin` is in your `PATH`)_


## Usage

```bash
archeyX
```

#### Auto-load

To load at start. Add to your `.bashrc` _(or `.bash_profile`)_:

```bash
# Load archeyX (if installed)
[[ $(type archeyX 2> /dev/null) && ${UID} != 0 ]] && archeyX
```

#### Only in interactive mode

If you have installed `archeyX` on a remote server, with an SSH key based setup. Transfering files to the remote with `scp` for example, will cause some errors. You can use `$-` to check for that:

```bash
# Load archeyX (if installed)
# If not running interactively, don't do anything
if [[ $- == *i*  && ${UID} != 0 ]]; then
    [[ $(type archeyX 2> /dev/null) ]] && archeyX
fi
```

## Settings and Colors

See [Settings and Colors][prefs] in the Wiki


## Tested distros

- [x] Arch Linux
- [x] Rocky Linux: 8.7, 8.8 (desktop)
- [x] CentOS: 7.6.1810 (server)
- [x] Debian: 8.3 (server), 10.4 (MATE, Xfce)
- [x] Fedora: 23 (Cinnamon)
- [x] OS X/macOS: 10.7.5

_Please, report working distributions [here][iss1]._


## License, credits and copyright

![][licenseBadge]

Get version and copyright with:

```bash
# Example
$ archeyX -V
archeyX: v0.9.0, Copyright (c) 2020 Eric F

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
more details.

You should have received a copy of the GNU General Public License along
with this program. If not, see <https://www.gnu.org/licenses/gpl-3.0.txt/>.
```

For the original author(s) and copyright, se [Archey][dja], by [djmelek][djm].


## Contributing

1. Fork it (<https://gitlab.com/iefdev/Archey-X/forks/new>)
2. Create your feature branch (`git switch -c feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Merge Request


## Author notes

-   **[2017-04-30]** From now, Arxhey X is using Python 3.6+. The “shebang” is changed, and there's a `f'{}'` to trigger an error with a msg to ask you to upgrade if you don't have 3.6. So, please upgrade if needed. Thanks!
-   **[2016-11-23]** This repo has been renamed from: “Archey :: OS X” -> “Archey X”, since it will be X-compatible. Initial version(s) will be `v0.7.0-YYYYMMDD-beta` until it's been tested/verified more to work with _N_ distributions.

**Pylint**

-   **[2020-07-24]** 9.83/10 (pylint 2.5.3, Python 3.8.3).
-   **[2020-06-27]** 9.79/10 (pylint 2.5.3, Python 3.8.3).
-   **[2019-10-02]** 9.96/10 (pylint 2.3.1, Python 3.7.4).
-   **[2019-09-28]** 9.79/10 (pylint 2.3.1, Python 3.7.4).
-   **[2017-05-01]** 9.96/10 (pylint 1.7.1, Python 3.6.1).

- - -

 

If you have any feedback, suggestions? Please, use the Issues, Merge Requests, send an email or a post me on X.

· Eric ([@iefdev][x])

<!-- Markdown: link & image dfn's -->
[pythonVersion]: https://img.shields.io/badge/python->%3D_3.6-FFD343.svg?logo=python&logoColor=FFD343&labelColor=3D75AD&style=plastic
[licenseBadge]: https://img.shields.io/badge/license-GPL--3.0--or--later-C00?style=plastic
[masterBadge]: https://img.shields.io/badge/master-v0.99-778899.svg?logo=gitlab&style=plastic
[latestBadge]: https://img.shields.io/badge/latest-v0.9.0-blue.svg?logo=gitlab&style=plastic
[latest]: https://gitlab.com/iefdev/Archey-X/tags/ "Tags"
[master]: https://gitlab.com/iefdev/Archey-X/ "Master"
[dja]: https://github.com/djmelik/archey "Archey"
[djm]: https://github.com/djmelik "Melik Manukyan"
[vimeo]: https://vimeo.com/217440806 "Archey X (demo)"
[vimeo_poster]: https://gitlab.com/iefdev/Archey-X/raw/main/images/vimeo_poster.png "Archey X (demo)"
[scrap]: https://gitlab.com/iefdev/Archey-X/raw/main/images/screenshot.png "Screenshot of Archey X"
[scraps]: https://gitlab.com/iefdev/Archey-X/wikis/Screenshots "More Screenshots"
[x2]: https://gitlab.com/iefdev/Archey-X/wikis/_Images/screenshot_x2.png "Screenshot(s) of Archey X"
[myterm]: https://gitlab.com/iefdev/myTerm "My Terminal theme"
[about]: https://gitlab.com/iefdev/Archey-X/wikis/About "About Archey X"
[credits]: https://gitlab.com/iefdev/Archey-X/wikis/Credits "Credits and copyright"
[prefs]: https://gitlab.com/iefdev/Archey-X/wikis/Settings-and-Colors "Settings and Colors"
[iss1]: https://gitlab.com/iefdev/Archey-X/issues/1 "#1 - Verify distributions"
[x]: https://twitter.com/iefdev
