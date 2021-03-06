# coding=utf-8
"""
@author: cer
应用入口
调用模型接口，实现起名
"""

import iv_rnn_one_hot as rnn
import v_gru_c2v as gru
import vi_lstm_c2v as lstm
from ii_data_process import load_training_data, load_sample_training_data
import numpy as np
import time


def generate_name(model, name_len, first_name, X_train, y_train, char_to_index, index_to_char):
    new_name = [char_to_index[first_name]]
    print new_name
    for i in range(name_len-1):
        next_word_probs = model.predict(new_name)
        print "next_word_probs: ",  next_word_probs
        # print sum(sum(next_word_probs))
        samples = np.random.multinomial(1, next_word_probs[-1])
        sampled_word = np.argmax(samples)
        new_name.append(sampled_word)
    name_str = [index_to_char[x] for x in new_name]
    return name_str


def namer_rnn_one_hot():
    # np.random.seed(1)
    # X_train, y_train, char_to_index, index_to_char = load_training_data()
    X_train, y_train, char_to_index, index_to_char = load_sample_training_data(0)
    char_num = len(char_to_index.keys())
    print char_num

    name_num = 10
    name_len = 3
    # first_name = u"宋"
    # first_name = u"董"
    first_name = u"陈"
    if first_name not in char_to_index:
        print "暂时不支持这个姓，Sorry！！！"
    else:
        print "支持这个姓，请稍等 ... ..."
        model = rnn.RNNTheano(char_num)
        # losses = train_with_sgd(model, X_train, y_train, nepoch=50)
        # save_model_parameters_theano('./data/trained-model-theano.npz', model)
        rnn.load_model_parameters_theano('model/rnn_one_hot/model-80-3296-2017-01-14-21-30-39.npz', model)
        ignore_num = 0
        i = 0
        while i <= name_num:
            name = [first_name]
            try:
                name = generate_name(model, name_len, first_name, X_train, y_train, char_to_index, index_to_char)
            except ValueError as ve:
                ignore_num += 1
                continue
            print " ".join(name)
            i += 1
        print "ignored samples: ", ignore_num


def namer_gru_c2v():
    # np.random.seed(1)
    # X_train, y_train, char_to_index, index_to_char = load_training_data()
    X_train, y_train, char_to_index, index_to_char = load_sample_training_data(1)
    char_num = len(char_to_index.keys())
    print char_num

    name_num = 30
    name_len = 3
    # first_name = u"宋"
    # first_name = u"董"
    first_name = u"陈"
    if first_name not in char_to_index:
        print "暂时不支持这个姓，Sorry！！！"
    else:
        print "支持这个姓，请稍等 ... ..."
        model = gru.GRUTheano(char_num)
        gru.load_model_parameters_theano('model/gru_c2v/GRU-2017-01-22-12-09-5264-48-128.dat.npz', model)
        ignore_num = 0
        i = 0
        while i <= name_num:
            name = [first_name]
            try:
                name = generate_name(model, name_len, first_name, X_train, y_train, char_to_index, index_to_char)
            except ValueError as ve:
                ignore_num += 1
                continue
            print " ".join(name)
            i += 1
        print "ignored samples: ", ignore_num


def namer_lstm_c2v():
    # np.random.seed(1)
    # X_train, y_train, char_to_index, index_to_char = load_training_data()
    X_train, y_train, char_to_index, index_to_char = load_sample_training_data(1)
    char_num = len(char_to_index.keys())
    print char_num

    name_num = 10
    name_len = 3
    # first_name = u"宋"
    # first_name = u"董"
    first_name = u"陈"
    if first_name not in char_to_index:
        print "暂时不支持这个姓，Sorry！！！"
    else:
        print "支持这个姓，请稍等 ... ..."
        model = lstm.LSTM()
        model.sample_name(first_name=first_name, ckpt_file="model/lstm_c2v/LSTM-2017-01-29-20-00-6569-400-128.ckpt")


if __name__ == '__main__':
    # namer_rnn_one_hot()
    # namer_gru_c2v()
    namer_lstm_c2v()