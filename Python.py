# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 14:22:35 2019 
@author: jessi
"""
#TextFrequenct class to ..
class TextFrequency:
   
    #constructor for class TextFrequency
    def __init__(self,file_name):
        #instance variables file_name and text
        #create empty list for text
        self.text = []
        self.file_name = file_name
        #call method getText so text load when object is instantiated
        self.getText()
         
    #method to read, open and close file     
    def getText(self):
        file = open(self.file_name,'r')
        self.text = file.read()
        file.close()
        
    #Method to count number of times a word has occured     
    def wordFreq(self):
        freq = {}#create dictionary
        words = self.text.split()#split string
        for word in words:#iterate over word text 
                if word in freq:
                    freq[word] += 1
                else:
                    freq[word] = 1
        return freq
                    
    #Method to count number of time a letter has occured
    def letterFreq(self):
        freq = {}#create dictionary
        letters = self.text.split()#split string
        for line in letters:#iterate over letter in text 
            for letter in line:
                if letter in freq:#add 1 to the letter count 
                    freq[letter] +=1
                else:
                    freq[letter] = 1
        return freq
   #Method which returns 
    def toLower(self):
        self.text = self.text.lower()
        print(self.text)
               
        
 #pass file to the init function 
myTextFrequecny = TextFrequency('newlyrics.txt')
#-----new test test the to lower method with text frequency class methods
myTextFrequecny.toLower()
#--------Suggested test 1    
letterFreq = myTextFrequecny.letterFreq()
for letter in letterFreq:
    print(letter, letterFreq[letter])
#--------Sugested test 2 
wordFreq = myTextFrequecny.wordFreq()
for word in wordFreq:
    print(word,wordFreq[word])
    
#Histogram class to inherit from TextFrequency 
class HistogramPrinter(TextFrequency):
    def __init__(self,file_name):
        TextFrequency.__init__(self,file_name)
    
    
    def printLetterHist(self):
        #call letterfreq method assign to freq
        freq = TextFrequency.letterFreq(self)
        #loop through all items in the dictionary
        for item in freq:
            freq[item] = '*'*freq[item]#reaplce letter count with aterisk
            print(item,freq[item])
             
      
    def printwordHist(self):
         #create a new instance of class letterFreq store in freq
        freq = TextFrequency.wordFreq(self)
        for items in freq:#replace word count with aterisk 
            freq[items]='*'*freq[items] 
            print(items,freq[items])
    
   
#----Suggested test  2 and 3   
#create a new instance of class    
myHistogram = HistogramPrinter('newlyrics.txt')
#assign to new varible
myHistogram.toLower() 
myHistogram.printLetterHist()
myHistogram.printwordHist()    


        
        
        