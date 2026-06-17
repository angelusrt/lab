# Apresentando nova arquitetura

O propósito deste projetinho é praticar a criação de apresentações, 
_pitches_ e diagramas.

## Passos

Eu comecei tentando criar um diagrama no Excalidraw onde eu 
senti falta de componentização. Esse site me parece bom para 
expressar ideias bem rápido, mas não para apresentações mais sérias.

Tentei usar o Figma FigJam, mas possui o mesmo conceito...

O próximo passo seria usar o Figma Design para desenhar um diagrama com 
componentização e ícones SVG.

Tendo usado o Figma, consegui criar um diagrama muito bonito e profissional 
com componentização - o que facilitará os próximos designs.

Agora, eu vou estudar a criação de slides com o Google Apresentações.

## Arquitetura

Nossa equipe possui uma arquitetura de dados, onde possuímos algumas fontes, como:
- Planilhas do google
- Outros arquivos
- Bancos de dados
- Sites
- APIs

O nosso desejo é estruturar os dados para a geração de visuais no _Power BI_ para 
análise e extração de _insights_. 

Nós não temos necessidade de real-time e funcionamos bem com o dado em batch. Também 
não temos acesso aos dispositivos produtores dos dados diretamente - ao invés, temos 
acesso aos formatos consumíveis (como banco de dados).

Ainda assim, os dados normalmente chegam denormalizados. Para normalizá-los, 
usamos o _DBT_ como o motor de templates de SQL que irão transformar os 
dados em 4 fases:
- Raw
- Staging
- Intermediate
- Marts

Para esse caso, vamos imaginar que temos 3 fontes de dados e 2 produtos de 
visualização.

Fontes:
- A: Planiha
- B: Banco de dados
- C: Planilha

Paineis:
- Painel A
- Painel B

## Apresentação

O propósito desta apresentação é demonstrar a nova arquitetura e vendê-la. 

Vamos imaginar que a antiga arquitetura era muito próxima de um lake/swamp 
onde você extrai e apresenta.

Para vender essa ideia, eu utilizarei a estrutura:
- Solução
- Problema
- Evidência

O problema que temos atualmente é:
- Dados não padronizados
- Valores quantitativos errados 
- Falta de normalização

Evidência:
- Dashboard A mostrou dado X sobre Y, quando na verdade o dado era Z
- No mesmo dashboard, o número B ficou errado, pois um valor foi mal-agregado
- No Dashboard B, um dado estava errado pois não foi normalizado com a fonte C
