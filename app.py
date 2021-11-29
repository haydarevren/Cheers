import os
from flask import Flask, render_template, request
import tensorflow as tf
import tensorflow_hub as hub
import dill
import numpy as np
import pandas as pd

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import wordcloud
from PIL import Image

from io import BytesIO
import base64

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
#Load Models and OneHotEncoders

#Sentence Encoder
module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
SENTENCE_ENC = hub.load(module_url)

#Recommender 1
MODEL_REC = tf.keras.models.load_model("models/model_recommender.h5")
N=3 #num of recommendations
#Recommender 2
MODEL_STYLE = tf.keras.models.load_model("models/model_style.h5")
M=6 #num of style recommendations
#Encoders
with open("models/encoder_recommender", "rb") as fin:
    enc = dill.load(fin)
with open("models/encoder_style", "rb") as fin:
    enc_style = dill.load(fin)

df_beers = pd.read_csv('data/beers_clean.csv')

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return render_template('index.html') 

@app.route('/submit', methods=['POST'])
def submit():

    form_text = request.form['form_text'].strip()
    if form_text=='': form_text="fruity, dry, and light on spice. Has a medium body, delicate sweet malt character with a crisp bitter"
    x=SENTENCE_ENC([form_text])

    probs = MODEL_REC.predict(x)
    top_n = np.argsort(probs)[:,:-N-1:-1]

    top_n_beers=[]
    for i in top_n[0]:
        vector = np.zeros(probs.shape)
        vector[0][i]=1
        top_n_beers.append(enc.inverse_transform(vector)[0][0])  

    probs_style = MODEL_STYLE.predict(x)
    top_m = np.argsort(probs_style)[:,:-M-1:-1]

    top_m_styles=[]
    top_m_styles_prob=[]
    for i in top_m[0]:
        vector = np.zeros(probs_style.shape)
        vector[0][i]=1
        top_m_styles.append(enc_style.inverse_transform(vector)[0][0]) 
        top_m_styles_prob.append(probs_style[0][i])

    rates= top_m_styles_prob
    xticklabels = top_m_styles
    
    fig = Figure(figsize=(20,20))
    ax = fig.add_subplot(111,polar=True)
    radii = 10 * np.random.rand(M)
    colors = plt.cm.viridis(radii / 10.)
    
    if max(rates)>0.9:
        rates = np.log(rates) - min(np.log(rates))
    
    theta = np.arange(0, 2*np.pi, 2*np.pi/M) 
    bars = ax.bar(theta, rates, width=1, color=colors, alpha=0.5)

    ax.set_xticks(theta)
    ax.set_xticklabels(xticklabels, fontsize=25)
    ax.yaxis.grid(True)
    ax.set_yticklabels([])
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")

    # Embed the result in the html output.
    polar_chart_url = base64.b64encode(buf.getbuffer()).decode("utf8")

    df_tfidf=pd.read_csv("data/data_corpus_tfidf.csv", index_col=0, )
    df_tfidf.columns=[int(col) for col in df_tfidf.columns] 

    wc_url_dic={}
    beer_names=[]
    beer_notes=[]
    beer_styles=[]

    def black_color_func(word, font_size, position,orientation,random_state=None, **kwargs): return("hsl(0,100%, 1%)")
    mask = np.array(Image.open('images/image_mask.jpg'))
    STOPWORDS = wordcloud.STOPWORDS.add('beer')
    wc = wordcloud.WordCloud(stopwords=STOPWORDS,
                            mask=mask, background_color="white",
                            max_words=200, max_font_size=256, min_font_size=11,
                            random_state=42, width=mask.shape[1],
                            height=mask.shape[0], 
                            color_func=black_color_func,
                            )


    for i,beer in enumerate(top_n_beers):
        wc.generate_from_frequencies(df_tfidf[beer])
        buf = BytesIO()
        wc.to_image().save(buf, 'png')  

        # Embed the result in the html output.
        wc_url_dic[i] = base64.b64encode(buf.getbuffer()).decode("utf8")

        name = df_beers[df_beers.id == beer].name.values[0] 
        txt = df_beers[df_beers.id == beer].notes.values[0]
        style = df_beers[df_beers.id == beer]['style'].values[0]
        beer_names.append(name)
        beer_notes.append(txt)
        beer_styles.append(style)

    return render_template('plot.html', polar_chart_url=polar_chart_url, wc_url_dic=wc_url_dic, beer_names=beer_names, beer_notes=beer_notes, beer_styles=beer_styles)
   

if __name__ == '__main__':
	app.run(debug=True)