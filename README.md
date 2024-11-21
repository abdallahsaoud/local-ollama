Local-RAG: Retrieval-Augmented Generation avec Ollama
Ce projet implémente un pipeline de RAG (Retrieval-Augmented Generation), combinant la récupération de documents depuis un bucket S3 et l'utilisation du modèle d'IA llama3.2 via Ollama pour répondre à des questions basées sur le contenu des documents.

Fonctionnalités
Récupération de fichiers depuis S3 :

Le projet permet de récupérer des fichiers texte depuis un bucket AWS S3 à l'aide du SDK boto3.
Interaction avec le modèle Ollama :

Utilise le modèle llama3.2 pour générer des réponses basées sur les documents récupérés.
Pipeline RAG :

Combine le texte récupéré depuis S3 avec une requête utilisateur pour générer des réponses pertinentes.
Prérequis
Python (Version 3.7 ou supérieure)
AWS CLI configuré avec des accès valides à un bucket S3
Ollama installé sur la machine locale
Modules Python requis :
- boto3
- subprocess


Installation

1. Clonez le dépôt
```bash 
git clone https://github.com/votre-utilisateur/local-rag.git
cd local-rag
```
2. Créez un environnement virtuel
```bash
python3 -m venv .env
source .env/bin/activate  # Sur Windows : .env\Scripts\activate
```
3. Installez les dépendances
```bash
pip install boto3
```
4. Configurez vos clés AWS
Exportez vos Access Key ID et Secret Access Key comme variables d'environnement dans un fichier .env :
```bash
 AWS_ACCESS_KEY_ID="AKIAYUQGSUPDSMAM4N5D"
 AWS_SECRET_ACCESS_KEY="v8DEKVI9AbhvBRG9zcKeVTRQWRa01kWNBeb7YEa5m"
```

5. Installez Ollama

Téléchargez et installez Ollama depuis ollama.ai.
Téléchargez le modèle llama3.2 :
```bash
ollama pull llama3.2
```

Utilisation
Configurez votre bucket S3 :

Assurez-vous qu'un fichier texte est présent dans le bucket S3 configuré (rag-documents).
Lancez le script principal :

```bash
python main.py
```
Exemple de sortie attendue : Si le fichier dans S3 contient :
Les Jeux Olympiques modernes ont été créés en 1896.

Et que la requête est :
Quel est l'origine des JO ?

La sortie sera une réponse générée par le modèle Ollama.
