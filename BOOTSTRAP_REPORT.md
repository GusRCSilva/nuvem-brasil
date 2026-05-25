# BOOTSTRAP_REPORT.md

## Resumo

Bootstrap do projeto Gusmail concluído com sucesso. Todos os 13 passos executados
e validados. Projeto segue o paradigma Spec-Driven Development com stack
FastAPI + Pydantic v2 + uv + just + podman.

## Passos executados

| Step | Commit | Descrição |
|------|--------|-----------|
| 1 | `e164dac` | `feat(bootstrap): initialize uv project with deps` |
| 2 | `85454f6` | `chore(bootstrap): configure ruff, mypy, pre-commit` |
| 3 | `137faef` | `feat(specs): add Pydantic schema and folder structure` |
| 4 | `d051b25` | `feat(specs): add healthcheck example spec` |
| 5 | `4789f8a` | `feat(tools): add spec-validate, spec-list, spec-to-tests CLIs` |
| 6 | `e7a6770` | `feat(api): add FastAPI app with /healthz endpoint` |
| 7 | `f1b1e26` | `test(from_specs): add healthcheck tests derived from spec` |
| 8 | `437cf5e` | `feat(infra): add compose.yaml with postgres, mailhog, redis` |
| 9 | `1ce4aa3` | `feat(dx): add justfile with developer commands` |
| 10 | `adf066d` | `docs: add README` |
| 11 | `0e1116c` | `docs: add AGENTS.md with agent rules` |
| 12 | `b212286` | `docs: add paradigm explanation` |
| fix | `dce7350` | `fix(bootstrap): add SELinux :Z volume label, fix clean recipe` |
| fix | `7dca974` | `fix(bootstrap): update pre-commit revs and add types-pyyaml` |

Total: 14 commits atômicos com mensagens convencionais.

## Decisões de design que merecem revisão humana

1. **`podman-compose` como `uv tool`**: A distribuição Bazzite/Fedora Atomic
   não inclui `podman-compose` por padrão. Para evitar instalação via `dnf`,
   foi instalado como `uv tool install podman-compose`. Isso funciona, mas
   significa que o comando `podman-compose` está em `~/.local/bin/` e não
   no venv do projeto. Um setup script ou o `just bootstrap` poderia
   verificar e instalar automaticamente.

2. **Volume mount com `:Z` no SELinux**: O compose.yaml usa `:Z` no volume
   do postgres para lidar com SELinux no Bazzite. Funciona localmente mas
   pode não ser necessário em outros SOs. O `:z` (minúsculo) seria menos
   restritivo se o volume fosse compartilhado entre múltiplos containers.

3. **`disallow_any_generics = false` no mypy**: O schema das specs usa
   `dict[str, Any]` para os campos `setup`, `action` e `check` porque
   eles contém dados YAML de estrutura variável. Com `disallow_any_generics`
   ativado isso falharia. A alternativa seria usar `dict[str, object]` e
   lidar com casts, mas `Any` é semanticamente mais correto aqui.

4. **`sys.path.insert` nos tools**: Os scripts em `tools/` usam
   `sys.path.insert(0, str(Path(__file__).resolve().parent.parent))` para
   importar de `specs/`. Isso é frágil se a estrutura de diretórios mudar.
   Alternativas: tornar `specs/` parte do pacote Python ou usar editable
   installs.

5. **`ignore_missing_imports = false`**: Mantido como false (default do
   strict). Todos os imports estão tipados. Se uma nova dependência sem
   stubs for adicionada, `mypy` falhará — isso é intencional para manter
   qualidade de tipos.

## Output da validação final

Todos os comandos executados com exit code 0:

```
just clean          → 0
rm -rf .venv        → 0
just bootstrap      → 0 (uv.lock + .venv criados)
just lint           → 0 (ruff check, ruff format, mypy — tudo verde)
just spec-validate  → 0 (1 spec válida)
just spec-list      → 0 (health/healthcheck ✓ green)
just services-up    → 0 (postgres, mailhog, redis rodando)
curl localhost:8025 → mailhog acessível
podman compose ps   → 3 containers Up
just test           → 0 (2 testes passando)
just test-spec      → 0 (2 testes passando)
just run + curl     → 0 ({"status":"ok"} via /healthz)
just clean          → 0 (containers e volumes removidos)
```

## Estrutura final

```
.github/workflows/        ← vazio (placeholder)
.pre-commit-config.yaml
.gitignore
.python-version           ← "3.12"
pyproject.toml
uv.lock
justfile
compose.yaml
README.md
AGENTS.md
BOOTSTRAP_REPORT.md       ← este arquivo
specs/
  README.md
  __init__.py
  schema/
    __init__.py
    spec_schema.py
  features/
    health/
      healthcheck.spec.yaml
  invariants/README.md
  kpis/README.md
  slos/README.md
src/
  gusmail/
    __init__.py
    api/
      __init__.py
      main.py
    core/
      __init__.py
tests/
  conftest.py
  unit/__init__.py
  integration/__init__.py
  from_specs/
    __init__.py
    test_health_healthcheck.py
tools/
  spec_validate.py
  spec_list.py
  spec_to_tests.py
docs/
  paradigm.md
volumes/                  ← gitignored
.venv/                    ← gitignored
```
