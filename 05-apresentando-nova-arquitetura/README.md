# Apresentando nova arquitetura

O propósito deste projetinho é praticar a criação de apresentações, 
_pitches_ e diagramas.

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

## Passos

Eu comecei tentando criar um diagrama no Excalidraw onde eu 
senti falta de componentização. Esse site me parece bom para 
expressar ideias bem rápido, mas não para apresentações mais sérias.

Tentei usar o Figma FigJam, mas possui o mesmo conceito...

O próximo passo seria usar o Figma Design para desenhar um diagrama com 
componentização e ícones SVG.
