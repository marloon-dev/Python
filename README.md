<div align="center">

# 🐍 Python — Estudos de Programação

**Exercícios, aulas e desafios de Python, do primeiro `print` às estruturas de controle.**

[![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![CI](https://github.com/marloon-dev/Python/actions/workflows/ci.yml/badge.svg)](https://github.com/marloon-dev/Python/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/marloon-dev/Python?label=vers%C3%A3o)](https://github.com/marloon-dev/Python/releases)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-FE5196?logo=conventionalcommits&logoColor=white)](https://www.conventionalcommits.org/pt-br/v1.0.0/)
[![Licença: MIT](https://img.shields.io/badge/licen%C3%A7a-MIT-green)](LICENSE)

</div>

---

## Sumário

- [Sobre](#sobre)
- [Progresso](#progresso)
- [Como executar](#como-executar)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Catálogo](#catálogo)
- [Convenções](#convenções)
- [Roadmap](#roadmap)
- [Licença](#licença)

## Sobre

Repositório onde registro minha evolução em Python. Reúne:

- os **Mundos 1 e 2** do curso de Python do [Curso em Vídeo](https://www.cursoemvideo.com/) (Gustavo Guanabara) — aulas e desafios;
- **exercícios de nivelamento** de Programação de Computadores, como simuladores de ponto de venda e de análise de crédito;
- **projetos extra**, como um jogo da velha com interface gráfica.

Cada exercício é um script independente, executado no terminal.

## Progresso

| Etapa | Conteúdo | Progresso |
|---|---|---|
| **Mundo 1** — Fundamentos | Aulas 06–11 · Desafios 001–035 | ![100%](https://img.shields.io/badge/35%2F35-concluído-brightgreen) |
| **Mundo 2** — Estruturas de controle | Aula 12 · Exercícios 036–071 | ![17/36](https://img.shields.io/badge/17%2F36-em%20andamento-yellow) |
| **Mundo 3** — Estruturas compostas | Exercícios 072–115 | ![a iniciar](https://img.shields.io/badge/0%2F44-a%20iniciar-lightgrey) |

As versões publicadas acompanham este progresso — ver [Releases](https://github.com/marloon-dev/Python/releases).

## Como executar

**Requisitos:** [Python 3](https://www.python.org/downloads/) (os scripts são verificados com Python 3.10 e 3.13 no CI).

```bash
git clone https://github.com/marloon-dev/Python.git
cd Python

# Opcional: ambiente virtual e dependências de alguns scripts
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Executar um exercício
python3 "Gustavo Guanabara Python/MUNDO - 02/EXERCÍCIOS/ex045.py"
```

A maioria dos scripts usa apenas a biblioteca padrão. As exceções estão no [`requirements.txt`](requirements.txt):

| Script | Dependência | Observação |
|---|---|---|
| `MUNDO - 01/Aulas/aula008b.py` | `emoji` | — |
| `MUNDO - 01/Desafios/des021` | `python-vlc` | Requer o [VLC](https://www.videolan.org/) instalado; ver o [README do desafio](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des021/README.md) |
| `Exercícios/jogo da velha.py`, `MUNDO - 02/EXERCÍCIOS/main.py` | `tkinter` | Incluído no Python; em Linux pode ser preciso `sudo apt install python3-tk` |

> Os exercícios do Mundo 2 usam cores ANSI. No Windows, use o **Windows Terminal** ou o terminal do VS Code para vê-las corretamente.

## Estrutura do repositório

```
Python/
├── Exercícios/                    Nivelamento e projetos extra
│   ├── Análise de Crédito Estudantil (ACE).py
│   ├── Calculadora de Saúde (IMC).py
│   ├── IMCAtualizado.py
│   ├── Ponto de Venda (PDV).py
│   ├── jogo da velha.py           Interface gráfica com Tkinter
│   └── quiz.py
├── Gustavo Guanabara Python/
│   ├── MUNDO - 01/
│   │   ├── Aulas/                 aula006a.py … aula011.py
│   │   └── Desafios/              des001.py … des035.py (des021/ em pasta própria)
│   └── MUNDO - 02/
│       ├── AULAS/                 aula012a.py
│       └── EXERCÍCIOS/            ex036.py … ex053.py, main.py
├── .github/workflows/ci.yml       Verifica a sintaxe de todos os scripts
├── requirements.txt               Dependências opcionais
└── LICENSE
```

## Catálogo

<details>
<summary><strong>Exercícios de nivelamento e projetos extra</strong> (6)</summary>

| Script | Descrição |
|---|---|
| [Ponto de Venda (PDV)](Exerc%C3%ADcios/Ponto%20de%20Venda%20%28PDV%29.py) | Simulador de caixa: valor da compra, desconto à vista ou parcelamento |
| [Análise de Crédito Estudantil (ACE)](Exerc%C3%ADcios/An%C3%A1lise%20de%20Cr%C3%A9dito%20Estudantil%20%28ACE%29.py) | Aprova ou nega crédito conforme a capacidade de pagamento |
| [Calculadora de Saúde (IMC)](Exerc%C3%ADcios/Calculadora%20de%20Sa%C3%BAde%20%28IMC%29.py) | Cálculo do IMC |
| [IMC atualizado](Exerc%C3%ADcios/IMCAtualizado.py) | Versão com classificação e dados armazenados em um dicionário |
| [Jogo da velha](Exerc%C3%ADcios/jogo%20da%20velha.py) | Jogo para dois jogadores com interface gráfica (Tkinter) |
| [Quiz](Exerc%C3%ADcios/quiz.py) | Perguntas e respostas no terminal |

</details>

<details>
<summary><strong>Mundo 1 — Aulas</strong> (9)</summary>

| Aula | Tema |
|---|---|
| [aula006a](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Aulas/aula006a.py) | Tipos primitivos: soma de dois números |
| [aula006b](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Aulas/aula006b.py) | Dissecando uma variável (`isnumeric`, `isalpha`…) |
| [aula008a](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Aulas/aula008a.py) | Módulo `math` (`sqrt`, `floor`) |
| [aula008b](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Aulas/aula008b.py) | Biblioteca externa `emoji` |
| [aula009](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Aulas/aula009.py) | Manipulação de strings |
| [aula010](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Aulas/aula010.py) | Condições: verificar idade do carro (TVDE) |
| [aula010a](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Aulas/aula010a.py) | Condições: exemplo "Box Keys" |
| [aula010b](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Aulas/aula010b.py) | Condições: cálculo de nota |
| [aula011](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Aulas/aula011.py) | Cores no terminal (ANSI) |

</details>

<details>
<summary><strong>Mundo 1 — Desafios</strong> (35)</summary>

| # | Desafio | # | Desafio |
|---|---|---|---|
| [001](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des001.py) | Olá, Mundo | [019](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des019.py) | Sorteio de um nome |
| [002](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des002.py) | Respondendo ao usuário | [020](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des020.py) | Ordem de apresentação (`shuffle`) |
| [003](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des003.py) | Somando dois números | [021](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des021/des021.py) | Tocar um MP3 (`python-vlc`) |
| [004](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des004.py) | Soma com mensagem formatada | [022](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des022.py) | Analisador de nomes |
| [005](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des005.py) | Antecessor e sucessor | [023](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des023.py) | Separando dígitos |
| [006](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des006.py) | Dobro, triplo e raiz quadrada | [024](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des024.py) | Cidade começa com… |
| [007](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des007.py) | Média aritmética | [025](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des025.py) | Procurar "Silva" no nome |
| [008](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des008.py) | Conversor de medidas | [026](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des026.py) | Ocorrências de uma letra |
| [009](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des009.py) | Tabuada | [027](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des027.py) | Primeiro e último nome |
| [010](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des010.py) | Conversor de moedas | [028](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des028.py) | Jogo de adivinhação |
| [011](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des011.py) | Tinta por m² | [029](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des029.py) | Radar eletrônico |
| [012](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des012.py) | Desconto de produto | [030](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des030.py) | Par ou ímpar |
| [013](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des013.py) | Aumento de salário | [031](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des031.py) | Preço da passagem |
| [014](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des014.py) | Celsius para Fahrenheit | [032](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des032.py) | Ano bissexto |
| [015](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des015.py) | Aluguel de carros | [033](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des033.py) | Maior e menor de três valores |
| [016](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des016.py) | Porção inteira (`trunc`) | [034](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des034.py) | Aumento por faixa salarial |
| [017](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des017.py) | Hipotenusa (`hypot`) | [035](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des035.py) | Retas formam triângulo? |
| [018](Gustavo%20Guanabara%20Python/MUNDO%20-%2001/Desafios/des018.py) | Seno, cosseno e tangente | | |

</details>

<details open>
<summary><strong>Mundo 2 — Exercícios</strong> (17 de 36)</summary>

Aula: [aula012a](Gustavo%20Guanabara%20Python/MUNDO%20-%2002/AULAS/aula012a.py) — condições aninhadas · Extra: [main.py](Gustavo%20Guanabara%20Python/MUNDO%20-%2002/EXERC%C3%8DCIOS/main.py) — primeira interface com Tkinter

| # | Exercício | Estado |
|---|---|---|
| [036](Gustavo%20Guanabara%20Python/MUNDO%20-%2002/EXERC%C3%8DCIOS/ex036.py) | Financiamento de imóvel | ✅ |
| [037](Gustavo%20Guanabara%20Python/MUNDO%20-%2002/EXERC%C3%8DCIOS/ex037.py) | Conversor de bases (binário, octal, hexadecimal) | ✅ |
| [038](Gustavo%20Guanabara%20Python/MUNDO%20-%2002/EXERC%C3%8DCIOS/ex038.py) | Comparando números | ✅ |
| [039](Gustavo%20Guanabara%20Python/MUNDO%20-%2002/EXERC%C3%8DCIOS/ex039.py) | Alistamento militar | ✅ |
| [040](Gustavo%20Guanabara%20Python/MUNDO%20-%2002/EXERC%C3%8DCIOS/ex040.py) | Média escolar com presença | ✅ |
| [041](Gustavo%20Guanabara%20Python/MUNDO%20-%2002/EXERC%C3%8DCIOS/ex041.py) | Categorias de natação | ✅ |
| [042](Gustavo%20Guanabara%20Python/MUNDO%20-%2002/EXERC%C3%8DCIOS/ex042.py) | Classificação de triângulos | ✅ |
| [043](Gustavo%20Guanabara%20Python/MUNDO%20-%2002/EXERC%C3%8DCIOS/ex043.py) | IMC de várias pessoas | ✅ |
| [044](Gustavo%20Guanabara%20Python/MUNDO%20-%2002/EXERC%C3%8DCIOS/ex044.py) | Formas de pagamento | ✅ |
| [045](Gustavo%20Guanabara%20Python/MUNDO%20-%2002/EXERC%C3%8DCIOS/ex045.py) | Pedra, papel e tesoura | ✅ |
| [046](Gustavo%20Guanabara%20Python/MUNDO%20-%2002/EXERC%C3%8DCIOS/ex046.py) | Contagem regressiva | ✅ |
| [047](Gustavo%20Guanabara%20Python/MUNDO%20-%2002/EXERC%C3%8DCIOS/ex047.py) | Números pares | ✅ |
| [048](Gustavo%20Guanabara%20Python/MUNDO%20-%2002/EXERC%C3%8DCIOS/ex048.py) | Soma dos ímpares múltiplos de 3 | ✅ |
| [049](Gustavo%20Guanabara%20Python/MUNDO%20-%2002/EXERC%C3%8DCIOS/ex049.py) | Tabuada com `for` | ✅ |
| [050](Gustavo%20Guanabara%20Python/MUNDO%20-%2002/EXERC%C3%8DCIOS/ex050.py) | Soma dos números pares | ✅ |
| [051](Gustavo%20Guanabara%20Python/MUNDO%20-%2002/EXERC%C3%8DCIOS/ex051.py) | Progressão aritmética | ✅ |
| [052](Gustavo%20Guanabara%20Python/MUNDO%20-%2002/EXERC%C3%8DCIOS/ex052.py) | Número primo | ✅ |
| [053](Gustavo%20Guanabara%20Python/MUNDO%20-%2002/EXERC%C3%8DCIOS/ex053.py) | Em desenvolvimento | 🚧 |

</details>

## Convenções

| Tema | Padrão |
|---|---|
| **Commits** | [Conventional Commits](https://www.conventionalcommits.org/pt-br/v1.0.0/) com escopo por etapa: `feat(mundo-02): implementar o exercício 045 (pedra, papel e tesoura)` |
| **Tipos** | `feat` novo exercício · `fix` correção · `refactor` reorganização sem mudar o resultado · `style` formatação · `docs` documentação · `chore` manutenção |
| **Versões** | [SemVer](https://semver.org/lang/pt-BR/) com tags `vX.Y.Z` e [Releases](https://github.com/marloon-dev/Python/releases): MINOR a cada bloco de exercícios, MAJOR ao concluir um Mundo ou em mudanças incompatíveis |
| **Nomes** | `desNNN.py` (Mundo 1) e `exNNN.py` (Mundo 2+), com três dígitos |
| **Mundo 2+** | Cada exercício começa com as cores ANSI e as funções `inicio()` e `fim()` |

## Roadmap

- [x] Mundo 1 — fundamentos ([v1.0.0](https://github.com/marloon-dev/Python/releases/tag/v1.0.0))
- [ ] Mundo 2 — exercícios 053 a 071
- [ ] Mundo 3 — tuplas, listas, dicionários, funções, módulos e tratamento de erros
- [ ] Testes automatizados para os exercícios com lógica reutilizável

## Licença

Distribuído sob a [licença MIT](LICENSE). Os enunciados dos desafios pertencem ao [Curso em Vídeo](https://www.cursoemvideo.com/).

---

<div align="center">

Feito por **[Marlon](https://github.com/marloon-dev)** · [LinkedIn](https://www.linkedin.com/in/marloon-dev/)

</div>
