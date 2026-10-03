# Completando o Framework Scrum: guia visual e aplicação prática

**Autor:** 0Barone  
**Desafio:** Completando o Framework Scrum — DIO  
**Versão de referência:** Scrum Guide 2020  
**Data:** outubro de 2026

## Resumo

Este guia apresenta uma reconstrução autoral do Framework Scrum e o aplica ao produto fictício **EcoCiclo**, uma plataforma para localizar pontos de reciclagem. O conteúdo organiza teoria e prática em quatro camadas: fundamentos empíricos, valores, responsabilidades formais, eventos e artefatos com seus compromissos. Também separa elementos oficiais de práticas opcionais e de conceitos que não pertencem ao Scrum. O objetivo não é decorar um diagrama, mas compreender como cada parte cria transparência, viabiliza inspeção e permite adaptação orientada a valor.

**Palavras-chave:** Scrum; empirismo; Sprint; Product Backlog; agilidade; gestão de produtos.

## 1. Propósito do projeto

Scrum é um framework leve para gerar valor por meio de soluções adaptativas para problemas complexos. Ele não prescreve técnicas detalhadas, ferramentas, cargos organizacionais ou um processo completo de engenharia. Em vez disso, estabelece um conjunto mínimo de responsabilidades, eventos e artefatos que sustenta ciclos frequentes de aprendizado.

Este material foi desenvolvido do zero para o desafio. Não reproduz os slides nem o quadro disponibilizado na aula. A arquitetura visual, as explicações, a classificação dos conceitos e o exemplo EcoCiclo são autorais. As definições normativas foram conferidas no Scrum Guide 2020 e estão referenciadas ao final.

A leitura pode começar pelo mapa geral e seguir pelas relações, em vez de memorizar listas isoladas. Primeiro observe quem assume cada responsabilidade. Depois identifique em qual evento ocorre a inspeção, qual artefato fornece a evidência e qual compromisso orienta a decisão. Por fim, verifique quais valores tornam o comportamento coerente. Essa sequência ajuda a responder não apenas “qual é o elemento?”, mas “que problema ele resolve e como se conecta aos demais?”.

## 2. A base: empirismo e pensamento Lean

Scrum se apoia no **empirismo**: decisões são tomadas com base no que é observado, não apenas no que foi previsto. Também utiliza o pensamento Lean para reduzir desperdício e concentrar energia no essencial.

Os três pilares empíricos são:

- **Transparência:** processo e trabalho precisam ser visíveis para quem executa e para quem recebe seus resultados. Baixa transparência produz decisões com pouco valor e risco elevado.
- **Inspeção:** artefatos e progresso em direção às metas são examinados com frequência suficiente para detectar variações ou problemas.
- **Adaptação:** quando o resultado observado se distancia do esperado, o produto ou a forma de trabalhar é ajustado rapidamente.

Os pilares formam um ciclo inseparável: sem transparência, a inspeção se apoia em dados incompletos; sem inspeção, não há aprendizado; sem adaptação, aprender não modifica o resultado.

## 3. Os cinco valores

O uso bem-sucedido do Scrum depende de cinco valores:

1. **Compromisso:** o Scrum Team se compromete com suas metas e com o apoio mútuo.
2. **Foco:** a atenção principal permanece no trabalho da Sprint e no progresso em direção às metas.
3. **Abertura:** equipe e stakeholders tratam trabalho e desafios de maneira transparente.
4. **Respeito:** pessoas reconhecem umas às outras como profissionais capazes e independentes.
5. **Coragem:** problemas difíceis são enfrentados e as decisões corretas são tomadas mesmo quando são desconfortáveis.

Os valores não são slogans. Eles orientam comportamentos observáveis: expor um impedimento demonstra abertura; proteger a Meta da Sprint demonstra foco; rejeitar um incremento abaixo da qualidade definida exige coragem.

## 4. Scrum Team e responsabilidades formais

O Scrum Team é uma unidade coesa, multifuncional e autogerenciável. Não possui subequipes ou hierarquias internas prescritas pelo framework. Normalmente tem dez pessoas ou menos e reúne todas as capacidades necessárias para criar valor em cada Sprint.

### 4.1 Product Owner

É responsável por maximizar o valor do produto resultante do trabalho do Scrum Team. Sua atuação inclui:

