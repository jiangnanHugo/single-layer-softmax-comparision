import time

from rnnlm import *
from utils import TextIterator

lr=0.01
n_batch=20
NEPOCH=200

n_input=256
maxlen=200

train_datafile='../data/wikitext-103/idx_wiki.train.tokens'
filepath='../data/wikitext-103/frequenties.pkl'
n_words_source=-1
vocabulary_size=267736

def train():
    # Load data
    print 'loading dataset...'
    train_data=TextIterator(train_datafile,n_words_source=n_words_source,n_batch=n_batch,maxlen=maxlen)

    print 'building model...'
    model=RNNLM(n_input,vocabulary_size)
    print 'training start...'
    time_list=[]
    for epoch in xrange(NEPOCH):
        gain=0
        for x,x_mask,y,y_mask in train_data:
            cost=model.train(x,y,y_mask,lr)
            print cost
            #model.forward(x,y,y_mask)
        time_list.append(gain)

    print time_list


if __name__ == '__main__':
    train()
