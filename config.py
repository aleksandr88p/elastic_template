


index_name = "laws"


conteiner_adress = "http://elasticsearch:9200"
local_adress = "http://localhost:9200"


IN_CONTEINER = True

address = local_adress if not IN_CONTEINER else conteiner_adress
