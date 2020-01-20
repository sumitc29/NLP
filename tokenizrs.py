#in gensim if you give pandas dataframe it will throw you error, need to give line by line
from gensim import utils
list(utils.tokenize("good morning glad to met you here" , lowercase = True ))


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


#nltk tokenizer word_tokenizer vs sentence_tokenizer
#in nltk tokenizer also we need to use strings ot directly dataframe
from nltk.tokenize import word_tokenize
nltk.download('punkt')

#print(word_tokenize(new_train_data['combined'][0]))


from nltk.tokenize import sent_tokenize
print(len(sent_tokenize(new_train_data['combined'][0])))



#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#keras tokenizer work as tokenizer + vectoriser both
#moreover it will taje all dataframe as input 
from  keras.preprocessing import text

tokenizer = text.Tokenizer(num_words = 1000)
tokenizer.fit_on_texts(new_train_data['combined'])

word_index = tokenizer.word_index
