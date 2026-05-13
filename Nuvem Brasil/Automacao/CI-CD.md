# CI/CD

**Para quem é:** desenvolvedores e DevOps.

**O que você vai aprender aqui:** como funciona a esteira de integração e entrega contínua do projeto.

---

## Princípios

1. **Toda alteração passa por CI** — nenhum código vai para produção sem passar pelos checks automatizados
2. **Build uma vez, deploy em vários lugares** — o artefato gerado na CI é o mesmo promovido entre ambientes
3. **Falha rápido** — os checks mais baratos rodam primeiro

## Pipeline

### Integração Contínua (CI)

Disparada em todo push para qualquer branch:

1. Lint e formatação
2. Testes unitários
3. Testes de integração
4. Build dos artefatos

### Entrega Contínua (CD)

Disparada em push para branches específicas (`main`, `homologacao`):

1. CI passa
2. Deploy automático no ambiente alvo
3. Testes de fumaça (smoke tests)
4. Testes E2E
5. (Opcional) Aprovação manual para produção

## Ferramentas

<!-- Atualizar quando definido -->

| Etapa | Ferramenta |
|---|---|
| CI | *Pendente* |
| CD | *Pendente* |
| IaC | *Pendente* |
