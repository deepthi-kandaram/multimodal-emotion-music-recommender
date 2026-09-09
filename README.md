# Multimodal Emotion Recognition Music Recommender Using LLMs

An end-to-end intelligent recommendation system that detects user emotions across multiple modalities (Facial Expressions, Speech/Audio, and Text) and leverages Large Language Models (LLMs) to generate personalized music recommendations and tailored explanations.

## 📌 Features
- **Multimodal Emotion Detection**: Real-time emotion classification using facial cues (OpenCV/CNNs), voice tone analysis, and text input.
- **LLM-Driven Recommendations**: Utilizes an LLM to contextualize detected emotions, reason about listener intent, and curate tailored music playlists.
- **Dynamic Contextual Explanation**: Generates personalized, empathetic reasoning for why each track suits the user's current mood.
- **Interactive UI**: User-friendly web dashboard for real-time video/audio input and playlist generation.

## 🏗 System Architecture
1. **Input Layer**: Captures video stream, audio input, or user text prompt.
2. **Feature Extraction & Classification**:
   - Facial Emotion Recognition (FER) via CNN / Vision Models.
   - Speech Emotion Recognition (SER) via Librosa / Transformers.
   - Text Sentiment Analysis via NLP/BERT.
3. **Multimodal Fusion Engine**: Combines modal outputs into a unified emotion vector.
4. **LLM Orchestration**: Passes emotion metadata and user preferences to an LLM to select tracks via Spotify / Deezer API integration.

## 🛠 Tech Stack
- **Languages**: Python
- **ML/DL Frameworks**: PyTorch / TensorFlow, OpenCV, Hugging Face Transformers
- **LLM Framework**: LangChain / OpenAI API / Llama / Ollama
- **Audio Processing**: Librosa
- **Web App**: Streamlit / FastAPI
- **External APIs**: Spotify Web API

## 📜 License
Distributed under the MIT License.
