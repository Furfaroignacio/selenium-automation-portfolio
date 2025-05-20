# API Testing - JSONPlaceholder

Este proyecto contiene pruebas automatizadas de la API pública JSONPlaceholder usando Python, pytest y requests.

## Endpoints testeados

- GET /users
- GET /users/999
- POST /posts
- DELETE /posts/1

### Capturas

![Resultados de pytest](./api-testing/evidencia/pytest_resultado.png)


## Cómo ejecutar

```bash
pip install -r requirements.txt
pytest
