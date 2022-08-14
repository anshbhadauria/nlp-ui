import streamlit as st

project_uris={
    "Spacy":"https://spacy.io/",
    "Apache OpenNLP": "https://opennlp.apache.org/",
    "NLTK":"http://www.nltk.org/",
    "AllenNLP":"https://allennlp.org/",
    "flairNLP":"https://github.com/flairNLP/flair",
    "gensim":"https://github.com/RaRe-Technologies/gensim",
    "SparkNLP":"https://nlp.johnsnowlabs.com/"
}

selected_engine=st.sidebar.selectbox("NLP Engines", [
    "Spacy", "Apache OpenNLP", "NLTK", "AllenNLP","flairNLP","gensim", "SparkNLP"
    ])

st.write(selected_engine)
st.write(project_uris[selected_engine])