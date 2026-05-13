# Guia para Desenvolvedores

**Para quem é:** desenvolvedores que vão escrever código neste repositório.

**O que você vai aprender aqui:** como configurar o ambiente, onde encontrar cada coisa e como contribuir.

---

## Pré-requisitos

<!-- Atualizar com as ferramentas reais do projeto -->

- Git
- Linguagem/framework principal: *Pendente*
- Gerenciador de pacotes: *Pendente*
- Docker (recomendado)

## Setup inicial

```bash
git clone <url-do-repositorio>
cd nuvem-brasil
# comandos de setup (pendente)
```

## Onde encontrar o quê

| Pasta | Conteúdo |
|---|---|
| `Nuvem Brasil/` | Documentação e cenários BDD |
| `apps/` | Código das aplicações |
| `infra/` | Infraestrutura como código |
| `libs/` | Bibliotecas compartilhadas |

## Fluxo de trabalho

1. Escolha uma issue ou tarefa
2. Crie um branch a partir de `main`
3. Escreva o cenário BDD primeiro (veja [BDD.md](../Automacao/BDD.md))
4. Implemente o código
5. Escreva os testes referentes aos cenários
6. Abra um pull request

## Convenções de código

<!-- Atualizar com as convenções reais -->

- Seguir o estilo definido nas configs de linter do projeto
- Commits em português, descritivos
- Testes obrigatórios para qualquer funcionalidade nova
