Title: Golpe do Pedágio Digital: Como não pagar a conta do vilão
Date: 2026-07-02 08:00
Category: Phishing, CTI
header_image: /static/ped.jpg

![](/static/ped.jpg)

Toda vez que o Brasil adota um novo sistema de pagamento ou cobrança automatizada, abre-se uma janela de adaptação, e é justamente nessa janela que o golpe encontra espaço. Foi assim com os primeiros Internet Bankings, foi assim com o PIX, e agora é a vez do pedágio eletrônico *free flow*: carro passa direto pelo pórtico, sem cancela, e a cobrança some no ar até você descobrir, dias depois, que devia alguma coisa pra alguém. Sabe aquela sensação de receber uma multa de trânsito e pensar "mas eu nem saí de casa esse fim de semana"? É exatamente essa dúvida que os golpistas estão explorando agora.

Aqui haverá alguns termos técnicos, evitarei aportuguesar para que termos não conhecidos possam ser descobertos e quem sabe se tornem um novo aprendizado para você. Mas vamos ao que interessa.

## O terreno perfeito pra confusão

O *free flow* em si não é o vilão, é até um avanço: reduz fila e emissão parada no trânsito. Só que o modelo de cobrança envolve dezenas de concessionárias diferentes, cada uma responsável por um trecho de rodovia, e nem todo mundo tem TAG. Pra cobrir essa lacuna existe o Pedágio Digital, o site/app oficial onde quem não tem TAG consulta e paga as passagens registradas em rodovias sob concessão da Motiva e da Econoroeste. É justamente esse serviço de consulta, e não uma concessionária qualquer, que está sendo clonado no golpe que vou mostrar aqui.

EcoRodovias, Way-262, a estatal gaúcha EGR e a ANTT (agência federal que regula o setor) também já saíram publicamente alertando sobre criminosos se passando por elas, e o G1, na coluna Fato ou Fake, já confirmou como fake pelo menos um desses sites clonados usados especificamente pra aplicar golpe do Pix em cima do free flow. O roteiro se repete quase igual em cada caso: e-mail ou mensagem de WhatsApp avisando de um débito, botão de "regularizar agora" e uma página clonada pedindo placa, CPF e cartão.

Mas por que um serviço de consulta centralizado como esse facilita tanto o golpe? Justamente por ser o canal que concentra a busca de quem não tem TAG, ele vira o alvo mais óbvio de clonagem: o criminoso não precisa convencer a vítima de que existe um pedágio, ele só precisa convencê-la de que aquele é o canal certo pra consultar e pagar.

No caso que peguei durante o monitoramento de fontes do projeto Antiphishing, o domínio é `ww-brasilrodovias.click`. Nem precisa que o carro tenha passado perto de pedágio nenhum, o sistema gera um "débito" do nada e a pressão de "regularize ou vira multa" faz o resto do trabalho.

## "Paguem Seguro" e o problema de fundo

> **Typosquatting**: técnica de registrar domínios ou nomes de empresa parecidos o suficiente com uma marca legítima pra confundir a vítima, sem precisar comprometer nada tecnicamente.

O destino do dinheiro é onde a coisa fica mais clara: o pagamento vai para uma empresa chamada "Paguem Seguro". A semelhança proposital com uma instituição de pagamento de verdade não é coincidência, é typosquatting aplicado ao nome da empresa, não só ao domínio.

Vale um parêntese: parte do espaço que esse golpe encontra pra crescer vem do próprio modelo de concessão fragmentado que citei acima. Quando existem dezenas de "empresas oficiais" diferentes cobrando por rodovia, fica trivial inventar mais uma no meio da multidão. Não é debate técnico, é debate de política pública, mas fica o registro.

<blockquote class="tiktok-embed" cite="https://www.tiktok.com/@i.sundaysik/video/7482836338610277687" data-video-id="7482836338610277687" style="max-width: 605px;min-width: 325px;" > <section> <a target="_blank" title="@i.sundaysik" href="https://www.tiktok.com/@i.sundaysik?refer=embed">@i.sundaysik</a> Respondendo a @Canal Só por causa <a target="_blank" title="♬ original sound - Jordan" href="https://www.tiktok.com/music/original-sound-7250560292583787290?refer=embed">♬ original sound - Jordan</a> </section> </blockquote> <script async src="https://www.tiktok.com/embed.js"></script>

