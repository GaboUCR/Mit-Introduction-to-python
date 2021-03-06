# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory

class NewsStory (object):
    def __init__(self, guid, title, description, link, pubdate): 
        self.guid = guid
        self.title = title    
        self.description = description
        self.link = link 
        self.pubdate = pubdate
        
    def get_guid(self):
        new_guid = self.guid
        return new_guid
    
    def get_title(self):
        new_title = self.title
        return new_title    
    
    def get_description(self):
        new_description = self.description
        return new_description
    
    def get_link(self):
        new_link = self.link
        return new_link
    
    def get_pubdate(self):
        new_pubdate = self.pubdate
        return new_pubdate
    

#======================
# Triggers
#======================

    

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS
class PhraseTrigger (Trigger):
    def __init__(self, phrase):
        self.phrase = phrase
        
    def get_phrase (self):
        new_phrase = self.phrase
        return new_phrase
    
    def is_phrase_in (self,text):
         text = text.lower()
         phrase = self.get_phrase().lower() 
         
         ## take symbols out
         for symbols in string.punctuation:
             
             text = text.replace(symbols," ")
         
         text_list = text.split(" ")
         for elem in range(len(text_list)):
             try:
                 text_list.remove("")
             except:
                    break
                
        
         phrase_list = phrase.split(" ")
                 
         for N_text in range(len(text_list)) :
             try:                             
                 
                 
                 if phrase_list[0] == text_list[N_text]:
                     
                     for N_phrase in range(len(phrase_list)):
                         if phrase_list[N_phrase] != text_list[N_text + N_phrase] :
                             
                             break
                         
                         if N_phrase == len(phrase_list) - 1 :
                             return True
                            
             except :
                 return False                         
         
         return False
        

class TitleTrigger (PhraseTrigger) :
    def __init__(self,phrase):
        PhraseTrigger.__init__(self,phrase)
            
    def evaluate (self, story):
        
        return self.is_phrase_in(story.get_title())        
        
        
class DescriptionTrigger (PhraseTrigger) :
    def __init__(self,phrase):
        PhraseTrigger.__init__(self,phrase)
            
    def evaluate (self, story):
        
        return self.is_phrase_in(story.get_description())                
        
        
        
class TimeTrigger (Trigger):
    def __init__(self, date):
        self.dateTime = datetime.strptime(date, "%d %b %Y %H:%M:%S")           
            
    def get_date(self):
        new_date = self.dateTime
        return new_date
    


class BeforeTrigger (TimeTrigger):
    def __init__(self,date):
        TimeTrigger.__init__(self,date)        
        
            
    def evaluate(self, story):
        
        return self.get_date() > datetime.strptime(story.get_pubdate(), "%d %b %Y %H:%M:%S")             



class AfterTrigger (TimeTrigger):
    def __init__(self,date):
        TimeTrigger.__init__(self,date)        
        
            
    def evaluate(self, story):
        
        return self.get_date() < datetime.strptime(story.get_pubdate(), "%d %b %Y %H:%M:%S") 

        

class NotTrigger(Trigger):
    def __init__ (self, trigger,story):
        self.news_boolean = trigger.evaluate(story)
              
    
    def evaluate(self):
        
        return not self.news_boolean
        
         

class AndTrigger(Trigger):
    def __init__ (self, trigger1,trigger2 ,story):
        self.news_boolean = trigger1.evaluate(story) and trigger2.evaluate(story)
              
    
    def evaluate(self):
        
        return self.news_boolean        


class OrTrigger(Trigger):
    def __init__ (self, trigger1,trigger2 ,story):
        self.news_boolean = trigger1.evaluate(story) or trigger2.evaluate(story)
              
    
    def evaluate(self):
        
        return self.news_boolean     


def filter_stories (stories,TriggerList):
    good_news = []
    for news in stories:
        for trigger in TriggerList:
            if (trigger.evaluate(news)):
                good_news.append(news)
        
    return good_news    




    
    
    
# gatito = NewsStory ("guid" ,"title", "description", "link", "25 dec 1998 12:20:33")

# perrito = AfterTrigger("25 dec 1998 12:20:34")


# perico = NotTrigger(perrito,gatito) 

# print(perico.evaluate())



# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

# Problem 6
# TODO: BeforeTrigger and AfterTrigger


# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger

# Problem 8
# TODO: AndTrigger

# Problem 9
# TODO: OrTrigger


#======================
# Filtering
#======================

# Problem 10



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    # triggers_list = []
    
    # for line in lines:
        

            
    print(lines) # for now, print it so you see what it contains!

read_trigger_config(filename)

SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        # triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


# if __name__ == '__main__':
#     root = Tk()
#     root.title("Some RSS parser")
#     t = threading.Thread(target=main_thread, args=(root,))
#     t.start()
#     root.mainloop()