- desenvolver e comunicar explicitamente a Meta do Produto;
- criar e comunicar claramente os itens do Product Backlog;
- ordenar os itens do Product Backlog;
- garantir que o Product Backlog seja transparente, visível e compreendido.

O Product Owner pode delegar atividades, mas continua responsável. É uma pessoa, não um comitê.

### 4.2 Scrum Master

É responsável por estabelecer o Scrum conforme definido no Scrum Guide e pela efetividade do Scrum Team. Atua a serviço do time, do Product Owner e da organização. Entre suas contribuições estão:

- orientar autogerenciamento e multifuncionalidade;
- ajudar o time a produzir incrementos de alto valor que atendam à Definition of Done;
- promover a remoção de impedimentos;
- assegurar que os eventos ocorram de forma positiva, produtiva e dentro do timebox;
- apoiar planejamento empírico e adoção organizacional do Scrum.

O Scrum Master não é secretário de reuniões nem gerente das pessoas.

### 4.3 Developers

São as pessoas comprometidas em criar qualquer aspecto de um Incremento utilizável a cada Sprint. São responsáveis por:

- criar o plano da Sprint, o Sprint Backlog;
- incorporar qualidade por meio da Definition of Done;
- adaptar diariamente o plano em direção à Meta da Sprint;
- responsabilizar-se mutuamente como profissionais.

“Developer” representa quem contribui para o incremento, independentemente de cargo técnico específico.

## 5. Eventos do Scrum

A Sprint funciona como contêiner para todos os outros eventos. Os eventos criam regularidade e reduzem a necessidade de reuniões adicionais. Cada evento é uma oportunidade formal de inspecionar e adaptar artefatos.

| Evento | Propósito principal | Timebox em Sprint de um mês |
|---|---|---:|
| Sprint | transformar ideias em valor e abrigar os demais eventos | um mês ou menos |
| Sprint Planning | definir por que a Sprint é valiosa, o que será feito e como começar | até 8 horas |
| Daily Scrum | inspecionar progresso rumo à Meta da Sprint e adaptar o plano | 15 minutos |
| Sprint Review | inspecionar o resultado com stakeholders e adaptar o Product Backlog | até 4 horas |
| Sprint Retrospective | planejar maneiras de aumentar qualidade e efetividade | até 3 horas |

Para Sprints mais curtas, Planning, Review e Retrospective geralmente são mais curtas.

### 5.1 Sprint

Uma nova Sprint começa imediatamente após a anterior. Durante a Sprint:

- não são feitas mudanças que coloquem a Meta da Sprint em risco;
- a qualidade não diminui;
- o Product Backlog é refinado conforme necessário;
- o escopo pode ser esclarecido e renegociado com o Product Owner à medida que se aprende.

Somente o Product Owner possui autoridade para cancelar uma Sprint, caso sua meta se torne obsoleta.

### 5.2 Sprint Planning

O Scrum Team inteiro inicia a Sprint respondendo a três tópicos:

1. **Por que esta Sprint é valiosa?** A resposta dá origem à Meta da Sprint.
2. **O que pode ser feito nesta Sprint?** Developers selecionam itens do Product Backlog em conversa com o Product Owner.
3. **Como o trabalho escolhido será realizado?** Developers planejam o necessário para criar um Incremento que atenda à Definition of Done.

### 5.3 Daily Scrum

É um evento de 15 minutos para os Developers. Seu propósito é melhorar o foco e o autogerenciamento por meio da inspeção do progresso rumo à Meta da Sprint e da adaptação do Sprint Backlog. Não é uma reunião de prestação de contas ao Scrum Master.

### 5.4 Sprint Review

Scrum Team e stakeholders inspecionam o resultado da Sprint e discutem mudanças no ambiente. O Product Backlog pode ser adaptado. A Review é uma sessão de trabalho, não apenas uma apresentação e não funciona como portão obrigatório para liberar valor.

### 5.5 Sprint Retrospective

O Scrum Team examina pessoas, interações, processos, ferramentas e Definition of Done. Identifica mudanças úteis e pode adicionar melhorias ao próximo Sprint Backlog. Seu foco é aprender, não buscar culpados.

## 6. Artefatos e seus compromissos

Cada artefato representa trabalho ou valor e contém um compromisso que melhora foco e transparência.

