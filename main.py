#!/usr/bin/env python3

import sys
sys.path.insert(0,"test_submodule")
from test_submodule import submodule

def main():
    print("this is from the main project")
    submodule()
    return 0

if __name__ == "__main__":
    main()