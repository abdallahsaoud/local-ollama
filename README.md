Local-RAG : Retrieval-Augmented Generation avec Ollama
Ce projet met en œuvre un pipeline de RAG (Retrieval-Augmented Generation) en utilisant des documents récupérés depuis un bucket AWS S3 pour alimenter le modèle d'intelligence artificielle llama3.2, accessible via l'API HTTP d'Ollama.

Fonctionnalités

Récupération de documents depuis AWS S3 :
Récupération automatique de fichiers texte ou PDF à partir d'un bucket AWS S3 configuré.
Extraction du texte des fichiers PDF grâce à PyPDF2.

Interaction avec Ollama :
Utilise le modèle llama3.2 via une API HTTP locale.
Génère des réponses basées sur les documents récupérés ou uniquement sur la requête utilisateur.

Pipeline RAG :
Combine le contenu récupéré depuis S3 avec une requête utilisateur pour fournir des réponses pertinentes.
Paramètre de température configurable pour ajuster la créativité des réponses.
Prérequis

Environnement logiciel :
- Python 3.7+
- AWS CLI configuré avec des accès valides à un bucket S3.
- Ollama installé sur la machine locale avec le modèle llama3.2.

Bibliothèques Python requises :

- boto3 : pour interagir avec AWS S3.
- PyPDF2 : pour extraire le texte des fichiers PDF.
- python-dotenv : pour gérer les variables d'environnement.
- requests : pour interagir avec l'API HTTP d'Ollama.


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
pip install boto3 PyPDF2 python-dotenv requests
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

Lancer Ollama sur le serveur local
Une fois Ollama installé et le modèle llama3.2 téléchargé, voici les étapes pour démarrer le serveur local et s'assurer qu'il fonctionne correctement.

1. Démarrer Ollama
Pour lancer le serveur local d'Ollama, exécute cette commande dans le terminal :

```bash
ollama serve
```
Par défaut, le serveur écoute sur http://localhost:11434.
Si cette commande fonctionne correctement, tu verras un message comme :
```bash
Listening on http://localhost:11434
```
2. Tester si le serveur est actif
Tu peux vérifier si le serveur est actif en exécutant cette commande :

```bash
curl http://localhost:11434/api/generate
```
Si le serveur est actif, tu obtiendras une réponse indiquant que des paramètres manquent (comme 404 page not found ou une erreur JSON).
Si rien n’apparaît ou si la commande échoue, vérifie que le serveur est bien démarré.

Commandes utiles pour vérifier et gérer Ollama
1. Vérifier les processus utilisant le port
Si Ollama ne démarre pas parce que le port est déjà utilisé, identifie le processus qui l'occupe :

```bash
lsof -i :11434
```
Exemple de sortie :

```bash
COMMAND  PID       USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
ollama   1531 abdellahsa    3u  IPv4 0xab8e2b3f059393db      0t0  TCP localhost:11434 (LISTEN)
```
COMMAND : Le programme utilisant le port.
PID : L'identifiant du processus.

2. Tuer un processus bloquant
Si Ollama est déjà en cours d'exécution ou si un autre processus bloque le port, tu peux le forcer à se terminer :

```bash
kill -9 <PID>
```

Après cela, relance Ollama avec :

```bash
ollama serve
```


Utilisation

Configuration

Configurer le bucket S3 :
Vérifiez que votre bucket S3 contient un fichier texte ou PDF.
Par défaut, le bucket est configuré comme suit :
Nom du bucket : local-rag
Clé du fichier : pdf-exemple.pdf
Vous pouvez modifier ces valeurs dans les fichier s3_config.py et main.py.

Lancez le script principal :
```bash
python main.py
```

Entrez les informations demandées dans le terminal :

Question utilisateur : La question à laquelle vous souhaitez obtenir une réponse.
Utiliser RAG ? : Répondez "oui" pour inclure le document récupéré depuis S3 dans la réponse, sinon "non".
Température : Une valeur entre 0.0 (réponses déterministes) et 1.0 (réponses créatives).

Exemple de sortie attendue : 
Le fichier pdf-exemple.pdf dans S3 contient :
des informations sur les origine des JO

Essayer la requête :
Quel est l'origine des JO ?

La sortie sera une réponse générée par le modèle llama3.2 de ollama
