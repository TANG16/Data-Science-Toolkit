# import the modules we'll need
from IPython.display import HTML
import base64

# function that takes in a dataframe and creates a text link to  
# download it (will only work for files < 2MB or so)
def create_download_link(df, title = "Download CSV file", filename = "data.csv"):  
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode())
    payload = b64.decode()
    html = '<a download="{filename}" href="data:text/csv;base64,{payload}" target="_blank">{title}</a>'
    html = html.format(payload=payload,title=title,filename=filename)
    return HTML(html)

# FuzzyWuzzy is a library of Python which is used for string matching
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process


fuzz.ratio('geeksforgeeks', 'geeksgeeks') 
87

# Exact match 
fuzz.ratio('GeeksforGeeks', 'GeeksforGeeks')   

100
fuzz.ratio('geeks for geeks', 'Geeks For Geeks ')  
80


fuzz.partial_ratio("geeks for geeks", "geeks for geeks!") 
100
# Exclamation mark in second string,  
# but still partially words are same so score comes 100

fuzz.partial_ratio("geeks for geeks", "geeks geeks") 
64
# score is less because there is a extra  
# token in the middle middle of the strin


#Winden the display as default
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))


def reverse_number(n):
    rev = 0
    
    while(n > 0): 
        a = n % 10
        rev = rev * 10 + a 
        n = n // 10      
    print(rev) 




def apache_line_parser(path):
  """Read log data and return DataFrame with log history"""
  import glob2
  import apache_log_parser

  path = glob2.glob(path) # Get the path you want to parse through
  print(path)
  # Argument of make_parser is arbitrary. You get them from apache
  line_parser = apache_log_parser.make_parser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")
  parsed=[]
  for path_n in path: # Go through each file in a path 
    print(path_n)
    with open(path_n) as lg:
      line_list = lg.readlines()# Read log file 
    for line in line_list: # Parse through log file and append it to parsed
      parsed.append(line_parser(line))
    
  df = pd.DataFrame(parsed) # Make DataFrame of parsed log data
  return df