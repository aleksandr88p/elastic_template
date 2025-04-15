## Команды для работы с проектом

### Запуск контейнера
```bash
docker-compose up -d
```

### Остановка контейнера
```bash
docker-compose down
```

### Перезапуск контейнера
```bash
docker-compose down
docker-compose up -d
```

### Проверка состояния контейнера
```bash
docker ps
```

### Проверка доступности Elasticsearch
```bash
curl localhost:9200
```

### Работа с Volume
- Список volumes:
  ```bash
  docker volume ls
  ```
- Информация о volume:
  ```bash
  docker volume inspect elastic_template_elasticsearch_data
  ```
- Удаление volume (осторожно!):
  ```bash
  docker volume rm elastic_template_elasticsearch_data
  ```