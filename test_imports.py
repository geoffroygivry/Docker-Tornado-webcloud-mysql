import matplotlib
print('matplotlib: %s' % matplotlib.__version__)
import wordcloud
print('WordCloud: %s' % wordcloud.__version__)
import os
import bs4
print('BeautifulSoup: %s' % bs4.__version__)
from collections import Counter
from string import punctuation
import re
import requests
import nltk
print('nltk: %s' % nltk.__version__)
import tornado
print('tornado: %s' % tornado.version)
import torndb
print('torndb: %s' % torndb.version)
import MySQLdb
print('MySQLdb: %s' % MySQLdb.__version__)

print("All imports succeeded. Well done!")
