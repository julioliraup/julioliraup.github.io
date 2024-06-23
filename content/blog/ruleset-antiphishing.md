Title: Antiphishing: Ruleset livre para a comunidade contra ataques de phishing
Date: 2024-06-23 13:30
Category: blueteam
header_image: /static/antiphishing.gif

Quando falamos em segurança da informação, desenvolvemos um leque de possibilidades e ataques dos mais sofisticados de espionagem corporativa aos mais amadores dos estelionátos que vemos por aí. E defender disso tudo é um desafio grande para o investimento na área (que é pouco), mas vamos ao que interessa.

# Dados sobre ataques no mundo
Segue o apanhado, e tire você mesmo a conclusão sobre ataques phishing:

-   Segundo o Phishing Activity Trends Report da APWG (Anti-Phishing Working Group) de 2021, houve um aumento significativo nos ataques de phishing, com mais de 222.127 ataques únicos registrados em um único trimestre, o que foi um recorde na época.
-   Em 2022, a Microsoft relatou que os ataques de phishing representam 70% dos incidentes de segurança observados.

-   Custo Direto e Indireto:
        O relatório Internet Crime Report de 2021 do FBI estimou que as perdas financeiras devido a phishing e variantes de ataques de engenharia social ultrapassaram US$ 54 milhões em 2020.
-   Impacto em Empresas:
        Em um estudo da Ponemon Institute, o custo médio de uma violação de dados originada por phishing em uma empresa foi estimado em US$ 4,65 milhões. Isso inclui custos diretos, como investigação e resposta, bem como custos indiretos, como perda de negócios e danos à reputação.

Mas apesar de muito esforço os ataques continuam, geralmente as vitimas são pessoas que dão o acesso aos ataques e geram esse prejuizo, como diz Bruce Schneier: O elo mais fraco é o ser humano. Sabendo disso, fica a pergunta: Como instalar um endpoint numa pessoa? 🫠

Já que não dá, então impeçamos que ela caia no golpe nem que queira!

# Rulesets para bloquear phishing
Globalmente existem vários grupos que identificam ameaças de phishing (as vezes são vítimas), e centralizam essas informações em vários agregadores públicos, são listas imensas diárias geradas sob o mesmo tema.

Muitas empresas grandes que trabalham com segurança da informação e procura de ameaças, usam listas como essas e vendem listas e ferramentas que atuam nesse segmento, as vezes com todo um time voltado para isso.

Utilizando essas fontes de informações públicas e globais conseguimos obter uma lista razoavel com ameaças em tempo real. Assim criamos a [Antiphishing](https://github.com/julioliraup/Antiphishing). Para vermos o nível de ação dela, ela possui:
    
-   196639 regras que impedem diretórios em específicos com regras HTTP
-   19068 regras que impedem de consultar o DNS quanto validar o certificado (TLS)

> Mas vale lembrar que isso é no momento que escrevo, ela **atualiza de hora em horas.**

O projeto é livre sob GPLv3, então fique a vontade de aperfeiçoar e nos mandar um PR ou até mesmo editar um projeto com modificações para uso próprio ou em outro projeto.

Para implementar vale estudar um pouco sobre datasets, no projeto tem um pequeno manual em inglês. E é isso, boa sorte!
