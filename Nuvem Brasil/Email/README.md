# Email — Provedor de Email Nuvem Brasil

Serviço de email livre, gratuito e soberano para a população brasileira.

O Email Nuvem Brasil oferece contas de email completas com interface web,
aplicativo mobile e suporte a protocolos padrão (IMAP, SMTP). Inclui integração
nativa com servidor MCP (Model Context Protocol) para operação por agentes de IA.

## Funcionalidades

| Funcionalidade | Descrição |
|---------------|-----------|
| [Cadastro](cadastro.md) | Criação e verificação de conta de email |
| [Login](login.md) | Autenticação, recuperação de senha e 2FA |
| [Inbox](inbox.md) | Caixa de entrada, leitura e pesquisa de emails |
| [Envio](envio.md) | Composição, envio, anexos e rascunhos |
| [Contatos](contatos.md) | Gerenciamento de contatos e grupos |
| [Pastas](pastas.md) | Organização em pastas, filtros e etiquetas |
| [MCP Server](mcp-server.md) | Servidor MCP para operação por agentes de IA |

## Arquitetura

```
┌──────────────────────────────────────────────────┐
│                  Navegador / App                  │
├──────────────────────────────────────────────────┤
│  Frontend Web (PWA)                              │
├──────────────────────────────────────────────────┤
│  API REST / IMAP / SMTP                          │
├──────────────────────────────────────────────────┤
│  Backend (auth, mail storage, search, contacts)  │
├──────────────────────────────────────────────────┤
│  MCP Server (agentic operation)                  │
├──────────────────────────────────────────────────┤
│  Infra (armazenamento em solo brasileiro)         │
└──────────────────────────────────────────────────┘
```

## Princípios

- **Soberania de dados** — armazenamento exclusivo em território brasileiro
- **Criptografia** — TLS em trânsito e criptografia em repouso
- **Sem rastreamento** — zero coleta de dados para publicidade
- **Acessibilidade** — interface compatível com leitores de tela e navegação por teclado
- **Agentes** — servidor MCP nativo permite que IAs operem o email de forma segura
