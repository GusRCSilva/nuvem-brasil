# Convenções do Monorrepo

Este documento descreve como o repositório é organizado e as regras que todos devem seguir.

## Estrutura de diretórios

```
/
├── README.md                     ← Visão geral do repositório
├── Nuvem Brasil/                 ← Documentação central
├── apps/                         ← Aplicações (futuro)
├── infra/                        ← Infraestrutura como código (futuro)
├── libs/                         ← Bibliotecas compartilhadas (futuro)
└── .github/                      ← Workflows e templates (futuro)
```

## Nomenclatura de arquivos e pastas

| Onde | Regra | Exemplo |
|---|---|---|
| Documentação | português, PascalCase com hífen | `Guia-do-Projeto.md` |
| Código (fase inicial) | inglês, kebab-case | `user-service.ts` |
| Código (futuro) | português, kebab-case | `servico-de-usuario.ts` |
| README | sempre `README.md` (exigência do GitHub) | `README.md` |

## Língua

- **Documentação:** português brasileiro com acentos, cedilha e caracteres Unicode
- **Código:** inglês inicialmente; a meta é migrar tudo para português
- **Commits:** português, descrevendo *o que* e *por que* foi feito

## Documentação

Cada pasta deve ter um `README.md` que funciona como índice. Arquivos de conteúdo usam hífen nos nomes.

## Automação e testes

Fluxos de funcionalidades são descritos em [BDD.md](Automacao/BDD.md). Cada cenário documentado pode originar testes em múltiplos níveis:

- **Unitário:** verifica uma função ou método isolado
- **Integração:** verifica a comunicação entre componentes
- **E2E:** verifica o fluxo completo do ponto de vista do usuário
