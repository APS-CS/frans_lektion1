"""
File manager:
1. Visa alla filer i en katalog
2. kopiera alla filer i en katalog
3. flytta filer
"""

import argparse

def main():
    parser = argparse.ArgumentParser(description="File manager")

    parser.add_argument("-o", "--operation", choices=["list", "copy", "move"])








if __name__ == "__main__":
    main()

