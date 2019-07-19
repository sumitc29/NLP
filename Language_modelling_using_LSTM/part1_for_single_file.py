################  DATA EXTRACTION #####################
############### part 1 of  Phrase prediction Algo #####
#Action : this is used to extract data from the xml file and save combines data it into simple text file 
#Input:  .xml files
#outut: simple text file
#
#Author: sumit chandak  (chandaksumit29@gmail.com)
#Date: 1/12/2018
#
##########################################################

import glob
import fileinput
import pandas as pd


def remove_error(filename):
    with fileinput.FileInput(filename, inplace=True) as file:
            for line in file:
                print(line.replace('"id=','id="' ), end='')
                
                
def remove_empty_lines(filename):
    """Overwrite the file, removing empty lines and lines that contain only whitespace."""
    with open(filename, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.writelines(line for line in lines if line.strip())
        f.truncate()
                
                

        
        
##########################################################################


filename='C:/F/task/fulltext/06_3.xml'

remove_error(filename)

sentencedf=pd.DataFrame(columns=['id','text'])
catchphrasedf=pd.DataFrame(columns=['id','text'])




from xml.dom import minidom
xmldoc = minidom.parse(filename)

name = xmldoc.getElementsByTagName("name")[0]
print(name.firstChild.data)



catchphraselist = xmldoc.getElementsByTagName('catchphrase') 
for s in catchphraselist :
    #print ("Attribute id : ", s.attributes['id'].value)
    #print ("Text : ", s.firstChild.nodeValue)
    attribute=s.attributes['id'].value
    data=s.firstChild.nodeValue
    catchphrasedf = catchphrasedf.append({'id':attribute, 'text':data}, ignore_index=True)
    


sentencelist = xmldoc.getElementsByTagName('sentence') 
for s in sentencelist :
    #print ("Attribute id : ", s.attributes['id'].value)
    #print ("Text : ", s.firstChild.nodeValue)
    attribute=s.attributes['id'].value
    data=s.firstChild.nodeValue
    sentencedf = sentencedf.append({'id':attribute, 'text':data}, ignore_index=True)

##################################################################
    
datadf=pd.concat([sentencedf, catchphrasedf])
datadf['text'].to_csv('inter_1.txt',sep=' ',header=False, index=False)

remove_empty_lines('inter_1.txt')


























        
        
        
        
        
        