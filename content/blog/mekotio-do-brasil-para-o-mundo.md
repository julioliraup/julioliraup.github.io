Title: Mekotio - Malware voltado para instituições bancárias: Do Brasil para o mundo
Date: 2024-08-01 19:30
Category: RAT
header_image: /static/mekotio.jpg 
> Aqui haverá alguns termos técnicos, evitarei aportuguesar para que termos não conhecidos possam ser descobertos e quem sabe se tornem um novo aprendizado para você

# Objetivo dos malwares

Esses dias, me peguei lembrando de umas matérias do Fantástico, logo que surgiram os vírus, há alguns anos tinha viralizado e virado meme, pela forma que eram tratadas essas matérias. Os "arrombadores digitais", inclusive vale a pena ver (para tentar fazer esse assunto não ser tão assustador).

Lembrei especificamente de como funcionavam os vírus, também da lenda que rolava antigamente que dizia: os vírus são escritos por empresas que fazem antivírus. Resumidamente, os vírus geravam confusões, abriam e fechavam pastas, cuspiam textos, tinha alguns que até achei bem legalzinhos para usar como protetor de tela.

<iframe width="560" height="315" src="https://www.youtube.com/embed/lYKMeZHluKc?si=kaXFcNe85dVBoxQ3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

O objetivo deles também era comercial, causando prejuízo aos usuários, fazendo com que investissem novamente para formatação do sistema ou renegociar as licenças do sistema, além, claro, de justificar a compra dos antivírus (mesmo sendo teoria da conspiração, eu acredito que antes era assim).

Com o avanço da tecnologia, várias plataformas financeiras migraram para a internet, com isso um leque de novos motivos foram incentivando novos ataques (e mais sofisticados). Em todo o mundo, existem ameaças, e o Brasil está sendo, nos últimos anos, porta-voz de novos malwares.

# Origem do malware

O Mekotio foi identificado desde 2018, pesquisadores da ESET identificaram que o Trojan se dá a partir de um golpe de phishing, de formas variadas. Além disso, também foi identificado até agosto de 2020, **38** variantes do malware, como apresenta o gráfico da ESET.

![](https://www.eset.com/fileadmin/ESET/BLOG/mekotio_affected_countries.png)

As modificações variam conforme a diferença em ambientes e versões. Mas, no seu fundamental por ter o objetivo de atingir instituições financeiras, ele mantém sua estrutura de funcionamento genérico, é sobre ela que iremos falar.

Ao enviar um email de phishing de temas variados: por vezes intimação judicial, boletos e afins. A outra fase é um arquivo comprimido com um instalador que teria falsamente o PDF, mas na verdade se trata do Trojan. Como apresenta a imagem tirada do relatório da HP (vamos utilizar essa variante).

![](/static/mekotio-map.png)

Ao executar o AutoHotKey, o script consulta o ipinfo.io - que traz informações detalhadas do IP como geolocalização, AS e hostname - e caso o IP NÃO tenha origem no Brasil, Argentina, Colômbia ou México, então ele não dá seguimento.

Após isso, baixa e extrai um arquivo zip contendo um .dll e um .exe. Então o .dll é modificado para `shfolder.dll` (nome legítimo de uma biblioteca importante do Windows). O arquivo `vmnat.exe` é um programa legítimo usado pela VMware Workstation, ao modificar a `dll`, o programa executará a `.dll` sequestrada (para estudos: [DLL hijacking](https://attack.mitre.org/techniques/T1574)).

Após instalado, o comportamento comum geralmente é exibir pop-ups falsos solicitando informações bancárias, se passando por instituições financeiras.

Com a técnica, torna-se mais difícil o reconhecimento de que há infecção, e por se tratar de um malware silencioso, pode ser que várias máquinas ainda estejam infectadas, mas não há notificação, pois não há nem ciência dela.

Após instalado, o malware extrai informações como:
    + Versão do Windows
    + Configurações de Firewall
    + Configurações de restrições na rede
    + Dados de navegação
    + Screenshots
    + Textos escritos
    + Clipboard
    + Dados bancários

Além de tudo isso, o malware possui um sistema de persistência: fazendo cópias próprias, inicialização conjunta e agendando execução. Essa parte ficaria reservada para os IOCs, nesse caso em específico com tantas variantes, não quis reservar aqui essa sessão.

Veja outras referencias no [MalPedia](https://malpedia.caad.fkie.fraunhofer.de/details/win.Mekotio)
