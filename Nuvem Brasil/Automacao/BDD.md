# BDD — Cenários de Comportamento

**Para quem é:** desenvolvedores, QA, analistas de negócio e qualquer pessoa que queira descrever como o sistema deve se comportar.

**O que você vai aprender aqui:** como escrever cenários BDD em Markdown que podem ser usados para gerar testes automatizados em diferentes níveis.

---

## Por que BDD em Markdown?

- **Linguagem natural** — qualquer pessoa consegue ler e escrever
- **Independente de ferramenta** — não exige Gherkin, Cucumber, ou parser específico
- **Rastreável** — cada cenário vira um ou mais testes
- **Versionado** — fica no repositório junto com o código

## Formato

Cada fluxo é descrito em um arquivo Markdown separado, seguindo esta estrutura:

```markdown
# Fluxo: Nome do Fluxo

**Para quem é:** [público-alvo do fluxo]

## Contexto
Pré-condições que devem ser verdade para o cenário acontecer.

## Cenário: Nome do Cenário

- **Dado que** [condição inicial]
- **Quando** [ação do usuário ou do sistema]
- **Então** [resultado esperado]

## Cenário: Nome de Outro Cenário

- **Dado que** [condição inicial]
- **E** [outra condição]
- **Quando** [ação]
- **Então** [resultado]
- **E** [outro resultado]

## Verificações por nível

- [ ] **Unitário:** o que o teste unitário precisa cobrir
- [ ] **Integração:** o que o teste de integração precisa cobrir
- [ ] **E2E:** o que o teste ponta-a-ponta precisa cobrir
```

## Exemplo

```markdown
# Fluxo: Criação de Usuário

**Para quem é:** cidadão que acessa o sistema pela primeira vez.

## Contexto
O visitante está na página inicial e clica em "Criar conta".

## Cenário: Cadastro com sucesso

- **Dado que** o visitante está no formulário de cadastro
- **Quando** ele preenche todos os campos obrigatórios com dados válidos
- **E** clica em "Criar conta"
- **Então** o sistema cria o usuário
- **E** redireciona para a página de confirmação
- **E** envia um e-mail de boas-vindas

## Cenário: Cadastro com e-mail duplicado

- **Dado que** existe um usuário com o e-mail "joao@exemplo.com"
- **Quando** um novo visitante tenta cadastrar com o mesmo e-mail
- **Então** o sistema exibe a mensagem "Este e-mail já está cadastrado"
- **E** não cria o usuário

## Verificações por nível

- [ ] **Unitário:** validação de formato de e-mail
- [ ] **Unitário:** regra de unicidade de e-mail
- [ ] **Integração:** fluxo de criação + persistência no banco + disparo de e-mail
- [ ] **E2E:** abertura do formulário, preenchimento, envio e confirmação na interface
```

## Onde armazenar

Cada fluxo fica em um arquivo dentro de uma pasta `Fluxos/` ao lado da funcionalidade que descreve. Exemplo:

```
Nuvem Brasil/
├── Fluxos/
│   ├── Criacao-de-Usuario.md
│   ├── Autenticacao.md
│   └── Recuperacao-de-Senha.md
```

## Checklist de qualidade

- [ ] O cenário descreve um comportamento observável
- [ ] "Dado" estabelece estado inicial (não ações)
- [ ] "Quando" é uma ação única
- [ ] "Então" é verificável
- [ ] Evita detalhes de implementação (ex: "clica no botão X" ao invés de "envia POST /api/users")
