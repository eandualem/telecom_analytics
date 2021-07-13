import pandas as pd

def __init__(self):
  pass

class DfCleaner():
  
  def __init__(self):
    pass

  def fixLabel(self, label):
    label = label.split('(', 1)[0]
    label = label.strip()
    label = label.replace(' ', '_').replace('.', '').replace('/', '_')
    return label.lower()


