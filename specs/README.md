# Specs — Fonte de Verdade do Projeto

Este diretório contém todas as especificações do Gusmail no formato **Spec-Driven
Development (SDD)**. Cada spec é um arquivo YAML que descreve formalmente o
que o sistema deve fazer, deixando o *como* para o código.

## Formato

Uma spec é composta por:

- **metadados**: `feature`, `priority` (P0–P3), `category`, `description`
- **KPI links**: referências a indicadores em `specs/kpis/`
- **SLO**: objetivo de latência (p95) e disponibilidade
- **cenários BDD**: blocos `given` (pré-condições), `when` (ações), `then` (asserções)
- **invariantes**: propriedades que nunca podem ser violadas
- **failure_modes**: modos de falha cobertos

## Spec executável

Testes em `tests/from_specs/` são derivados manualmente das specs. O pipeline de
validação (`just spec-validate` + `just spec-list`) garante que toda spec tenha
testes e que todo teste esteja verde.

O schema que valida as specs está em `specs/schema/spec_schema.py` (Pydantic v2).
Ele é a definição canônica do formato e vai evoluir conforme o projeto cresce.

## Convenções

- Specs vivem em `specs/features/<categoria>/<nome>.spec.yaml`
- Testes correspondentes em `tests/from_specs/test_<categoria>_<nome>.py`
- O campo `feature` deve ser único no projeto
