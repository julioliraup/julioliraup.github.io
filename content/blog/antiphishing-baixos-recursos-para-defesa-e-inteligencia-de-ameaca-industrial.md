Title: Antiphishing (AT) - Baixos recursos para defesa e inteligencia de ameaça industrial
Date: 2026-05-18 08:00
Category: Phishing, CTI
header_image: /static/antiphishing-1.gif 

# FAZER MUITO COM POUCO GUARDE BEM ESSA FRASE

Durante a 2° Guerra mundial, a União das Repúblicas Socialistas Soviéticas (URSS) conseguiu superar a tática empregada pelo exercito nazista que até então era invicta utilizando 3 táticas principais, mas essa frase fala sobre a segunda e principal tática, a que ocasionou a virada naquele cenário.

A tática do **contra-ataque**, em cidades já dominada, foram definidos grupos militares que o unico papel seria sabotar o inimigo, cortar comunicação, e enfraquecer a estabilidade.

Eram grupos guerrilheiro, foram decisivo para o fim do Nazismo, não tinham nem se quer uma arma, mas seu papel era apenas sabotar.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7zW6nilcKlY?si=KnKqcFQ1YFkQOMi8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

No decorrer da história se passaram vários cenários que se repetiam isso, o emprego de forças menores e distribuídas em ataques decisivos que causaria efeito borboleta, ocasionando a vitória do grupo menos favorecido militarmente e na URSS apesar da inferioridade tecnologica e militar, havia uma superioridade tática.

## Tecnologia de guerra

Não é de hoje que a criatividade em uso para ataques corporativos também são empregadas, se lembrarmos dos patronos, vemos kevin Mitnick revirando lixo e conseguindo informações preciosíssimas. Deixando um sinal claro, em cenário onde háproteção, o humano será o fator decisivo de fraqueza.

Com o avanço da internet também foram avançando os ataques e hoje, um problema central desvalorizado é o Phishing.

> **Phishing**: Softwares que se passam por legítimos a fim de obter informações sensíveis ou ser vetor de entrada de ataque.

Antes dos super ataques que colapsa toda a corporação, são feitos sucessões por vezes pacientemente de ataques desse tipo. A negligencia desse ataque por vezes faz com que se avance ao próximo passo.

E é  nesse ponto que quero falar.

## Antiphishing

Notando essa necessidade no trabalho, notei que soluções corporativas cumprem bem o papel, mas  geralmente o engessamento permite que as brechas sejam desencadeadas em efeito cascata, sem a garantia de autonomia para o incremento de vetores de ameaças agil o suficiente, e por vezes ignorando domínios recentes considerados como phishing. Além de serem soluções caríssimas e de altíssimo consumo de recursos.

Então observando APIs públicas, repositórios e plataformas, desenvolvi o Antiphishing: Conjunto de regras para Suricata (NDR/IDS/IPS), contendo as ameaças, com informações detalhadas da origem da URL maliciosa. E com ela, desenvolvi também uma API para que outros possam se basear e contribuir, inclusive eu mesmo.

Agora diáriamente e em certos intervalos de horas, a lista é atualizada e disponibilizada gratuitamente com um hardware homelab, possível ser feito a atualização e o controle até mesmo em VPS de baixo processamento. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/8P7MsLDZDwI?si=nyj5EQNe3kDGk_Vi" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Antiphishing → CTI

Com a regra, a API, desenvolvi também um portal também atualizado dinamicamente por cada regra, ele incrementa um visual para as informações valiozíssimas da API.

Em alguns casos além do vetor de ameaça, é possível obter informações de propriedade do domínio, Whois, IP, ASN, geo localização, código de resposta, tudo isso de graça e auditável e com hardware de baixo recurso.

Dado a apresentação, faço a reflexão que em certos pontos, precisamos construir soluções criativamente no combate ao ciber crime. Quantas vezes não responsabilizamos a vítima pelo ataque? Mas é possível mudar esse cenário com o que já temos, claro que não descarta análise aprofundada de trafego com controle de informações e configurações política de prevenções a vazamentos. Mas é possível avançar muito mais que nosso inimigo e aproveitar recursos para a nossa superioridade tática.

**Por fim, esse projeto é independente, estamos falando em baixo recurso, por mais que não precise de muito. Agora não temos nada, estamos usando o github pages, com o action, e recursos homelab.**

**Então aceitamos doações, nós ainda precisamos de uma VPS ao invés do meu PC, de um domínio, de um dinheiro para conseguir utilizar APIs interessantes de CTI que não autoriza varrer informações automáticamente como planejamos, isso implementará melhorias na API e no dashboard**

**Doe ao PIX: 08650081401 (Meu CPF 🤨), ou me contacte jul10l1r4@disroot.org**
