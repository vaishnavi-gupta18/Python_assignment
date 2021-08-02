import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import login
import database as db
import time

def user_check(func):
    def inner(username):
        data = db.get_whole_data()
        for x in data:
          if username in x:
            data2 = db.get_data(username)
            for y in data2:
                if y[1] is not None :
                    if y[2] is not None :
                        a = json.loads(y[2])
                        Person(y[1],a,y[3]).show()
                        break
                    else:
                        Person(y[1],[],y[3]).show()
                        break
                   
                else :
                    return func(username)
                    break
            break
        raise ValueError('User does not exist')  
        return 
    return inner


class Person:

  def __init__(self,name,work = [],city = "Roorkee"):
    self.name=name
    self.city=city
    if len(work) != 0:
      self.work = []
      self.work=work

  def show(self):
    print("My name is {0} and my current city is {1}".format(self.name,self.city))
    a = "I work at "
    if len(self.work) == 1:
      a+=self.work[0]
    else:
      for i in range(len(self.work)):
        if(i == (len(self.work)-1)):
          a+=" and "+self.work[i]
        else:
          a+=self.work[i]+", "
    print(a)
  
  def add_data(self,username):
    db.add_data(self.name, self.work, self.city, username)  

@user_check
def scrap(username):
  URL = "https://m.facebook.com/{}".format(username)
  r = requests.get(URL)
  soup = BeautifulSoup(r.content, 'html5lib')
  global per,flag,info,checked_users
  name = soup.find('div', attrs = {'id':'cover-name-root'}).h3.text.strip()
  try:
    table=[]
    table = soup.findAll('table')
    city=table[5].a.text.strip()
  except:
    city=""
  
  try:
    cont=[]
    cont = soup.findAll('div', attrs = {'class':'cj ck'})
    wo=[]
    work=[]
    wo=cont[1].findAll('a')
    for i in range(len(wo)):
      if i%2 !=0:
        work.append(wo[i].text.strip())
  except:
    work=[]
  
  
  if len(city) !=0 :
    if len(work)!=0:
      per = Person(name,work,city)
    else:
      per = Person(name,[],city)
  else:
    if len(work)!=0:
      per = Person(name,work)
    else:
      per = Person(name)
  per.add_data(username)
  per.show()

  driver = webdriver.Chrome()
  driver.get("https://m.facebook.com")
  uname = driver.find_element_by_id("m_login_email")
  passwrd = driver.find_element_by_id("m_login_password")
  submit = driver.find_element_by_name("login")

  uname.send_keys(login.username)
  passwrd.send_keys(login.password)

  submit.click()
  time.sleep(3)
  driver.get("https://m.facebook.com/checkpoint/?__req=b")
  login_app = driver.find_element_by_id("checkpointSubmitButton-actual-button")
  login_app.click()
  time.sleep(5)
  driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/form/div/article/section/div/fieldset/label[3]/div/div[2]/div').click()
  driver.find_element_by_id("checkpointSubmitButton-actual-button").click()
  time.sleep(5)
  driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/form/div/article/section/div/div[2]/div/div[1]/div[2]/fieldset/label[18]/div/div[1]').click()
  time.sleep(1)
  driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/form/div/article/section/div/div[2]/div/div[2]/div[2]/fieldset/label[9]/div/div[1]').click()
  time.sleep(1)
  driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/form/div/article/section/div/div[2]/div/div[3]/div[2]/fieldset/label[7]/div/div[1]').click()
  time.sleep(1)
  driver.find_element_by_id("checkpointSubmitButton-actual-button").click()
  time.sleep(5)
  driver.find_element_by_id("checkpointSubmitButton-actual-button").click()
  time.sleep(5)

  driver.get("https://m.facebook.com/"+username+"/about?")
  time.sleep(3)
  SCROLL_PAUSE_TIME = 5

  last_height = driver.execute_script("return document.body.scrollHeight")

  while True:
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

      time.sleep(SCROLL_PAUSE_TIME)

      new_height = driver.execute_script("return document.body.scrollHeight")
      if new_height == last_height:
          break
      last_height = new_height

  time.sleep(3)
  fav = []
  driver.find_element(By.XPATH, "//div[contains(text(),'Likes')]/../../../../div[1]/div/div")
  for span in driver.find_elements(By.XPATH, "//div[contains(text(),'Likes')]/../../../../div[1]/div/div/div[*]/div[1]/span"):
      fav.append(span.text)

  a = "My favourites include "
  if len(fav) == 1:
      a+=fav[0]
  else:
      for i in range(len(fav)):
          if(i == (len(fav)-1)):
              a+=" and "+fav[i]
          else:
              a+=fav[i]+", "
  print(a)

scrap('utkarsh.parkhi.1')



  
