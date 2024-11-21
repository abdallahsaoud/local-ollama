from s3_config import get_file_from_s3
from ollama_interaction import query_ollama

def local_rag_pipeline(user_query, bucket_name, file_key):
    # Récupérer le document depuis S3
    document = get_file_from_s3(bucket_name, file_key)
    print("Document récupéré depuis S3 :", document)

    # Créer le prompt RAG
    prompt = f"""
    Voici un document : {document}

    Question : {user_query}
    Répondez de manière claire et concise.
    """

    # Interroger Ollama
    response = query_ollama(prompt, model="llama3.2")
    return response

# Test
if __name__ == "__main__":
    bucket_name = "local-rag"  # Nom de ton bucket S3
    file_key = "pdf-exemple.pdf"      # Fichier texte dans ton bucket
    user_query = "Quel est l'origine des JO ?"

    response = local_rag_pipeline(user_query, bucket_name, file_key)
    print("Réponse :", response)
