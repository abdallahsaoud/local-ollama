import boto3
import os
from PyPDF2 import PdfReader
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv(".env")

# Configuration AWS
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name='eu-north-1'
)

# Bucket et fichier en dur (modifiable si besoin)
bucket_name = "local-rag"  # Nom du bucket S3
file_key = "pdf-exemple.pdf"  # Clé du fichier dans le bucket

def get_file_from_s3(bucket_name, file_key):
    """
    Récupère le contenu d'un fichier depuis un bucket S3 et le convertit en texte.
    """
    try:
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        content = response['Body'].read()

        # Identifier le type de fichier en fonction de son extension
        if file_key.lower().endswith('.pdf'):
            # Sauvegarde temporaire pour lire avec PyPDF2
            temp_file_path = "/tmp/temp_document.pdf"
            with open(temp_file_path, "wb") as temp_file:
                temp_file.write(content)
            
            # Lecture du texte du PDF
            reader = PdfReader(temp_file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text()

            # Supprimer le fichier temporaire
            os.remove(temp_file_path)
            return text
        else:
            # Supposer que c'est un fichier texte
            return content.decode('utf-8')
    except Exception as e:
        print(f"Erreur lors de la récupération ou du traitement du fichier S3 : {e}")
        return None




