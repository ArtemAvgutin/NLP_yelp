# -*- coding: utf-8 -*-

# %tensorflow_version 2.x
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, GRU, LSTM
from tensorflow.keras import utils
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.callbacks import ModelCheckpoint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

num_words = 10000
max_review_len = 100

!wget https://www.dropbox.com/s/ufbhk3kadtnn6h0/yelp_review_polarity_csv.tgz?dl=1 -O yelp_review_polarity_csv.tgz

!tar -xvf yelp_review_polarity_csv.tgz

!cat yelp_review_polarity_csv/readme.txt

!head yelp_review_polarity_csv/train.csv

!head yelp_review_polarity_csv/test.csv

!wc -l yelp_review_polarity_csv/train.csv #строк для обучения
!wc -l yelp_review_polarity_csv/test.csv #строк в тестовой части

train = pd.read_csv('yelp_review_polarity_csv/train.csv',
                    header=None,
                    names=['Class', 'Review'])

train

reviews = train['Review']

reviews[:10]

y_train = train['Class'] - 1

y_train

reviews[:10]

tokenizer = Tokenizer(num_words=num_words)

tokenizer.fit_on_texts(reviews)

tokenizer.word_index

sequences = tokenizer.texts_to_sequences(reviews)

index = 0
print(reviews[index])
print(sequences[index])

tokenizer.word_index['frustration']

x_train = pad_sequences(sequences, maxlen=max_review_len)

x_train[:5]

model = Sequential()
model.add(Embedding(num_words, 64, input_length=max_review_len))
model.add(LSTM(128))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model_save_path = 'best_model.h5'
checkpoint_callback = ModelCheckpoint(model_save_path,
                                      monitor='val_accuracy',
                                      save_best_only=True,
                                      verbose=1)

history = model.fit(x_train,
                    y_train,
                    epochs=5,
                    batch_size=128,
                    validation_split=0.1,
                    callbacks=[checkpoint_callback])

plt.plot(history.history['accuracy'],
         label='Доля верных ответов на обучающем наборе')
plt.plot(history.history['val_accuracy'],
         label='Доля верных ответов на проверочном наборе')
plt.xlabel('Эпоха обучения')
plt.ylabel('Доля верных ответов')
plt.legend()
plt.show()

model.load_weights(model_save_path)

test = pd.read_csv('yelp_review_polarity_csv/test.csv',
                    header=None,
                    names=['Class', 'Review'])

test

test_sequences = tokenizer.texts_to_sequences(test['Review'])

x_test = pad_sequences(test_sequences, maxlen=max_review_len)

x_test[:10]

y_test = test['Class'] - 1

y_test

model.evaluate(x_test, y_test, verbose=1)

text = '''Macdonalds restaurant is worst. It’s a durty place.
The food awful and disgusting.  The host and waiters are rude.
'''

sequence = tokenizer.texts_to_sequences([text])

sequence

data = pad_sequences(sequence, maxlen=max_review_len)

data

result = model.predict(data)

result

if result[[0]] < 0.5:
    print('Negative review')
else:
    print('Positive review')

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, MaxPooling1D, Conv1D, GlobalMaxPooling1D, Dropout

model = Sequential()
model.add(Embedding(num_words, 64, input_length=max_review_len))
model.add(Conv1D(250, 5, padding='valid', activation='relu'))
model.add(GlobalMaxPooling1D())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.summary()

history = model.fit(x_train,
                    y_train,
                    epochs=5,
                    batch_size=128,
                    validation_split=0.1)

plt.plot(history.history['accuracy'],
         label='Доля верных ответов на обучающем наборе')
plt.plot(history.history['val_accuracy'],
         label='Доля верных ответов на проверочном наборе')
plt.xlabel('Эпоха обучения')
plt.ylabel('Доля верных ответов')
plt.legend()
plt.show()

test = pd.read_csv('yelp_review_polarity_csv/test.csv',
                    header=None,
                    names=['Class', 'Review'])
test

test_sequences = tokenizer.texts_to_sequences(test['Review'])
x_test = pad_sequences(test_sequences, maxlen=max_review_len)
x_test[:9]

y_test = test['Class'] - 1
y_test

model.evaluate(x_test, y_test, verbose=1)

text = '''
Everything was delicious. The workers are kind and can always give advice.
'''

sequence = tokenizer.texts_to_sequences([text])
sequence

data = pad_sequences(sequence, maxlen=max_review_len)
data

result = model.predict(data)
result

if result < 0.5:
    print('Отзыв отрицательный')
else:
    print('Отзыв положительный')
