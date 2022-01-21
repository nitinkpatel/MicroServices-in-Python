from javax.swing import JOptionPane

def forString(question):
  return JOptionPane.showInputDialog(question)


def forInt(question):
  return int(forString(question));


def forDouble(question):
  return float(forString(question))
  

def forFloat(question):
  return float(forString(question))
  
  
def forBoolean(question):
  input = forString(question)
  return "y"==input.lower() or "true"==input.lower() or "yes"==input.lower()
