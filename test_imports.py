import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS 
import os
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation
import re
import requests
import nltk
import tornado.ioloop
import tornado.web

print("looking great!")