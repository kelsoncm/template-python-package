<!-- template:start -->
# template-python-package

Template de pacote Python tipado (layout `src/`, `py.typed`), com Ruff, mypy estrito, pytest com cobertura mínima de
100%, pre-commit, documentação Sphinx (Furo) no GitHub Pages e release por tag com publicação no PyPI via Trusted
Publishing (sem token).

## Como usar

1. **Use this template > Create a new repository** (ex.: `python-meupacote`).
2. Clone e rode o inicializador (só biblioteca padrão do Python 3.10+):

   ```bash
   python template_init.py --name meu_pacote --description "O que o pacote faz."
   ```

   `--name` é o nome de importação (`meu_pacote`); o nome no PyPI vira `meu-pacote` (troque com `--dist`).
   O exemplo `new_package`/`new-package` e os marcadores (`{{OWNER}}`, `{{AUTHOR}}`...) são trocados e o script se
   apaga. Use `--dry-run` para conferir antes.
3. Desenvolva:

   ```bash
   python -m venv .venv && . .venv/bin/activate   # no Windows: .venv\Scripts\activate
   pip install -e ".[dev,docs]"
   pre-commit install --install-hooks -t pre-commit -t pre-push
   ```

4. Ative o GitHub Pages (*Settings > Pages > Source: GitHub Actions*) e configure o Trusted Publisher no PyPI
   (workflow `release.yml`, environment `pypi`).

---
<!-- template:end -->
# new-package

{{DESCRIPTION}}

[![QA](https://github.com/{{OWNER}}/new-package/actions/workflows/qa.yml/badge.svg)](https://github.com/{{OWNER}}/new-package/actions/workflows/qa.yml)

Documentação: <https://{{OWNER}}.github.io/new-package/>

## Instalação

```bash
pip install new-package
```

## Uso

```python
from new_package import greet

greet("Ada")  # 'Hello, Ada!'
```

## Desenvolvimento

```bash
pip install -e ".[dev,docs]"
pre-commit install --install-hooks -t pre-commit -t pre-push
ruff check . && ruff format --check . && mypy && pytest
sphinx-build -W -b html docs docs/_build/html
```

## Release

1. Atualize `version` no `pyproject.toml` e a seção no `CHANGELOG.md`.
2. `git tag vX.Y.Z && git push origin vX.Y.Z`: o workflow `release.yml` confere a versão, cria a release e publica
   no PyPI.

## Licença

[MIT](LICENSE.md).
