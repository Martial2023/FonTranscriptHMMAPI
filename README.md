# API de Transcription de Texte en Langue Fon

Bienvenue dans notre projet de transcription de texte en langue Fon. Cette application utilise des modèles HMM (Hidden Markov Models) pour transcrire des fichiers audio en texte et fournir une traduction contextuelle.

## Fonctionnalités

- **Transcription Audio** : Transcription de fichiers audio en texte en langue Fon.
- **Traduction** : Traduction contextuelle des transcriptions en français.
- **Support Frontend** : Une interface frontend est disponible à l'adresse [gbe-ce.vercel.app](https://gbe-ce.vercel.app).
- **Documentation API** : La documentation de l'API est accessible à [https://fontranscripthmmapi.onrender.com/docs](https://fontranscripthmmapi.onrender.com/docs).

## Structure du Projet

- **main.py** : Contient les endpoints de l'API FastAPI.
  - Endpoint `/` : Retourne un message de bienvenue.
  - Endpoint `/api/transcribe` : Permet de transcrire un fichier audio uploadé.
- **utils.py** : Contient les fonctions utilitaires pour le traitement audio et la gestion des modèles HMM.
  - `extract_mfcc` : Extrait les coefficients MFCC d'un fichier audio.
  - `load_hmm_models` : Charge les modèles HMM et le vocabulaire.
  - `decode_audio` : Transcrit un fichier audio en utilisant les modèles HMM.
  - `translate_sentence` : Traduit une phrase en utilisant un dictionnaire de traductions.

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/Martial2023/FonTranscriptHMMAPI.git
   ```
2. Accédez au répertoire FastAPI :
   ```bash
   cd FastAPI
   ```
3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

### Lancer le Serveur Localement

1. Démarrez le serveur FastAPI :
   ```bash
   uvicorn main:app --reload
   ```
2. Accédez à la documentation interactive de l'API :
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Points de Terminaison Principaux

- **GET /** : Retourne un message de bienvenue.
- **POST /api/transcribe** :
  - Paramètre : Fichier audio (format accepté : `.wav`).
  - Réponse :
    ```json
    {
      "transcription": "<texte transcrit>",
      "translation": "<traduction en français>"
    }
    ```

## Déploiement

- **Frontend** : Disponible à [gbe-ce.vercel.app](https://gbe-ce.vercel.app).
- **API** : Déployée sur Render à [https://fontranscripthmmapi.onrender.com/docs](https://fontranscripthmmapi.onrender.com/docs).

## Contribution

1. Forkez le projet.
2. Créez une branche pour votre fonctionnalité :
   ```bash
   git checkout -b feature/ma-fonctionnalite
   ```
3. Effectuez vos modifications et committez-les :
   ```bash
   git commit -m "Ajout de ma fonctionnalité"
   ```
4. Poussez vos modifications :
   ```bash
   git push origin feature/ma-fonctionnalite
   ```
5. Créez une Pull Request.

## Licence

Ce projet est sous licence MIT.