> Pardal do mal

Praticamente não existe nenhuma técnica de exploração de sistema nesse golpe, é tudo manipulação psicológica em cima de infraestrutura nova e barata de montar (para estudos: o comportamento se encaixa no que o MITRE ATT&CK cataloga como [T1657 – Financial Theft](https://attack.mitre.org/techniques/T1657/), técnica incluída recentemente no framework justamente pra cobrir fraude via engenharia social sem invasão técnica de fato). É por isso que antivírus tradicional de endpoint não pega nada aqui: não tem malware rodando em lugar nenhum, só um formulário bem feito hospedado num domínio novo.

## O prejuízo incalculável

O resultado é sempre a mesma história: prejuízo que ninguém sabe medir direito, porque a maior parte das vítimas nem chega a denunciar. Já reportei o domínio ao provedor, mas segurança, na prática, só vira prioridade de alguém depois que essa pessoa já perdeu dinheiro. Quantas vezes não responsabilizamos a vítima pelo golpe, em vez de olhar pra fragilidade do sistema que permitiu ele existir?

O perfil oficial do Pedágio Digital, a plataforma clonada nesse caso, está cheio de gente reclamando de cobrança indevida nos comentários, sinal de que o golpe está ativo e pegando gente de verdade.

![IMAGEM: Print do perfil oficial do Pedágio Digital](/static/print-ped-perfil.png)

![IMAGEM: Print dos comentários de usuários relatando terem caído no golpe ou desconfiando da cobrança](/static/print-ped-post.png)

## O que a gente pode fazer com pouco

Esse domínio foi identificado durante o monitoramento diário das fontes utilizadas pelo [Antiphishing](https://julioliraup.github.io/AT/signature.html?sid=6013394), o projeto que venho desenvolvendo: regras Suricata atualizadas de hora em hora, cruzando fontes como Phishstats e Openphish e convertendo isso em detecção pronta pra usar. Essa inteligência é publicada automaticamente e fica disponível de graça pra qualquer um. Se quiser entender a arquitetura por trás, de onde vêm os dados e como as regras são geradas, já detalhei tudo [nesse outro artigo sobre a Ruleset Antiphishing](https://julioliraup.github.io/antiphishing-ruleset-livre-para-a-comunidade-contra-ataques-de-phishing.html).

Na prática, quem já usa a ruleset estava protegido contra esse domínio bem antes de eu sentar pra escrever este post. Código aberto no [GitHub](https://github.com/julioliraup/Antiphishing) pra quem quiser auditar, contribuir ou rodar na própria rede.

Se você não usa a ruleset, nem nenhuma equivalente, fica a dica de sempre: desconfie de cobrança urgente por WhatsApp, SMS ou e-mail, nunca clique no link, digite o endereço da concessionária manualmente, e complemente com XDR, antivírus atualizado e um bom NG-Firewall. Mas o detector mais barato e mais rápido continua sendo os comentários nas redes sociais oficiais, geralmente é lá que a informação circula primeiro.

Também realizei um estudo do vetor em si, e notei a presença de API, concentradores de comportamento e endpoints vulneráveis. Não vou detalhar nada disso agora, o site permanece no ar e entrar em detalhe técnico aqui abriria margem pra exposição de vítimas. Fica registrado que existe mais profundidade nesse vetor do que um phishing genérico costuma ter, e assim que o domínio cair, trago os detalhes.

E é isso, boa sorte!

## Referências

- G1, Fato ou Fake: [É #FAKE site que imita página para pagamento de pedágio free flow e dá golpe do Pix](https://g1.globo.com/fato-ou-fake/noticia/2026/04/24/e-fake-site-que-imita-pagina-para-pagamento-de-pedagio-free-flow-e-da-golpe-do-pix.ghtml)
- [Perguntas frequentes do Pedágio Digital](https://www.pedagiodigital.com/perguntas-frequentes)

## IOC

- Domínio: `ww-brasilrodovias.click`, subdominio: `www`
- Empresa usada como isca no pagamento: "Paguem Seguro" (typosquatting), futuramente posso analisar o CNPJ mas aí é OSINT
- Regra Antiphishing (Suricata): [SID 6013394](https://julioliraup.github.io/AT/signature.html?sid=6013394)
- Ruleset completa: [github.com/julioliraup/Antiphishing](https://github.com/julioliraup/Antiphishing)

