# Topologia de Rede

**Para quem é:** profissionais de infraestrutura e segurança.

**O que você vai aprender aqui:** como a rede é organizada, as regras de tráfego e as conexões entre ambientes.

---

## Em construção

Esta seção será preenchida com:

- Diagrama da topologia de rede
- VPCs e sub-redes por ambiente
- Regras de firewall e grupos de segurança
- Conectividade entre ambientes (VPN, Direct Connect, Peering)
- DNSSEC, certificados e terminação TLS
- Estratégia de IPs públicos e privados

## Padrões esperados

| Aspecto | Padrão |
|---|---|
| Ambientes | desenvolvimento, homologação, produção |
| Isolamento | VPC separada por ambiente |
| Acesso externo | Balanceador de carga como ponto único de entrada |
| Acesso interno | VPN para conexão administrativa |
| Resolução de nomes | DNS privado por ambiente |
