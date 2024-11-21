import boto3
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader

# Charger les variables d'environnement
load_dotenv(".env")

# Configuration AWS
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name='eu-north-1'
)

def get_file_from_s3(bucket_name, file_key):
    # Récupération de l'objet S3
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    content = response['Body'].read()
    
    # Gestion des fichiers PDF
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

    # Gestion des fichiers texte
    else:
        return content.decode('utf-16')  # Modifier l'encodage si nécessaire
