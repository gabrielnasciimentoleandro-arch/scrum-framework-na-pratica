# Aplicação prática — EcoCiclo

## Visão do produto

O EcoCiclo é uma plataforma fictícia para localizar pontos de reciclagem e consultar materiais aceitos, horários e instruções. O exemplo demonstra o funcionamento integrado do Scrum sem transformar técnicas opcionais em regras do framework.

## Meta do Produto

> Tornar o descarte responsável mais simples, permitindo que moradores encontrem uma opção adequada em até dois minutos e que informações incorretas sejam corrigidas pela comunidade.

## Composição do Scrum Team

| Responsabilidade | Decisões no exemplo |
|---|---|
| Product Owner | ordena oportunidades por valor ambiental, risco e aprendizado |
| Scrum Master | promove empirismo, efetividade e remoção de impedimentos |
| Developers | decidem como transformar itens selecionados em incremento utilizável |

O time tem sete pessoas: um Product Owner, um Scrum Master e cinco Developers com competências complementares.

## Product Backlog inicial

| Ordem | Item | Valor | Pontos opcionais |
|---:|---|---|---:|
| 1 | busca por CEP ou localização | encontrar ecopontos próximos | 8 |
| 2 | filtro por material | evitar deslocamentos inúteis | 5 |
| 3 | detalhes, horário e instruções | aumentar confiança | 3 |
| 4 | abrir rota no mapa | facilitar chegada | 3 |
| 5 | informar dado incorreto | melhorar qualidade dos dados | 3 |
| 6 | cadastrar e validar ecoponto | ampliar cobertura com controle | 8 |
| 7 | agendar coleta domiciliar | ampliar acessibilidade | 8 |
| 8 | acompanhar agendamento | reduzir incerteza | 5 |

Story points foram adotados apenas como apoio à conversa. Eles não são exigidos pelo Scrum.

## Sprint 1 — quatro semanas

### Meta da Sprint

Permitir que moradores encontrem um ecoponto confiável por CEP e material aceito, consultando informações essenciais antes de sair de casa.

### Itens selecionados

- busca por CEP;
- filtro por material;
- detalhes do ecoponto;
- mecanismo para informar dado incorreto.

### Plano inicial dos Developers

1. validar o fluxo principal com usuários;
2. estruturar a base de ecopontos e materiais;
3. implementar API e interface responsiva;
4. integrar busca e filtros;
5. criar testes automatizados e exploratórios;
6. verificar acessibilidade e segurança;
7. preparar observabilidade e documentação operacional.

O plano é emergente e pode ser atualizado diariamente.

## Definition of Done

- critérios de aceitação atendidos;
- revisão de código concluída;
- testes relevantes aprovados;
- nenhuma vulnerabilidade crítica conhecida;
- fluxo essencial acessível por teclado e celular;
- privacidade e uso mínimo de dados verificados;
- documentação atualizada;
- incremento integrado e potencialmente liberável.

## Agenda da Sprint

| Momento | Evento ou atividade | Duração planejada |
|---|---|---:|
| primeiro dia | Sprint Planning | 4 horas |
| dias úteis | Daily Scrum | 15 minutos |
| quando necessário | refinamento | atividade sem timebox prescrito |
| último dia | Sprint Review | 2 horas |
| após a Review | Sprint Retrospective | 90 minutos |
| imediatamente depois | nova Sprint | sem intervalo obrigatório |

Os tempos planejados ficam abaixo dos limites máximos do Scrum Guide para uma Sprint de um mês.

## Cenário de adaptação

Na segunda semana, testes revelam que parte dos usuários não sabe qual categoria corresponde ao material que deseja descartar. Developers atualizam o Sprint Backlog para incluir exemplos visuais nos filtros. O Product Owner esclarece critérios sem alterar a Meta da Sprint. A mudança é legítima porque usa aprendizado e preserva o objetivo.

Na Review, stakeholders sugerem agendamento de coleta. O Product Owner não promete entrega imediata: registra a oportunidade, avalia valor e reordena o Product Backlog. Na Retrospective, o time identifica demora na validação dos dados e decide automatizar uma verificação no próximo ciclo.

## Resultado esperado

Ao final da Sprint, o Incremento permite completar o fluxo definido na meta e atende à Definition of Done. Se isso não ocorrer, itens incompletos retornam ao Product Backlog; não recebem crédito parcial como incremento pronto.
