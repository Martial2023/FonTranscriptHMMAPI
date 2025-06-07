from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from utils import load_hmm_models, decode_audio

app = FastAPI()
hmm_models, vocab = load_hmm_models(model_dir="hmm_models", vocab_file="vocab.pkl")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://gbe-ce.vercel.app/", "*"],  # Your Next.js frontend origin
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  # Explicitly allow methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def root():
    return {"message": "Bienvenue sur notre API de transcription de texte en langue fon."}

@app.post("/api/transcribe")
async def transcribe_audio(audio: UploadFile = File(...)):
    try:
        # Save the file temporarily
        file_path = f"temp_{audio.filename}"
        with open(file_path, "wb") as f:
            f.write(await audio.read())
        
        predicted_words = " ".join(decode_audio(file_path, hmm_models, vocab))

        # Simulate transcription (replace with your Markov model)
        transcription = predicted_words

        # Delete the temporary file
        os.remove(file_path)

        return JSONResponse(content={"transcription": transcription,
                                     "translation": "Les termes « traite négrière », « traite des nègres » et « traite des noirs » désignent le commerce d'esclaves noirs africains, phénomène historique qui concerne la déportation de dizaines de millions de victimes durant près de treize siècles."
                                     })
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"detail": f"Erreur lors du traitement: {str(e)}"}
        )