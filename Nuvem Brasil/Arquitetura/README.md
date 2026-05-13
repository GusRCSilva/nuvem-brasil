# Arquitetura

**Para quem é esta pasta:** arquitetos, desenvolvedores seniores e qualquer pessoa que queira entender como o sistema é estruturado.

## Conteúdo

| Arquivo | O que contém |
|---|---|
| [Visão Geral](Visao-Geral.md) | Diagramas e descrição dos componentes principais |
| [Decisões (ADRs)](Decisoes-ADRs.md) | Registro de decisões arquiteturais com contexto e alternativas |

## Princípios arquiteturais

- **Separação de responsabilidades** — cada componente tem um propósito claro
- **Resiliência** — falhas são esperadas e tratadas graciosamente
- **Observabilidade** — tudo que roda pode ser monitorado e auditado
- **Portabilidade** — evitar dependências que prendam a um único provedor
