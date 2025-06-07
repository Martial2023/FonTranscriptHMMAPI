import pickle
import os
import librosa
import json

translations = json.load(open("translations.json", "r"))

# Fonction pour extraire les MFCC (identique à avant)
def extract_mfcc(wav_file, n_mfcc=13):
    y, sr = librosa.load(wav_file, sr=16000)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    return mfcc.T

# Fonction pour charger les modèles HMM et le vocabulaire
def load_hmm_models(model_dir="hmm_models", vocab_file="vocab.pkl"):
    hmm_models = {}
    
    # Charger le vocabulaire
    with open(vocab_file, 'rb') as f:
        vocab = pickle.load(f)
    
    # Charger chaque modèle HMM
    for word in vocab.keys():
        model_path = os.path.join(model_dir, f"{word}.pkl")
        if os.path.exists(model_path):
            with open(model_path, 'rb') as f:
                hmm_models[word] = pickle.load(f)
    
    print(f"{len(hmm_models)} modèles chargés depuis {model_dir}")
    return hmm_models, vocab

# Fonction pour transcrire un fichier audio
def decode_audio(wav_file, hmm_models, vocab, n_mfcc=13):
    mfcc = extract_mfcc(wav_file, n_mfcc)
    scores = {}
    for word, model in hmm_models.items():
        try:
            score = model.score(mfcc)
            scores[word] = score
        except:
            continue
    # Retourner les top 3 mots prédits
    predicted_words = sorted(scores, key=scores.get, reverse=True)[:10]
    return predicted_words

# Étape 2 : Traduire une phrase
def translate_sentence(sentence):
    translated_sentence = []
    for word in sentence.split():
        # Chercher le mot dans le dictionnaire
        translated_word = translations.get(word, word)  # Si le mot n'est pas trouvé, on le laisse tel quel
        translated_sentence.append(translated_word)
    return ' '.join(translated_sentence)
