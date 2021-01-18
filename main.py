import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

#nltk.download('punkt')

def summarize():
    
    url=URL.get('1.0','end').strip()
    
    
    article=Article(url)
    
    article.download()
    
    article.parse()
    
    article.nlp()
    
    sentiment_analysis=TextBlob(article.text)
    
    title.config(state='normal')
    author.config(state='normal')
    pub_date.config(state='normal') 
    summary.config(state='normal')
    sentiment.config(state='normal')
    
    title.delete('1.0','end')
    title.insert('1.0',article.title)
    
    author.delete('1.0','end')
    author.insert('1.0',article.authors)
    
    pub_date.delete('1.0','end')
    pub_date.insert('1.0',article.publish_date)
    
    summary.delete('1.0','end')
    summary.insert('1.0',article.summary)
    
    sentiment.delete('1.0','end')
    sentiment.insert('1.0',f'Polartity: {sentiment_analysis.polarity} Sentiment {"positive" if sentiment_analysis.polarity > 0 else "negative" if sentiment_analysis.polarity < 0 else "neutral"}')
    
    title.config(state='diabled')
    author.config(state='disabled')
    pub_date.config(state='disabled') 
    summary.config(state='disabled')
    sentiment.config(state='disabled')
    
root=tk.Tk()
root.title('News Summarizer')
root.geometry('1200x600')

title_label=tk.Label(root,text='Title')
title_label.pack()
title=tk.Text(root,height=1, width=140)
title.config(state='disabled',bg='#dddddd')
title.pack()

author_label=tk.Label(root,text='Author')
author_label.pack()
author=tk.Text(root,height=1, width=140)
author.config(state='disabled',bg='#dddddd')
author.pack()

date_label=tk.Label(root,text='Publication Date')
date_label.pack()
pub_date=tk.Text(root,height=1, width=140)
pub_date.config(state='disabled',bg='#dddddd')
pub_date.pack()

summary_label=tk.Label(root,text='Summary')
summary_label.pack()
summary=tk.Text(root,height=18, width=140)
summary.config(state='disabled',bg='#dddddd')
summary.pack()

sentiment_label=tk.Label(root,text='Sentiment Analysis')
sentiment_label.pack()
sentiment=tk.Text(root,height=1, width=140)
sentiment.config(state='disabled',bg='#dddddd')
sentiment.pack()

url_label=tk.Label(root,text='URL')
url_label.pack()
URL=tk.Text(root,height=1, width=140)
URL.config(state='normal',bg='#dddddd')
URL.pack()


button=tk.Button(root,text='Summarize',command=summarize)
button.pack()
root.mainloop()


