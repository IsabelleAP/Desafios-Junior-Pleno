# Desafios-Junior-Pleno

## Desafio 01 - Consumo da API da Gupy 
Este script consome a API pública da Gupy para coletar vagas de emprego
com base em palavras-chave e salva os resultados em arquivos JSON.

Os dados são armazenados na pasta `dados/vagas`.

### Como executar
Clone o repositório (git clone <repo>) > Instale as dependências (pip install requests) > Execute o script (python3 main.py)

### API utilizada
Endpoint:
https://portal.api.gupy.io/api/job

Parâmetros utilizados:
- name: palavra-chave da vaga
- offset: posição inicial da paginação
- limit: quantidade de resultados retornados