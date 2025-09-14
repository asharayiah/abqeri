# Abqeri — Full Site (with Downloads)

Replace in `index.html`:
- FORM_ENDPOINT_EARLY_ACCESS
- FORM_ENDPOINT_HUMANITY
- FORM_ENDPOINT_ENTERPRISE
- https://buy.stripe.com/PROFESSIONAL_PRICE_LINK

Update `release_manifest.json` to point to real **public** release assets (GitHub Releases in `abqeri-downloads` or your storage).

Deploy:
1) Private or Public repo OK (Pages free only on public). If private, you need GitHub Pro.
2) Commit all files, including `.github/workflows/pages.yml`.
3) Repo → Settings → Pages → Source = GitHub Actions.
4) DNS: `www` CNAME to `<username>.github.io`; apex A records to GitHub Pages IPs.
5) Enforce HTTPS when available.
