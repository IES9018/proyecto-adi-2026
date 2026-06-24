# CI/CD — GitHub Actions

**Agente:** Tech Lead

---

## Workflow: CI Pipeline

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - run: pip install -r 08_CODIGO_FUENTE/backend/requirements.txt
      - run: ruff check 08_CODIGO_FUENTE/backend/src/
      - run: mypy 08_CODIGO_FUENTE/backend/src/
      - run: pytest 08_CODIGO_FUENTE/backend/tests/ -v --cov --cov-report=term-missing

  frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: "20" }
      - run: npm ci
        working-directory: 08_CODIGO_FUENTE/frontend
      - run: npm run lint
        working-directory: 08_CODIGO_FUENTE/frontend
      - run: npm run build
        working-directory: 08_CODIGO_FUENTE/frontend

  deploy:
    needs: [backend, frontend]
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Deploy via SSH
        uses: appleboy/ssh-action@v1
        with:
          host: ${{ secrets.DEPLOY_HOST }}
          username: ${{ secrets.DEPLOY_USER }}
          key: ${{ secrets.DEPLOY_KEY }}
          script: |
            cd /opt/escuela/gobernanza
            git pull
            docker compose up -d --build
```

---

## Workflow: Backup diario

```yaml
name: Backup

on:
  schedule:
    - cron: "0 3 * * *"  # 3 AM todos los días

jobs:
  backup:
    runs-on: ubuntu-latest
    steps:
      - name: Backup PostgreSQL
        run: |
          ssh ${{ secrets.DEPLOY_USER }}@${{ secrets.DEPLOY_HOST }} \
            "docker exec gobernanza-postgres pg_dump -U gobernanza gobernanza > /backups/gobernanza-\$(date +%Y%m%d).sql"
```
