################  DATA EXTRACTION #####################
############### part 1 of  Phrase prediction Algo #####
#Action : this is used to extract data from the xml filesand save combines data it into simple text file 
#Input: file directory containing all .xml files
#outut: simple text file
#
#Author: sumit chandak  (chandaksumit29@gmail.com)
#Date: 1/12/2018
#
##########################################################



import glob
import fileinput
import pandas as pd
from xml.dom import minidom


def remove_error(flist):
    for filename in flist:
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
                

            

def main():
    sentencedf=pd.DataFrame(columns=['id','text'])
    catchphrasedf=pd.DataFrame(columns=['id','text'])


    files_list=glob.glob("C:/F/task/fulltext/*.xml")    
    remove_error(files_list)
    for filename in files_list:
    
        try:
            xmldoc = minidom.parse(filename)
        except:
            print('sorry unable to read',filename)
        


        catchphraselist = xmldoc.getElementsByTagName('catchphrase') 
        for s in catchphraselist :
                attribute=s.attributes['id'].value
                data=s.firstChild.nodeValue
                catchphrasedf = catchphrasedf.append({'id':attribute, 'text':data}, ignore_index=True)
    


        sentencelist = xmldoc.getElementsByTagName('sentence') 
        for s in sentencelist :
            attribute=s.attributes['id'].value
            data=s.firstChild.nodeValue
            sentencedf = sentencedf.append({'id':attribute, 'text':data}, ignore_index=True)
    
    raw_data_df=pd.concat([sentencedf, catchphrasedf])
    raw_data_df['text'].to_csv('inter_1.txt',sep=' ',header=False, index=False)
    remove_empty_lines('inter_1.txt')
    
    
    
if __name__ == "__main__":
    main()


























        
        
        
        
        
        