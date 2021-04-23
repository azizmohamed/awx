#!/usr/bin/env python

import six
import json
import argparse
from collections import defaultdict

def main():
    parser = argparse.ArgumentParser()
   
    args = parser.parse_args()
   
    if args.list:
        print({
            "dyngroup":{
                "hosts":[
                    "cloud1.cloud.example.com",
                    "cloud2.cloud.example.com"
                ],
                "vars":{}
            },
            "_meta":{
                "hostvars":{
                    "cloud1.cloud.example.com":{
                        "type":"web"
                    },
                    "cloud2.cloud.example.com":{
                        "type":"database"
                    }
                }
            }
        })
    else:
        print({"_meta": {"hostvars": {}}})


if __name__ == '__main__':
    main()