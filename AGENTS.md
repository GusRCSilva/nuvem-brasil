# AGENTS.md — Regras para Agentes de Código

Este documento é lido por agentes automatizados ao abrir este repositório.
Siga estas regras rigorosamente. Qualquer violação será revertida por revisão
humana.

## Contexto do paradigma SDD

Gusmail usa **Spec-Driven Development (SDD)**: toda feature é definida primeiro
como uma spec YAML em `specs/features/`. O schema canônico está em
`specs/schema/spec_schema.py`. Testes em `tests/from_specs/` traduzem cada
cláusula `given/when/then` em assertions pytest. O código em `src/gusmail/`
existe exclusivamente para fazer os testes passarem.

Specs são a **fonte de verdade**. Código é descartável e pode ser reescrito
integralmente se uma spec mudar. Testes são a ponte entre spec e código.

## Regras invioláveis

1. **Nunca edite arquivos em `specs/` sem instrução humana explícita.**
   `specs/` é território humano. Agentes só lêem specs; não as criam, editam ou
   removem. A única exceção é se um humano instruir explicitamente "adicione uma
   spec para X" — nesse caso, valide com `just spec-validate` antes de commitar.

2. **Sempre rode `just lint` e `just test` antes de propor qualquer mudança.**
   Nenhum PR ou commit de agente deve quebrar lint ou testes. Se `just lint`
   falhar, corrija antes de commitar.

3. **Se uma spec parecer ambígua ou contraditória, pare e abra uma issue.**
   Não implemente com base em interpretação própria. Descreva a ambiguidade
   na issue e aguarde esclarecimento humano. Implementar a coisa errada é pior
   que não implementar nada.

4. **Commits atômicos com mensagens convencionais.**
   Use prefixos: `feat:`, `fix:`, `test:`, `chore:`, `docs:`, `refactor:`.
   Cada commit deve conter exatamente uma mudança lógica. Não agrupe features
   não relacionadas.

5. **Nunca rode `git push`.**
   A decisão de push é exclusivamente humana. Agentes trabalham em branches
   locais e reportam resultados.

## Fluxo de trabalho padrão

1. Rode `just spec-list` para ver quais specs estão vermelhas (sem teste ou
   com teste quebrado).
2. Escolha uma spec vermelha para trabalhar.
3. Crie uma branch: `git checkout -b agent/<spec-path>`.
4. Leia a spec YAML. Entenda cada cláusula `given/when/then`.
5. Crie ou atualize o teste em `tests/from_specs/test_<cat>_<name>.py`.
6. Implemente o código necessário em `src/gusmail/`.
7. Rode `just lint && just test`.
8. Se tudo passar, faça commit. Se não, corrija e repita.
9. Pare e relate o resultado ao humano. Não faça push.

## Onde NÃO mexer

- `specs/` — território humano (regra 1)
- `.github/` — pipelines de CI são configurados pelo humano
- `compose.yaml` — a menos que o agente precise adicionar uma dependência
  claramente justificada e documentada no commit

## Stack técnica

- **Linguagem:** Python 3.12+
- **Gestor de pacotes:** `uv` (comandos via `uv run` e `uv sync`)
- **Task runner:** `just` (consulte o `justfile` para comandos disponíveis)
- **Web framework:** FastAPI (app em `src/gusmail/api/main.py`)
- **Validação de dados:** Pydantic v2
- **Testes:** pytest + pytest-asyncio
- **Lint/format:** ruff
- **Type-check:** mypy (strict mode)
- **Containers:** podman compose (imagens com prefixo `docker.io/`)
