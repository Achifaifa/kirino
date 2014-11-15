# Each number indicates a positive or negative bonus
# Implemented as a dict object with multiple dicts for each race's bonus
# {<RACE>:{"str":<INT>,"INT":<INT>,"DEX":<INT>,"PER":<INT>,"CON":<INT>,"WIL":<INT>,"CHA":<INT>}}

stats = {
  "human": {
    "STR": 0,
    "INT": 0,
    "DEX": 0,
    "PER": 0,
    "CON": 0,
    "WIL": 0,
    "CHA": 0
  },
  "elf": {
    "STR": 0,
    "INT": 0,
    "DEX": 2,
    "PER": 0,
    "CON": -2,
    "WIL": 0,
    "CHA": 0
  },
  "orc": {
    "STR": 2,
    "INT": -2,
    "DEX": 0,
    "PER": 0,
    "CON": 2,
    "WIL": 0,
    "CHA": -2
  },
  "dwarf": {
    "STR": 0,
    "INT": 0,
    "DEX": 0,
    "PER": 0,
    "CON": 2,
    "WIL": 0,
    "CHA": -2
  },
  "high elf": {
    "STR": -1,
    "INT": 0,
    "DEX": 3,
    "PER": 0,
    "CON": -2,
    "WIL": 0,
    "CHA": 0
  },
  "half elf": {
    "STR": 0,
    "INT": 0,
    "DEX": 1,
    "PER": 0,
    "CON": -1,
    "WIL": 0,
    "CHA": 0
  },
  "half orc": {
    "STR": 2,
    "INT": -2,
    "DEX": 0,
    "PER": 0,
    "CON": 0,
    "WIL": 0,
    "CHA": -2
  },
  "halfling": {
    "STR": -2,
    "INT": 0,
    "DEX": 2,
    "PER": 0,
    "CON": 0,
    "WIL": 0,
    "CHA": 0
  },
  "necron": {
    "STR": 0,
    "INT": 0,
    "DEX": 0,
    "PER": 0,
    "CON": 0,
    "WIL": 2,
    "CHA": -2
  },
  "tyranid": {
    "STR": 3,
    "INT": 0,
    "DEX": 0,
    "PER": 0,
    "CON": 3,
    "WIL": -3,
    "CHA": -3
  },
  "tau": {
    "STR": -2,
    "INT": 2,
    "DEX": 2,
    "PER": 0,
    "CON": -2,
    "WIL": 0,
    "CHA": 0
  },
  "ratling": {
    "STR": 1,
    "INT": -1,
    "DEX": 2,
    "PER": 0,
    "CON": 0,
    "WIL": 0,
    "CHA": -2
  },
  "cyborg": {
    "STR": 1,
    "INT": 2,
    "DEX": -3,
    "PER": 2,
    "CON": 3,
    "WIL": -3,
    "CHA": 0
  },
  "cat": {
    "STR": -1,
    "INT": 0,
    "DEX": 1,
    "PER": 1,
    "CON": -1,
    "WIL": -1,
    "CHA": 1
  }
}