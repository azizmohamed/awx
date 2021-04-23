#!/usr/bin/env python

def main():
    return {
  "development": {
    "hosts": [
      "prometheus",
      "rotarran"
    ],
    "vars": {}
  },
  "production": {
    "hosts": [
      "talvath",
      "defiant"
    ],
    "vars": {}
  },
  "_meta": {
    "hostvars": {
      "defiant": {},
      "rotarran": {},
      "prometheus": {}, 
      "talvath": {}
    }
  }
}


if __name__ == '__main__':
    main()