import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Carrega as variáveis do arquivo .env
load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)

print("Conexão profissional via .env validada!")
# Teste de leitura
response = supabase.table('teste').select("*").execute()
print(response.data)