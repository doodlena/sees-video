Deployment

- GitHub Actions workflow: `.github/workflows/deploy.yml`
- Publishes the contents of the `html/` folder to the `gh-pages` branch via `peaceiris/actions-gh-pages`.
- Trigger: any push to `main` (automatically deploys after each push).

How to check status

1. Go to the repository's **Actions** tab and open the latest "Deploy" run.
2. After a successful run, the site will be available at:
   `https://doodlena.github.io/sees-video/`

Troubleshooting

- If the Pages site doesn't appear after a successful run, check repository Settings → Pages for any additional configuration or required domain settings.
- This workflow uses the default `GITHUB_TOKEN` so you don't need to add any secrets.
