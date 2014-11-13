# Each number indicates a positive or negative bonus
# Implemented as a dict object with multiple dicts for each race's bonus
# {<RACE>:{"str":<int>,"int":<int>,"dex":<int>,"per":<int>,"con":<int>,"wil":<int>,"cha":<int>}}

stats = {
  "human": {
    "str": 0,
    "int": 0,
    "dex": 0,
    "per": 0,
    "con": 0,
    "wil": 0,
    "cha": 0
  },
  "elf": {
    "str": 0,
    "int": 0,
    "dex": 2,
    "per": 0,
    "con": -2,
    "wil": 0,
    "cha": 0
  },
  "orc": {
    "str": 2,
    "int": -2,
    "dex": 0,
    "per": 0,
    "con": 2,
    "wil": 0,
    "cha": -2
  },
  "dwarf": {
    "str": 0,
    "int": 0,
    "dex": 0,
    "per": 0,
    "con": 2,
    "wil": 0,
    "cha": -2
  },
  "high elf": {
    "str": -1,
    "int": 0,
    "dex": 3,
    "per": 0,
    "con": -2,
    "wil": 0,
    "cha": 0
  },
  "half elf": {
    "str": 0,
    "int": 0,
    "dex": 1,
    "per": 0,
    "con": -1,
    "wil": 0,
    "cha": 0
  },
  "half orc": {
    "str": 2,
    "int": -2,
    "dex": 0,
    "per": 0,
    "con": 0,
    "wil": 0,
    "cha": -2
  },
  "halfling": {
    "str": -2,
    "int": 0,
    "dex": 2,
    "per": 0,
    "con": 0,
    "wil": 0,
    "cha": 0
  },
  "necron": {
    "str": 0,
    "int": 0,
    "dex": 0,
    "per": 0,
    "con": 0,
    "wil": 2,
    "cha": -2
  },
  "tyranid": {
    "str": 3,
    "int": 0,
    "dex": 0,
    "per": 0,
    "con": 3,
    "wil": -3,
    "cha": -3
  },
  "tau": {
    "str": -2,
    "int": 2,
    "dex": 2,
    "per": 0,
    "con": -2,
    "wil": 0,
    "cha": 0
  },
  "ratling": {
    "str": 1,
    "int": -1,
    "dex": 2,
    "per": 0,
    "con": 0,
    "wil": 0,
    "cha": -2
  },
  "cyborg": {
    "str": 1,
    "int": 2,
    "dex": -3,
    "per": 2,
    "con": 3,
    "wil": -3,
    "cha": 0
  },
  "cat": {
    "str": -1,
    "int": 0,
    "dex": 1,
    "per": 1,
    "con": -1,
    "wil": -1,
    "cha": 1
  }
}