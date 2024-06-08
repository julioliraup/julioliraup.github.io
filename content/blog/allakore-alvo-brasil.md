Title: Allakore - Ataques massivos no Brasil: Ataques direcionados e financeiro
Date: 2024-06-07 18:00
Category: RAT

# Brasil de portas abertas
Sempre se veem notícias de várias organizações cybercriminosas no mundo todo se voltam ao brasil para atacar, por vários motivos.

Entre elas, a subestimação da segurança da informação é um dos motivos mais gritantes que fazem os olhos do cyber crime se voltar ao Brasil. Ataques financeiros são cada vez mais comuns, e até mesmo dos mais simples aos mais complexos.

Mas parando de papo, vamos pra a visão do Allakore

## Filho do AllaSenha
Allakore é uma variante do AllaSenha, ambos são Malwares __tróia de acesso remoto__ (RAT - sigla em inglês), apenas foram feitas algumas mudanças de comportamentos, aumentando a complexidade e fazendo parte do desenvolvimento, e interpretação do virus ser na própria máquina da vítima.

![Gráfico de funcionamento]()

**A analise completa de seu funcionamento é muito bem apresentada por essa matéria do [Hafanglab.io](https://harfanglab.io/en/insidethelab/allasenha-allakore-variant-azure-c2-steal-banking-latin-america/) (Fica a indicação)**. Nessa matéria aqui estarei apresentando o funcionamento a nível de engenharia social e seu comportamento no fluxo da rede.

Resumidamente o Allakore ébaixado, após golpes phishing semelhantes a esse:
![Print de email]()

O link que dá no site `hxxps://notafiscal.nfe-digital[.]digital/nota-estadual/?notafiscal=`, que põe um link de ação, que executa instruções windows:


Executado e faz se parecer com erro PDF, então ele se instala com instruções básicas Bat e Powershell, baixa o python e baixa o seu arquivo compilado usando o script com o seguinte código:

```python3
# Hostnames generation algorithm from BPyCode

def lk():

    import hashlib

    from datetime import date

    try:

        d = date.today()

        wi = d.weekday()

        di = d.day + wi

        l = 'fghijlmnopqrstuvxzwkyjlmnopqabcghjlabcde'[di]

        r = []

        for _ in range(50, 61, 5):

            t = hashlib.sha1(f"{di*wi*_}{l}{wi}{l}{d.month * di*_}{l}{d.year*di*_}".encode()).hexdigest()*10

            r.append(t[:_].replace(t[:di], l).lower())

        return r

    except:

        return [f'google{di}']

```
