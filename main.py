import pathlib
import os

for pdp_file in pathlib.Path('./data/__groupfolders/1/').glob('**/*.pdp'):
    print(pdp_file)
