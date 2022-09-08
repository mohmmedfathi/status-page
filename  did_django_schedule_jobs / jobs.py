
import schedule
import time 


url = 'https://www.google.com/'
c = 0

def do_anything():
    
    try:    
        print('request number ' + str(c))
        
        response = requests.get(url,timeout=3) 

        response.raise_for_status()                 # Raise error in case of failure 

    except requests.exceptions.HTTPError as httpErr: 

        print ("Http Error:",httpErr) 

    except requests.exceptions.ConnectionError as connErr: 

        print ("Error Connecting:",connErr) 

    except requests.exceptions.Timeout as timeOutErr: 

        print ("Timeout Error:",timeOutErr) 

    except requests.exceptions.RequestException as reqErr: 

        print ("Something Else:",reqErr) 
    
    
    
    print(response.status_code)
"""

schedule.every(1).seconds.do(do_anything)

while 1:
    schedule.run_pending()
    time.sleep(1)
    c+=1
"""