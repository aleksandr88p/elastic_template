import os
from dotenv import load_dotenv
load_dotenv()



index_name = "laws"


conteiner_adress = "http://elasticsearch:9200"
local_adress = "http://localhost:9200"


IN_CONTEINER = True

address = local_adress if not IN_CONTEINER else conteiner_adress


bonsai_url = os.getenv("BONSAI_URL")
bonsai_access_key = os.getenv("BONSAI_ACCESS_KEY")
bonsai_secret_token = os.getenv("BONSAI_SECRET_TOKEN")
