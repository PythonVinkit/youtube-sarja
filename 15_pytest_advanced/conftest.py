import sys
import os
from pathlib import Path
root_dir = str(Path(__file__).parent.absolute())
print("Set working path to:", root_dir)
os.chdir(root_dir)
