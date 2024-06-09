# ZSSN - Rede social de sobrevivencia Zumbi

[![Versão](https://img.shields.io/github/v/release/LiedsonLB/desafio-infoG2)](https://github.com/LiedsonLB/desafio-infoG2/releases)
[![Forks](https://img.shields.io/github/forks/LiedsonLB/desafio-infoG2)](https://github.com/LiedsonLB/desafio-infoG2/network/members)
[![Contribuidores](https://img.shields.io/github/contributors/LiedsonLB/desafio-infoG2)](https://github.com/LiedsonLB/desafio-infoG2/graphs/contributors)
[![Pull Requests Abertos](https://img.shields.io/github/issues-pr/LiedsonLB/desafio-infoG2)](https://github.com/LiedsonLB/desafio-infoG2/pulls)
[![Última Atualização](https://img.shields.io/github/last-commit/LiedsonLB/desafio-infoG2)](https://github.com/LiedsonLB/desafio-infoG2/commits/master)

![NeoBoard](/img//zssn_initialPage.png)

ZSSN é o último vestígio de esperança em um mundo dilacerado, uma rede social de sobreviventes que colaboram, trocam recursos e estão alertas para as ameaças de zumbis. Em um cenário pós-apocalíptico, onde a solidariedade é a chave para a sobrevivência, ZSSN une aqueles que buscam apoio mútuo em meio ao caos, oferecendo um refúgio digital onde podem compartilhar informações e recursos.

## Design

- **Figma:** [ZSSN Figma](https://www.figma.com/design/Sg56PrGMQTkzuMh8UScyP4/ZSSN?node-id=0-1&t=0QHMiXPD4MQoceYy-0)

## Relatório de trabalho
- 03/06/2024 - criação do designer figma e estrutura do projeto (6h)
- 04/06/2024 - criação da models, views, e pastas da api (4h30)
- 05/06/2024 - criação da página Login e Modal Recursos (4h)
- 06/06/2024 - (0h)
- 07/06/2024 - (0h)
- 08/06/2024 - Teste das rotas de api interagindo com front (3h)
- 09/06/2024 - página de sobrevivente e layouts (6h)

## Testes

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/cypressio/cypressio-original.svg" alt="cypress" height="30" width="40" style="margin: 0 auto; width: 100%"> <br />
<p style="text-align: center">Ferramenta de Testes: Cypress</p>

- Teste de carregamento de componentes HTML ❌
- Envio de dados normal ❌
- Testes funcionais ❌
- Testes de banco e API ❌
- Testes de sistema ❌

# Conhecimentos utilizados:
<div style="display: flex; flex-wrap: wrap; gap: 5px; justify-content:center">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg" alt="HTML" height="30" width="40">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original.svg" alt="CSS" height="30" width="40">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/typescript/typescript-plain.svg" alt="typescript" height="30" width="40">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vuejs/vuejs-original.svg" height="30" width="40">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Git" height="30" width="40"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" alt="django" height="30" width="40" >
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/npm/npm-original-wordmark.svg" alt="npm" height="30" width="40">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" height="30" width="40">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" height="30" width="40">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/figma/figma-original.svg" height="30" width="40">        
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="github" height="30" width="40">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" alt="vscode" height="30" width="40">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" alt="Git" height="30" width="40"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" alt="Git" height="30" width="40"/>     
</div>
<br />

# Rodando o Projeto

## Clone o Repositório

1. Abra o terminal.

2. Navegue até o diretório onde deseja clonar o repositório.

3. Execute o seguinte comando:

```bash
git clone https://github.com/LiedsonLB/desafio-infoG2.git
```

## Execute o PostgreSQL com Docker Compose

1. Certifique-se de ter o Docker e o Docker Compose instalados em seu sistema.
2. Navegue até o diretório `desafio_ZSSN`.
3. Execute o seguinte comando para iniciar o contêiner:
``` bash
docker-compose up -d
```

## Execute o Vue

1. Navegue até o diretório<br/>
`desafio-infoG2/desafio_ZSSN/frontend`.
2. Instale as dependências utilizando npm ou yarn:
``` bash
npm install
```
ou
``` bash
yarn install
```

3. Inicie o servidor de desenvolvimento:
``` bash
npm run serve
```
ou
``` bash
yarn serve
```

## Execute o Django

1. Navegue até o diretório<br/>
`desafio-infoG2/desafio_ZSSN/backend`.
2. Instale as dependências do Python, geralmente feito com pip:

``` bash
pip install -r requirements.txt
```
3. Execute o servidor Django:
``` bash
python manage.py runserver
```

## Releases

- Release v1.0 ✅