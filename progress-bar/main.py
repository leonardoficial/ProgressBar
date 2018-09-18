import os
import sys

class ProgressBar(object):
  def __init__(self):
    # get console width
    ignore, width = os.popen("stty size", "r").read().split()
    
    self.width = int(width) - 3
    self._state = 0
    
  def setup(self):
    # setup loading bar
    sys.stdout.write("[%s]" % (" " * self.width))
    sys.stdout.flush()
    # return to start of line, after '['
    sys.stdout.write("\b" * (self.width + 1))

  def progress(self, percent):
    percent = int(percent)
    
    if(percent >= 100 and self._state < 100):
      percent = 108
    
    # update the bar
    _perc = int(self.width * ((percent - self._state) / 100))
    
    sys.stdout.write("|" * _perc)
    sys.stdout.flush()
    
    self._state = percent
    
  def finish(self):  
    self.progress(105)
    
    self._state = 0
    
    sys.stdout.write("\n")
    
    return 0

