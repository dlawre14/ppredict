#entry point for all protein programs

import argparse

#Function here

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Protein function predictor')
  parser.add_argument('-v', '--visual', action='store_true', help='display visual network with kivy')

  args = parser.parse_args()