| Artefato | O que representa | Compromisso associado |
|---|---|---|
| Product Backlog | lista emergente e ordenada do que é necessário para melhorar o produto | Meta do Produto |
| Sprint Backlog | Meta da Sprint, itens selecionados e plano acionável dos Developers | Meta da Sprint |
| Incremento | passo concreto e utilizável em direção à Meta do Produto | Definition of Done |

### 6.1 Product Backlog e Meta do Produto

O Product Backlog é a única fonte de trabalho realizado pelo Scrum Team. Ele evolui à medida que o produto e seu ambiente são compreendidos. A Meta do Produto descreve um estado futuro que serve como objetivo de longo prazo.

### 6.2 Sprint Backlog e Meta da Sprint

O Sprint Backlog é um plano criado por e para os Developers. Ele é atualizado ao longo da Sprint conforme mais se aprende, sem comprometer a Meta da Sprint. A Meta cria coerência e permite flexibilidade sobre o trabalho exato necessário para alcançá-la.

### 6.3 Incremento e Definition of Done

Um Incremento é um passo concreto, aditivo e completamente verificado. Trabalho que não atende à Definition of Done não faz parte do Incremento, não pode ser liberado nem apresentado como concluído na Sprint Review. Vários incrementos podem ser criados e entregues durante uma mesma Sprint.

## 7. Classificação correta dos conceitos

### Elementos formais do Scrum

- **Scrum Team:** Product Owner, Scrum Master e Developers.
- **Eventos:** Sprint, Sprint Planning, Daily Scrum, Sprint Review e Sprint Retrospective.
- **Artefatos:** Product Backlog, Sprint Backlog e Incremento.
- **Compromissos:** Meta do Produto, Meta da Sprint e Definition of Done.
- **Fundamentos:** empirismo, pensamento Lean, três pilares e cinco valores.

### Relacionados, mas não elementos formais

- stakeholders, clientes e usuários;
- refinamento do Product Backlog, que é uma atividade contínua, não um evento formal;
- user stories, story points, planning poker, burndown e quadro Kanban, que são técnicas opcionais;
- entrega ou release, que pode acontecer sempre que houver valor e qualidade suficientes.

### Não pertencem à definição do Scrum

- Project Manager como papel obrigatório;
- Sprint 0;
- reunião de status para o chefe;
- fase exclusiva de testes depois da Sprint;
- “To Do List” como substituto do Product Backlog;
- “Project Release” como evento obrigatório;
- rugby como componente do framework — o esporte inspirou a metáfora histórica, mas não é um elemento do Scrum.

## 8. Aplicação prática: produto EcoCiclo

O **EcoCiclo** é uma plataforma fictícia que ajuda moradores a encontrar pontos confiáveis para descarte de recicláveis e a consultar materiais aceitos, horários e instruções.

### 8.1 Meta do Produto

> Tornar o descarte responsável mais simples, permitindo que moradores encontrem uma opção adequada em até dois minutos e que informações incorretas sejam corrigidas pela comunidade.

### 8.2 Scrum Team

- **Product Owner:** ordena o backlog a partir do impacto ambiental e das necessidades dos usuários.
- **Scrum Master:** favorece empirismo, remove impedimentos e ajuda a organização a colaborar com o time.
- **Cinco Developers:** competências de experiência do usuário, front-end, back-end, qualidade, dados e infraestrutura são compartilhadas conforme necessário.

### 8.3 Product Backlog inicial

| Ordem | Item | Valor esperado | Estimativa opcional |
|---:|---|---|---:|
| 1 | buscar ecopontos por CEP ou localização | encontrar alternativas próximas | 8 pontos |
| 2 | filtrar por material aceito | evitar deslocamento inútil | 5 pontos |
| 3 | consultar endereço, horário e instruções | aumentar confiança nos dados | 3 pontos |
| 4 | abrir rota no aplicativo de mapas | facilitar o deslocamento | 3 pontos |
| 5 | informar dado incorreto | melhorar qualidade da base | 3 pontos |
| 6 | cadastrar e validar um ecoponto | ampliar cobertura com governança | 8 pontos |
| 7 | agendar coleta domiciliar | atender pessoas com baixa mobilidade | 8 pontos |
| 8 | receber atualização do agendamento | reduzir incerteza | 5 pontos |

