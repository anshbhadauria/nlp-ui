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

selected_db=st.sidebar.selectbox("Database", [
    "db 1", "db 2"
    ])

selected_table=st.sidebar.selectbox("Table", [
    "table 1", "table 2"
    ])

selected_engine=st.sidebar.selectbox("NLP Engines", [
    "Spacy", "Apache OpenNLP", "NLTK", "AllenNLP","flairNLP","gensim", "SparkNLP"
    ])

if selected_engine=="Spacy":
    import spacy_streamlit

    models = ["en_core_web_sm", "en_core_web_md"]
    default_text = "Sundar Pichai is the CEO of Google."
    spacy_streamlit.visualize(models, default_text)

select_preprocess=st.sidebar.multiselect("Preprocesses",options=["Lemmatization","Tokenization"])

select_tasks=st.sidebar.multiselect("Tasks",options=["NER", "Sentiment analysis"])

st.write(selected_db+" > "+selected_table)