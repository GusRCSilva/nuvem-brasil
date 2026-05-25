# Spec-Driven Development (SDD)

## O que é

Spec-Driven Development é um paradigma de desenvolvimento onde **especificações
formais são a fonte de verdade do sistema**. O código de produção não é o ativo
mais valioso — as specs, KPIs e testes é que são. Código pode ser reescrito
integralmente; o que importa é que os outputs e invariantes definidos pelas
specs continuem sendo respeitados.

## Por que specs como fonte de verdade?

Em desenvolvimento tradicional, o código é a autoridade. Se código e
documentação discordam, o código "está certo". Isso funciona mal com agentes
de IA, que não tem intuição sobre intenção. O SDD inverte a relação:

```
spec (humano) → teste (ponte) → código (descartável)
```

1. **Spec**: um humano define formalmente o que o sistema deve fazer
2. **Teste**: traduz cada cláusula da spec em assertions verificáveis
3. **Código**: existe exclusivamente para fazer os testes passarem

Se o código não passa, está errado e deve ser corrigido. Se a spec está
errada, o humano a corrige e o código é reescrito para atender à nova spec.

## O triângulo spec ↔ teste ↔ código

```
        Spec YAML
       /         \
      v           v
  Teste pytest   Código FastAPI
      \           /
       v         v
        KPI/SLO
```

- **Specs** definem cenários BDD (given/when/then), invariantes e SLOs
- **Testes** são derivados manualmente das specs e falham se o código viola
  qualquer cláusula
- **Código** implementa a lógica necessária para os testes passarem
- **KPIs/SLOs** são métricas de produção que validam se as specs estão sendo
  atendidas no mundo real

## Código descartável

No SDD, código é tratado como descartável. Se uma spec muda radicalmente,
a implementação inteira pode ser jogada fora e reescrita. Isso é uma
**vantagem**, não um problema:

- Elimina o custo de manter código legado por medo de quebrar algo
- Força o código a ser simples e direto ao ponto
- Torna viável experimentar arquiteturas diferentes para a mesma spec
- Permite que agentes de IA reescrevam código sem medo de "perder intenção"

A intenção está na spec, que é estável (ou muda apenas quando o humano decide).

## Como specs são validadas

```bash
just spec-validate   # valida sintaxe YAML contra o schema Pydantic
just spec-list       # mostra status verde/vermelho de cada spec
just test            # roda todos os testes do projeto
```

O pipeline completo: spec YAML → validação de schema → arquivo de teste
correspondente → código de produção → assertions verdes.

## Fontes de inspiração

- **Anthropic** — "Demystifying evals for AI agents": a ideia de que evals
  (testes) são o componente mais importante de qualquer sistema que envolva
  agentes de IA. Sem evals claras, é impossível saber se o agente está
  funcionando.

- **Dave Patten** — "Eval-Driven Agent Development": formalizou a ideia de
  que agentes de IA devem ser desenvolvidos guiados por avaliações
  automatizadas, não por revisão manual de código.

- **Gojko Adzic** — sobre Spec-Driven Development: a prática de usar
  especificações executáveis como fronteira entre negócio e implementação,
  popularizada via Specification by Example e BDD.

## Implicações para agentes

Agentes de código que trabalham neste repositório devem:

1. Ler a spec relevante antes de tocar no código
2. Criar ou atualizar testes derivados da spec
3. Implementar código até que `just test` passe
4. Rodar `just lint` antes de commitar
5. Nunca editar specs sem instrução humana explícita

O contrato é: specs são input humano, código é output de agente, testes são
a verificação de que a tradução foi correta.