Os pontos são uma técnica escolhida pelo time para apoiar conversas. Scrum não exige story points.

### 8.4 Primeira Sprint de quatro semanas

**Meta da Sprint:** permitir que moradores encontrem um ecoponto confiável por CEP e material aceito, consultando as informações essenciais antes de sair de casa.

**Itens selecionados:** busca por CEP, filtro por material, detalhes do ecoponto e mecanismo para informar dado incorreto.

**Plano inicial:** validar fluxo com usuários, estruturar base de dados, implementar API e interface responsiva, criar testes, verificar acessibilidade e preparar monitoramento. O plano pode mudar durante a Sprint; a Meta permanece como referência.

### 8.5 Definition of Done inicial

Um item somente integra o Incremento quando:

- critérios de aceitação foram atendidos;
- revisão de código foi concluída;
- testes automatizados e exploratórios relevantes passaram;
- não há vulnerabilidade crítica conhecida;
- interface essencial funciona por teclado e em tela móvel;
- dados pessoais seguem o mínimo necessário e a política definida;
- documentação de operação foi atualizada;
- incremento está integrado e potencialmente liberável.

### 8.6 Calendário dos eventos

- **Dia 1:** Sprint Planning, planejada para quatro horas e limitada a oito.
- **Todos os dias úteis:** Daily Scrum de 15 minutos.
- **Ao longo da Sprint:** refinamento quando necessário, sem transformá-lo em evento prescrito.
- **Último dia:** Sprint Review planejada para duas horas e limitada a quatro.
- **Após a Review:** Sprint Retrospective planejada para 90 minutos e limitada a três horas.
- **Imediatamente depois:** começa a próxima Sprint.

### 8.7 Evidências de empirismo

- Transparência: backlog, metas, Definition of Done e estado do incremento ficam visíveis.
- Inspeção: Daily, Review, Retrospective e testes revelam progresso e problemas.
- Adaptação: Developers atualizam o plano, o Product Owner reordena o backlog e o time melhora sua forma de trabalhar.

## 9. Antipadrões que o exemplo evita

1. **Product Owner ausente:** decisões de valor não podem depender de semanas de espera.
2. **Scrum Master como chefe:** autogerenciamento é incompatível com distribuição diária de tarefas por uma autoridade externa.
3. **Daily como status:** a conversa deve ajudar Developers a adaptar seu plano.
4. **Backlog congelado:** ele é emergente e muda quando há aprendizado.
5. **Review como aceite burocrático:** feedback não deve esperar o fim para descobrir valor.
6. **Retrospective sem ação:** pelo menos uma melhoria relevante precisa influenciar o trabalho futuro.
7. **Qualidade negociável:** reduzir a Definition of Done cria dívida e falsa percepção de velocidade.
8. **Sprint 0 eterna:** preparação necessária pode ser incorporada ao trabalho real sem inventar uma fase que não produz valor.

## 10. Síntese

O Scrum funciona como um sistema coerente. Responsabilidades deixam claro quem maximiza valor, quem sustenta a efetividade e quem cria o incremento. Eventos estabelecem um ritmo de inspeção e adaptação. Artefatos tornam trabalho e valor transparentes, enquanto metas e Definition of Done fornecem foco e qualidade.

Completar o framework não significa apenas posicionar cartões em um diagrama. Significa compreender as relações: a Sprint produz incrementos; o Sprint Backlog orienta Developers; a Meta da Sprint preserva coerência; a Review adapta o futuro do produto; e a Retrospective melhora a capacidade de entregar. Quando pilares e valores aparecem em decisões observáveis, Scrum deixa de ser uma agenda de reuniões e passa a apoiar aprendizado sobre problemas complexos.

---

## Referências

1. SCHWABER, Ken; SUTHERLAND, Jeff. *O Guia do Scrum: o guia definitivo para o Scrum — as regras do jogo*. Novembro de 2020. Tradução brasileira. Disponível em: <https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-PortugueseBR-3.0.pdf>.
2. SCHWABER, Ken; SUTHERLAND, Jeff. *The Scrum Guide*. Novembro de 2020. Versão oficial em inglês. Disponível em: <https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf>.
3. SCRUM GUIDES. *Download the official Scrum Guide*. Disponível em: <https://scrumguides.org/download.html>.
