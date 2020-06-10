from bs4 import BeautifulSoup
import urllib.request
import re, os

def claen_str(string):
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    return string.strip().lower()
url = "https://www.imdb.com/title/tt4154796/reviews?ref_=tt_ov_rt"
htmlData = urllib.request.urlopen(url)
bs = BeautifulSoup(htmlData, 'lxml')

title_list = bs.findAll('a','title')

review_list = bs.findAll('div','text show-more__control')

score_list = bs.findAll('span', 'rating-other-user-rating')

out_dir = os.path.abspath(os.path.join(os.path.curdir, "data"))

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

f = open('data/review.txt', 'w', encoding='utf-8')
for i in range(len(title_list)):
    f.write(claen_str(title_list[i].getText()) + " " + claen_str(review_list[i].getText()) + '\n')
f.close()
f = open('data/score.txt', 'w', encoding='utf-8')
for i in range(len(score_list)):
    f.write(score_list[i].span.getText() + '\n')
f.close()
