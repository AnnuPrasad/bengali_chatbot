# -*- coding: utf-8 -*-
"""chatbot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZiRS9aXpRhbnMRbxx796rMKC4I2aFKEk
"""

import nltk

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

import json

import pickle

import numpy as np

from keras.models import Sequential

from keras.layers import Dense, Activation, Dropout

from keras.optimizers import SGD

import random

# Sample dataset (you can replace this with your Bengali dataset)
data_1 = open('data.json').read()

data = json.loads(data_1)

!pip install SpeechRecognition

!pip install pydub

import os
from pydub import AudioSegment
from nltk.corpus import stopwords
import speech_recognition as sr


for filename in os.listdir("/content/audios"):
    if not filename.endswith(".wav"):
        print(f"File '{filename}' is not in WAV format.")

# Initialize the recognizer
recognizer = sr.Recognizer()

# Define a function to transcribe audio files
import os
from pydub import AudioSegment
import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

def transcribe_audio(audio_folder):
    transcribed_texts = []  # List to store transcribed texts
    for filename in os.listdir(audio_folder):
        if filename.endswith(".wav"):  # Check if the file is a WAV file
            audio_file_path = os.path.join(audio_folder, filename)
            with sr.AudioFile(audio_file_path) as source:
                audio_data = recognizer.record(source)
    return transcribed_texts


audio_folder_path = "/content/audios"
transcribed_texts = transcribe_audio(audio_folder_path)


# Replace sample_data with the transcribed text
data_1 = open("data.json").read()

data = json.loads(data_1)

# Download NLTK resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')


# Initialize lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('bengali'))


# # Tokenize, lemmatize, and remove stopwords
# tokenized_data = []
# for sentence in data:
#     lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]  # Lemmatize tokens
#     filtered_tokens = [token for token in lemmatized_tokens if token not in stop_words]  # Remove stop words
#     tokenized_data.append(filtered_tokens)

# # Remove duplicate words
# for i in range(len(tokenized_data)):
#     tokenized_data[i] = list(set(tokenized_data[i]))

# print(tokenized_data)

!pip install classes

!pip install bnlp

import numpy as np
import random
from nltk.tokenize import word_tokenize

# Define your classes for Bengali language
classes = ["politics", "sports", "entertainment", "technology", "health", "education"]

# Sample documents (replace with your actual data)
documents = [
    ("খেলাধুলা সম্পর্কে সংবাদ", "sports"),
    ("প্রযুক্তি নিয়ে আলোচনা", "technology"),
    ("সরকারের নীতিমালা সম্পর্কে বিবৃতি", "politics"),
    ("বিনোদনের প্রচ্ছদ", "entertainment"),
    ("স্বাস্থ্য সংক্রান্ত প্রতিবেদন", "health"),
    ("শিক্ষা ও শিক্ষার্থীরা", "education")
]

# Initialize an empty list for training data
training = []

# Create an empty array of zeros for output representation
output_empty = [0] * len(classes)

# Collect all unique words from documents
words = set()
for doc in documents:
    words.update(word_tokenize(doc[0]))

# Iterate over each document for processing
for doc in documents:
    bag = []

    # Tokenize words in the document
    pattern_words = word_tokenize(doc[0])
    pattern_words = [word.lower() for word in pattern_words]

    # Create bag of words representation
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # Create output row for classification
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    # Append bag of words and output row to training data
    training.append([bag, output_row])

# Shuffle training data
random.shuffle(training)

# Separate features and labels
train_x = np.array([sample[0] for sample in training])
train_y = np.array([sample[1] for sample in training])

# Print shapes for verification
print("Shape of train_x:", train_x.shape)
print("Shape of train_y:", train_y.shape)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.optimizers.legacy import SGD as LegacySGD

# Define the model
model = Sequential()

# Add layers to the model
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Use the legacy optimizer
sgd = LegacySGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Train the model
model.fit(train_x, train_y, epochs=200, batch_size=5, verbose=1)

# Save the model
model.save('chatbot_model.h5')

def predict_class(sentence, model):

    p = bow(sentence, words, show_details=False)

    res = model.predict(np.array([p]))[0]

    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)

    return_list = []

    for r in results:

        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})

    return return_list

!pip install PyQt5

!pip install tk

!pip install python-tk

!apt-get update
!apt-get install -y xvfb

!pip install pyvirtualdisplay

!export DISPLAY=:0

!pip install nltk

!jupyter notebook --port 8888 --no-browser &

# GUI with Tkinter

import tkinter as tk
from tkinter import *
from pyvirtualdisplay import Display

# Function to send message and get response
def chatbot_response(msg):
    # Here you would implement the logic to generate the chatbot's response based on the user's message
    # For demonstration, let's just return a static response
    return "This is a static response from the chatbot."

def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12))
        res = chatbot_response(msg)
        ChatLog.insert(END, "Bot: " + res + '\n\n')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

# Create a virtual display
display = Display(visible=0, size=(800, 600))
display.start()

# GUI setup
root = tk.Tk()
root.title("Chatbot")
root.geometry("400x500")
root.resizable(width=FALSE, height=FALSE)

ChatLog = Text(root, bd=0, bg="white", height="8", width="50", font="Arial")
ChatLog.config(state=DISABLED)

scrollbar = Scrollbar(root, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

SendButton = Button(root, font=("Verdana",12,'bold'), text="Send", width="12", height=5, bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff', command= send )

EntryBox = Text(root, bd=0, bg="white",width="29", height="5", font="Arial")

scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

root.mainloop()

# Stop the virtual display
display.stop()