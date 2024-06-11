Title: Allakore - Ataques massivos no Brasil: direcionados ao financeiro
Date: 2024-06-11 19:30
Category: RAT
header_image: /static/cx-eletronico.gif 
> Aqui haverão alguns termos técnicos, evitarei aportuguesar para que termos não conhecidos possam ser descoberto e quem sabe se torne um novo aprendizado pra você

# Brasil de portas abertas
Sempre se veem notícias de várias organizações cybercriminosas no mundo todo se voltam ao brasil para atacar, por vários motivos.

![Moneey](https://i.pinimg.com/originals/12/69/d3/1269d30ef08226057ca8ab4202273652.gif)

Entre elas, a subestimação da segurança da informação é um dos motivos mais gritantes que fazem os olhos do cyber crime se voltar ao Brasil. Ataques financeiros são cada vez mais comuns, e até mesmo dos mais simples aos mais complexos.

Mas parando de papo, vamos pra a visão do Allakore

## Filho do AllaSenha
Allakore é uma variante do AllaSenha, ambos são Malwares __tróia de acesso remoto__ (RAT - sigla em inglês), apenas foram feitas algumas mudanças de comportamentos, aumentando a complexidade e fazendo parte do desenvolvimento, e interpretação do virus ser na própria máquina da vítima.

![Gráfico de funcionamento](https://harfanglab.io/medias/2024/05/fig1-update1-1440x448.png)

**A analise completa de seu funcionamento é muito bem apresentada por essa matéria do [Hafanglab.io](https://harfanglab.io/en/insidethelab/allasenha-allakore-variant-azure-c2-steal-banking-latin-america/) (Fica a indicação)**. Nessa matéria aqui estarei apresentando o funcionamento a nível de engenharia social e seu comportamento no fluxo da rede.

Resumidamente o Allakore é baixado, após golpes phishing semelhantes a esse:

![Print de email](https://harfanglab.io/medias/2024/05/mailexample-480x389.png.webp)

O link que dá no site `hxxps://notafiscal.nfe-digital[.]digital/nota-estadual/?notafiscal=`, que põe um link de ação, que executa instruções windows, responsável por baixar o python (diretamente do site oficial) e executar instruções de instalação obfuscada em base64

Após isso estará instalado, e segue a analise resumida do seu funcionamento

# Allakore C2

Primeiramente o script base64 criará um _domain generation algorithm (DGA)_ que servirá para a comunicação de comando e controle (remotamente), o DGA segue essa estrutura nesse padrão de subdomínio `<DGA>.brazilsouth.cloudapp.azure[.]com`, além disso o software tentará chutar um range de 10 portas, até encontrar o padrão do servidor c2 (ref: botnet).

# Funcionamento

Ele comprime arquivos e executa na memória instruções de permanência modificando as chaves Reg e injetando DLLs. Além disso é executado em Delphi um script responsável por carregar o agente ao ser disparado.

Sempre que executado o script mapeia os diretórios a procura de dados bancários. Após analise, segue as opções mapeadas como comandos remotamente:

```
<|ASS-BLUE-PJ|>
<|ASS-BLUE|>
<|ASS-SANTA|>
<|BB-AMARELO|>
<|BB-AZUL|>
<|BB-PASS6|>
<|BB-PASS8|>
<|BB-PROCURADOR|>
<|BLOQUEAR|>
<|CLOSEKEYBOARD|>
<|DESCO-TKAPP|>
<|DESCO-TKCHAVEIRO|>
<|FECHAR-ANYDESK|>
<|ITAU-SNH-CARTAO|>
<|ITAU-SNH-ENTRADA|>
<|ITAU-TK-APP|>
<|ITAU-TK-CHAVEIRO|>
<|ITAU-TK-SMS|>
<|LIMPAR-TECLAS|>
<|PRINCIPAL|>
<|PUXAR-TECLAS|>
<|QR-CONFIRMADO|>
<|REQUESTKEYBOARD|>
<|SAFRA-DADOS|>
<|SENHA|>Ass: 
<|SICOOB-HEIGTH|>
<|SICREDI-TOKEN-CELULAR|>
<|SICREDI-TOKEN-CHAVEIRO|>
<|START-CAPTURA|>
<|STN-6DG|>
<|STOP-CAPTURA|>
<|TAMANHO|>
<|UNICRED-ASS|>
<|UNICRED-TKN|>
```

Entre esses comandos está o de congelar a tela da vítima para o roubo de confirmações de 2° fator (SMS,OPT e afins), dessa forma se rouba as sessões. Veja a captura de tela:

![Screenshot de roubo de sessão do Allakore](https://harfanglab.io/medias/2024/05/fig6.png.webp)

# Alvo sempre o mesmo

O principal alvo de campanha que usam essa ferramenta são instituição bancários ou até mesmo pequenas empresas que trata de informações de pagamento.

E seu modo de funcionamento utiliza serviços legítimos como os serviços da Azure, que passa credibilidade além de ser altamente replicável e escalável. As funções também possuem tratamentos de erros variádos e em diferentes ambientes, o malware termina se tornando bem sucedido.

# informações úteis de threat intelligence

1. Primeiramente se recebe o email com o link que direciona para: hxxps://notafiscal.nfe-digital[.]digital[ou TLD: .top]/nota-estadual/?notafiscal=<an identifier>
2. Acessa um Webdav: 191.232.38[.]???@80\Documentos (Aqui se baixa os arquivos iniciais vale apena ver que também são dinâmicos, dá uma lida no artigo que citei)
3. Baixa o python do site oficial: https://www.python.org/ftp/python/3.10.0/python-3.10.0-embed-win32.zip
4. Baixa o loader em: hxxps://raw.githubusercontent[.]com/alexiadarocha195267/rp/raw/main/Execute_dll.zip
5. Após isso se comunica com o servidor _c2_ em <DGA>.brazilsouth.cloudapp[.]azure[.]com
Por fim após analise dos dados e das funções vistas, se concluiu que os dados que são capturados são dos bancos em específicos:
   - Banco do Brazil;
   - Bradesco;
   - Banco Safra;
   - Itaú Unibanco;
   - Sicoob;
   - Caixa Econômica Federal.

## IOCs

```sha256
# Files
f848c0f66afc7b5a10f060c1db129529a974ae0ad71a767f7c7793351bb7ca04|Malicious LNK (NotaFiscal.pdf.lnk)
c300749ea44f886be1887b3e19b946efbdbbc3e1bf3e416c78cfbff8d23bf70a|Malicious LNK (NotaFiscal.pdf.lnk)
0d94547a0b8f9795e97e2a4a58b0ece65b4ea4b6e6019cbc96e1c79f373b4587|Malicious LNK (NotaFiscal.pdf.lnk)
d9877dc1ba0f977d100e687da59c216454d27e3988532652ac8f6331debbd071|Malicious LNK (NotaFiscal.pdf.lnk)
a6d995d015c16985b456bcc5cd44377c3e5e5cf72b17771eadc51e1d02a3c6ef|Malicious LNK (NotaFiscal.pdf.lnk)
21e22c4736e7567b198b505ed303c3ca933e0c2d931b886756f6db18a9884a75|Malicious LNK (NotaFiscal.pdf.lnk)
2c1251ae1ec9d417bbbdd1f6ac99baa3f16a7639d0c12cb2883ef8c22c73e58e|Malicious LNK (NotaFiscal.pdf.lnk)
e50bde1e319e699f587d3b5403c487e46deed61cc3f078fe951e7cb9f6896259|Malicious LNK (NotaFiscal.pdf.lnk)
f00cb0603c055c85c7cdf9963d919d527b13013c182dc115ba733d28da57b1d9|Malicious LNK (NotaFiscal.pdf.lnk)
2c53b4dc15882cf22772994d8ed0947e4a8b70aef3a12ab190017b3317c167ea|Malicious LNK (NotaFiscal.pdf.lnk)
46e754727efdc2c891319d25a67ee999a4d8a0b21b0113db08eead42cf51b780|Malicious LNK (NotaFiscal.pdf.lnk)
cd9f5773bd7672a3e09f2d05ef26775e8c7241879d5f4d13c5c5bc1704c49fa1|Malicious LNK (NotaFiscal.pdf.lnk)
8424e76c9a4ee7a6d7498c2f6826fcde390616dc65032bebf6b2a6f8fbf4a535|Malicious LNK (NotaFiscal.pdf.lnk)
1b4f44a00f61b3e0c8cd6c3125f03b6d4897d6ab90c8a6dc899ed96acee80dd6|Malicious LNK (NotaFiscal.pdf.lnk)
4546bc56c85ad2967859dc34b2c84f15891fcd192e86bfc630c49dc8d59e3e71|BPyCode launcher (c.cmd)
40c37bfcc9b0e0d1b3840cb7c751162fec91fe833d4caf4a17bc8b97d53c88b5|BPyCode launcher (c.cmd)
a839dfbe1e7979dbd15ef6c5e472afb3efca044ee8ad27185b01161ce01e4f36|BPyCode launcher (a3.cmd)
610f0ec33603ef4d1fd6530a8f6b0121a4c9cc62fb6fa2ceee8e2f5b2f866e4c|BPyCode launcher (a3.cmd)
c0bf82a3f7807e0c88076e0d500b07e253b106914058b02e112d45eeb6209998|BPyCode launcher (a3.cmd)
6f05d8f85384808036d3c77732b056e2b9cd429587a77b6be3ccdbd4bb558023|BPyCode launcher (a3.cmd)
3962c8a4d0472f91d4be45140eccf661ad6c579319953156dec438dc6a07eeb2|BPyCode launcher (a3.cmd)
b2e1f630c4593830ead91e7f3615d8d5214762dc5a1dd65bef7382d6f6c9f258|BPyCode launcher (a3.cmd)
010d9f1f16c01db5ff37ff9b519d7ecf3be096e00ae597d7bec12b7099b2f852|BPyCode launcher (a3.cmd)
eb2cd71e72ff676d80eb746b961840fea3601d8f6402201d7c0e849a670240ee|BPyCode launcher (a3.cmd)
643563613fb78f88fd90a6cf253ace9e9e6686568fdf6b6d7ec9760667d4d72b|BPyCode
f2db799d892f2a7ac82bfa15826e74d778abdfa153ccafb9db1fdf56a0248a40|BPyCode
d051c0aee007f2a1d0026330719a45e81c726251015837e66cf9348df3bd7210|BPyCode
dd3f1829cc743942d1fc3719c8d8162bc45ca624352ac71f43c08dafd54bbb7f|BPyCode
8a1aba66841ae4b20df95eea8a271538453a76a53596fd3254d47d4d57a3ab3a|BPyCode
3b450994add1e3a206c56a7f8fd28e4132cffb27f3df345e07e8908d7989751f|BPyCode
35329c2fb7a1844576a5defd5d9a7d250d78db51479b2612e3923e18539b0695|BPyCode
19c02c5724622be4eedff95633f3fbaa604449aa50cc0761693bb8adb1e8cf97|BPyCode
5782b9bc96ce5ad011c122496ff0ff0dc08d6444c6d2e98606ada82130d5f21a|BPyCode
6149a3d1cff3afe3ebb9ac091844a3b7db7533aa69801c98d00b19cdb8b18c9e|BPyCode persistence (C:\Users\Public\<filename>.txt)
99d0de52a63e5ff790e468dbb8cd0d5273b51ca3b67b5963c0bdedc3a4f44f12|ExecutorLoader (executor.dll)
3b0eb25ed6c0dff76a613bdcfd20ca1d2f482e3c1739747bf50834ca784e66bb|ExecutorLoader (executor.dll)
19594c51c61fc5fd833ddd0eecb648acebdf4d789b337f00cda0a03efbb1afcf|ExecutorLoader (executor.dll)
7e0051d9221c13a47245359a2cd2804b4d3d9302a321fc8085da1cf1a64bac91|ExecutorLoader (Execute_dll.exe)
b8b3963967232916cd721a22c80c11cd33057bd5629dcfa3f4b03d8a6dbf1403|ExecutorLoader (Execute_dll.exe)
e7aa64726783ec6f7249483e984ae20b31a091a488a3ed0f83c210702c506d20|ExecutorLoader (Execute_dll.exe)
65d86160cd4a08d60ada7fcafb7ed9493bf6dacfa098dba27f7851f1bb8de841|UPX-packed AllaSenha
ac4b4b6cfe4d4e8710384246c008764cdb7547a6c3081e72687fefdf0614c7a5|UPX-unpacked AllaSenha
b152346c2679392d7e15d1cc72a39a21d24e55360c4c1c845ef3524924e93fa9|AllaSenha
7232e3318fdc370e611b2bcbaaec3d58a0d687927714c24dc81fe60767d53a31|AllaSenha
883c49b7c869019951eff94699480a7ecc97c9c45060a15797ecbd5fce060d26|AllaSenha
561e6a42e23d12abe6bba8c98f84c3ba7c45a5df840bfa6fd0dfea803c9b4b7e|AllaSenha
ab3a284ae6e4e466a0715c162cfab85d75522bec48fa25947b16a0891ec2358a|AllaSenha
278897ee9158f9843125bc2e26c14f96c4e79d5fc578b7e5973dc8dc919a3400|AllaSenha
3c89775ae7c35fe3d1ec7e75ac9d4a19959d082d31ab412af243125440ffea6c|AllaSenha

# Domains
nfe-digital[.]online|Possibly malicious and/or associated domain
nfe-digital[.]site|Possibly malicious and/or associated domain

# URls
\\abrir-documento-adobe-reader-1.brazilsouth.cloudapp.azure[.]com@80\Documentos\|WebDAV stager path (on legitimate Azure infrastructure)
\\104.41.57[.]122@80\Documentos\|WebDAV stager path (on legitimate Azure infrastructure)
\\191.235.235[.]69@80\Documentos\|WebDAV stager path (on legitimate Azure infrastructure)
\\4.203.105[.]118@80\Documentos\|WebDAV stager path (on legitimate Azure infrastructure)
\\191.234.212[.]140@80\Documentos\|WebDAV stager path (on legitimate Azure infrastructure)
\\191.233.241[.]96@80\Documentos\|WebDAV stager path (on legitimate Azure infrastructure)
\\191.232.38[.]222@80\Documentos\|WebDAV stager path (on legitimate Azure infrastructure)
\\191.239.116[.]217@80\Documentos\|WebDAV stager path (on legitimate Azure infrastructure)
\\104.41.51[.]80@80\Documentos\|WebDAV stager path (on legitimate Azure infrastructure)
\\191.235.233[.]246@80\Documentos\|WebDAV stager path (on legitimate Azure infrastructure)
\\191.233.248[.]170@80\Documentos\|WebDAV stager path (on legitimate Azure infrastructure)
\\191.239.123[.]241@80\Documentos\|WebDAV stager path (on legitimate Azure infrastructure)
\\191.235.87[.]229@80\Documentos\|WebDAV stager path (on legitimate Azure infrastructure)
\\20.197.250[.]132@80\Documentos\|WebDAV stager path (on legitimate Azure infrastructure)
hxxps://raw.githubusercontent[.]com/marinabarros320168/new/main/Execute_dll.exe|ExecutorLoader staging URL (on legitimate Github infrastructure)
hxxps://raw.githubusercontent[.]com/alexiadarocha195267/rp/raw/main/Execute_dll.zip|ExecutorLoader staging URL (on legitimate Github infrastructure)
hxxp://jucatyo6.autodesk360[.]com/shares/download/file/SHd38bfQT1fb47330c999c2a86b9a6d091b6/dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLnY0Uk5ubHlyU0JXd0hlLXJyZWk0T2c_dmVyc2lvbj0x?bfccc0fd975348c980dd89e57f94815f|Stager for a likely associated and previous variant of BPyCode execution (on legitimate AutoDesk infrastructure)
hxxps://dpsols7.autodesk360[.]com/shares/download/file/SHd38bfQT1fb47330c99c55d44aacebd2ec7/dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLjhZc1hBS2Q2VHNDa0Z1NkZ0Q2tQdHc_dmVyc2lvbj00?b44bb61abebf41d695a4580f072d9b74|Stager for a likely associated and previous variant of BPyCode execution (on legitimate AutoDesk infrastructure)
```

