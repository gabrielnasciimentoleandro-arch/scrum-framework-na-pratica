# Como contribuir

Contribuições devem preservar a precisão conceitual e o caráter autoral do projeto.

## Critérios

1. Use o Scrum Guide 2020 como referência normativa.
2. Diferencie elementos formais de técnicas opcionais.
3. Não transforme práticas populares em regras do Scrum.
4. Cite fontes externas.
5. Não reproduza slides, templates ou textos sem licença.
6. Preserve acessibilidade e funcionamento offline do guia interativo.

## Verificação

```bash
python scripts/validate_project.py
python -m unittest discover -s tests -v
```

Se o guia principal for alterado, regenere os documentos:

```bash
python scripts/generate_deliverables.py
```
