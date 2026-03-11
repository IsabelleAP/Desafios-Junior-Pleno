# Desafios-Junior-Pleno

## Desafio 01 - Consumo da API da Gupy 
Este script consome a API pública da Gupy para coletar vagas de emprego com base em palavras-chave e salva os resultados em arquivos JSON.

Os dados estão armazenados na pasta `dados/vagas`.

### Estrutura do projeto
```
desafios-junior-pleno
│
├─ src/
│  ├─ api.py        # funções responsáveis por consumir a API
│  ├─ storage.py    # funções responsáveis por salvar arquivos
│  └─ main.py       # fluxo principal do programa
│
└─ dados/
   └─ vagas/        # arquivos JSON gerados pelo script
```

### Como executar
1. Clone o repositório 
`git clone <repo>`
2. Entre na pasta do projeto
3. Instale as dependências 
`pip install requests`
4. Execute o script 
`python3 src/main.py`

Após a execução, os arquivos JSON com as vagas coletadas serão gerados na pasta `dados/vagas`.

### API utilizada
Endpoint: https://portal.api.gupy.io/api/job

Parâmetros utilizados:
- name: palavra-chave para busca de vagas
- offset: posição inicial da paginação
- limit: quantidade de resultados retornados