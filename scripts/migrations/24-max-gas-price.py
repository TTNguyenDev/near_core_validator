"""
Add maximum gas price to avoid overflowing
"""

import sys
import os
import json
from collections import OrderedDict

home = sys.argv[1]
output_home = sys.argv[2]

config = json.load(open(os.path.join(home, 'output.json')),
                   object_pairs_hook=OrderedDict)

assert config['protocol_version'] == 23

config['protocol_version'] = 24
config['max_gas_price'] = str(10**22)

json.dump(config, open(os.path.join(output_home, 'output.json'), 'w'), indent=2)
