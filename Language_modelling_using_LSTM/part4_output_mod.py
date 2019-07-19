################  Output #####################
############### part 4 of  Phrase prediction Algo #####
#Action : to generate the reasult using trained model 
#Input: ML model and tokanizer.pkl file generated using part 3 
#outut: Next word for the given stream
#
#Author: sumit chandak  (chandaksumit29@gmail.com)
#Date: 1/12/2018
#
##########################################################
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from pickle import load
from random import randint

import pandas as pd

def load_data(filename):
	file = open(filename, 'r')
	text = file.read()
	file.close()
	return text


def get_seq(model, token, seq_length, test_text, out):
	output = list()
	for _ in range(out):
		encoded = token.texts_to_sequences([test_text])[0]
		encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
		y_out = model.predict_classes(encoded, verbose=0)
		out_word = ''
		for word, index in token.word_index.items():
			if index == y_out:
				out_word = word
				break
		test_text += ' ' + out_word
		output.append(out_word)
	return ' '.join(output)

def write_file(data_list,filename):
    with open(filename, 'w') as f:
        for item in data_list:
            f.write("%s\n" % item)


def main():
    in_filename = 'inter_2.txt'
    data = load_data(in_filename)
    lines = data.split('\n')

    token = load(open('token_class.pkl', 'rb'))

    seq_length = len(lines[0].split()) - 1

    model = load_model('model.h5')
    test_text=[]
    predicted_text=[]
    for i in range(0,50):

        text = lines[randint(0,len(lines))]
        test_text.append(text)
        generated = get_seq(model, token, seq_length, text, 1)
        predicted_text.append(generated)
    output=test_text

    for each in range(len(output)):
        print(each)
        output[each]=output[each].rsplit(' ', 1)[0]+" "+predicted_text[each]
    
    test_file='test_file.txt'
    predicted_file='predicted_file.txt'

    write_file(test_text,test_file)
    write_file(output,predicted_file)
    
if __name__ == "__main__":
    main()
    



