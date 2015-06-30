#!/usr/bin/python

import sys
import json
import os

def main():
  module = AnsibleModule(
      argument_spec = dict(
          package = dict(required=True),
          host    = dict(required=False),
          port    = dict(required=False),
          domain  = dict(required=False)
      )
  )

  package = os.path.expanduser(module.params['package'])


if __name__ == '__main__':
  main()

