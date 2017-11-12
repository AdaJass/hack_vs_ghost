from pyquery import PyQuery as pq
from ghost import Ghost, Session

def aa(r=0):
    return False

gh=Ghost() 
ran_str2 = 'User-Agent,Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;' #.join(random.sample(string.ascii_letters + string.digits, 8)) 
se=Session(gh,user_agent=ran_str2,display=True) 

se.open('http://192.168.1.1/',user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535....TML, like Gecko) Chrome/15.0.874.121 Safari/535.2')
se.wait_for_page_loaded(10)
se.sleep(10)
# d=pq(se.content)
# print(d('input#lgPwd').attr('value')) 
while True:    
    se.sleep(600)
    se.click('#disconnect',btn=0)
    se.sleep(3)
    se.click('#save',btn=0)
    se.sleep(20)



if __name__ == '__main__':     
    pass