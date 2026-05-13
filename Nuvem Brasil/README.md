# Documentação Nuvem Brasil

**Para quem é este diretório:** desenvolvedores, arquitetos, gestores públicos, cidadãos interessados — qualquer pessoa que queira entender o que é, como funciona e como contribuir com a Nuvem Brasil.

Toda a documentação é escrita em português claro, com explicações para conceitos técnicos. Termos inevitáveis estão no [Glossário](GLOSSARIO.md).

## Conteúdo

| Arquivo / Pasta | O que contém |
|---|---|
| [Guia do Projeto](GUIA-DO-PROJETO.md) | Visão, objetivos, valores e contexto da iniciativa |
| [Glossário](GLOSSARIO.md) | Definições de termos técnicos em linguagem simples |
| [Monorrepo](MONORREPO.md) | Convenções de diretórios, nomeação e fluxo de trabalho |
| [Arquitetura/](Arquitetura/README.md) | Decisões arquiteturais e visão geral do sistema |
| [Infraestrutura/](Infraestrutura/README.md) | Cloud, rede, provedores e topologia |
| [Automação/](Automacao/README.md) | CI/CD, IaC e cenários BDD para testes |
| [Guias/](Guias/README.md) | Guias práticos para diferentes públicos |

## Convenções

Este repositório segue as convenções descritas em [MONORREPO.md](MONORREPO.md). Resumo:

- **Idioma da documentação:** português brasileiro, com acentos e cedilha
- **Idioma do código:** inglês inicialmente, com migração gradual para português
- **Nomes de arquivo:** hífen (`-`) como separador; `README.md` mantido para renderização no GitHub
- **Documentação orientada a cenários:** fluxos descritos em BDD para gerar testes automatizados no futuro (veja [BDD.md](Automacao/BDD.md))
