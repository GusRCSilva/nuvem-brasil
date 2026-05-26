# Nuvem Brasil

**Ferramentas digitais livres para a população brasileira.**

Monorepo open-source que desenvolve ferramentas digitais acessíveis, de baixo
custo e centradas no cidadão — priorizando usabilidade, transparência e
confiança pública.

## Paradigma: Spec-Driven Development (SDD)

Toda feature é definida primeiro como uma spec YAML em `specs/features/`.
O schema canônico está em `specs/schema/spec_schema.py`. Testes em
`apps/<project>/tests/from_specs/` traduzem cada cláusula `given/when/then`
em assertions pytest. O código existe exclusivamente para fazer os testes
passarem.

Para entender o paradigma em detalhes, leia [`docs/paradigm.md`](docs/paradigm.md).

## Estrutura

```
Nuvem Brasil/      ← visão e documentação de produto
apps/              ← implementação de cada projeto
  email-server/    ← provedor de email (FastAPI)
shared/            ← código comum entre projetos
specs/             ← specs YAML organizadas por projeto
tools/             ← CLIs auxiliares (validate, list)
```

## Projetos

| Projeto | Status | Descrição |
|---------|--------|-----------|
| [email-server](apps/email-server/) | em desenvolvimento | Provedor de email livre com servidor MCP nativo |

## Como rodar

```bash
just bootstrap       # setup inicial
just services-up     # sobe postgres, mailhog, redis
just spec-validate   # valida sintaxe das specs
just spec-list       # status verde/vermelho de cada spec
just test            # roda todos os testes
just lint            # lint + type-check
just run             # servidor de desenvolvimento
```

## Contribuindo

1. Escreva ou edite uma spec em `specs/features/<project>/<feature>/<scenario>.spec.yaml`
2. Rode `just spec-validate` para validar o formato
3. Crie ou atualize o teste correspondente em `apps/<project>/tests/from_specs/`
4. Implemente o código em `apps/<project>/src/`
5. Rode `just lint && just test`
6. Abra um PR

Agentes de código devem ler [`AGENTS.md`](AGENTS.md) antes de qualquer
interação com este repositório.

## Licença

AGPL v3 — veja [`license.md`](license.md).
