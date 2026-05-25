# Gusmail

Servidor de e-mail desenvolvido sob **Spec-Driven Development (SDD)**: specs YAML são
a fonte de verdade do sistema. O código é implementado para fazer as specs passarem,
e os testes são derivados diretamente das specs.

## Paradigma

Toda feature começa como um arquivo YAML em `specs/features/`. O schema Pydantic
(`specs/schema/spec_schema.py`) valida a estrutura. Testes manuais em
`tests/from_specs/` traduzem cada cláusula `given/when/then` em assertions pytest.
O pipeline `just spec-validate → just spec-list → just test` fecha o ciclo.

Para entender o paradigma em detalhes, leia [`docs/paradigm.md`](docs/paradigm.md).

## Como rodar localmente

```bash
# Setup inicial (só precisa rodar uma vez)
just bootstrap

# Subir dependências (postgres, mailhog, redis)
just services-up

# Validar specs
just spec-validate
just spec-list

# Rodar testes
just test
just test-spec health/healthcheck

# Lint e type-check
just lint

# Rodar servidor de desenvolvimento
just run
```

## Estrutura

```
specs/          ← specs YAML (território humano)
src/gusmail/    ← código da aplicação
tests/          ← testes (unit, integration, from_specs)
tools/          ← CLIs auxiliares (validate, list, etc.)
```

## Contribuindo como humano

1. Escreva ou edite uma spec em `specs/features/<categoria>/<nome>.spec.yaml`
2. Rode `just spec-validate` para validar o formato
3. Crie ou atualize o teste correspondente em `tests/from_specs/`
4. Implemente o código em `src/gusmail/`
5. Rode `just lint && just test`
6. Abra um PR

## Configurando um agente

Agentes de código devem ler [`AGENTS.md`](AGENTS.md) antes de qualquer interação
com este repositório. O documento define regras de escopo, fluxo de trabalho e
territórios proibidos.

## Licença

AGPL v3 — veja [`license.md`](license.md).
