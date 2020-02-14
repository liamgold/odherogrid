# ODHeroGrid
![logo](logo.png)

Small script that generates a custom Dota 2 Hero Grid layout of heroes sorted 
by winrate in public or professional games, using stats from OpenDota.


# Installation
```
pip install odherogrid
```


# Usage
```
Usage:
  odhg [OPTIONS]

Options:
  [-b, --brackets] BRACKET (default: 7)
    Which skill bracket to get winrates from.
      <1, herald, h>                          Herald
      <2, guardian, g>                        Guardian
      <3, crusader, c>                        Crusader
      <4, archon, a>                          Archon
      <5, legend, l>                          Legend
      <6, ancient, n>                         Ancient
      <7, divine, d>                          Divine
      <8, pro, p>                             Pro
      <0, all, A>                             All
    Hero grids for multiple brackets can be generated by specifying the -b option several times.

  [-l, --layout] LAYOUT (default: 1)
    Which Hero Grid layout to use.
      <1, mainstat, m>                        Mainstat
      <2, attack, a>                          Attack
      <3, role, r>                            Role
      <0, single, s>                          Single

  [-p, --path] PATH
    Specify absolute path of Dota 2 userdata/cfg directory.
    (It's usually better to run --setup to configure this path.)

  [-s, --sort] (flag)
    Sort heroes by winrate in ascending order. (Default: descending).

  [-S, --setup] (flag)
    Runs first-time setup in order to create a persistent config.

  [-n, --name] NAME
    Sort heroes by winrate in an existing custom hero grid. This option is ONLY for sorting hand-made grids. Grids generated by ODHG do not require this option.

  [-h, --help] (flag)
    Show this message and exit.

  [-q, --quiet] (flag)
    Suppress all terminal output except errors.

```
## Using standard configuration 
```
odhg
```
Prompts to create config file in `~/.odhg/` the first time the program runs.

This is the recommended way to run ODHG.

# Command-line options
Command-line options can be supplied to override config settings.


## Bracket


#### Create grid for Herald hero winrates:
```
odhg --brackets 1
```


#### Bracket names can also be used:
```
odhg --brackets herald
```


#### Shorter:
```
odhg -b h
```


#
#### Create grids for Herald, Divine & Pro winrates:
```
odhg -b 1 -b 7 -b 8
```

#### Alternatively:
```
odhg -b h -b d -b p
```


#
#### Create grids for all brackets:
```
odhg -b 0
```


## Layout
#### Use role layout (Carry/Support/Flex). 
```
odhg --layout role
```

#### Single category layout
```
odhg --layout single
```


## Path
#### Specify a specific Steam user CFG directory:
```
odhg --path /home/bob/Steam/userdata/420666/570/remote/cfg
```


## Name
#### Sort custom grids with `--name`
```
odhg --name MyCustomGrid -b 7
```
#### Before:
![Before](screenshots/custom_presort.png)
#### After:
![After](screenshots/custom_postsort.png)

# Screenshots

![Divine Winrates](screenshots/screenshot.png)
_Divine winrate hero grid generated 2020-02-14_
