# Abqeri — Full Site Package (Static)
What to replace before deploy:
1) In index.html:
   - FORM_ENDPOINT_EARLY_ACCESS → your Formspree endpoint #1
   - FORM_ENDPOINT_HUMANITY → Formspree endpoint #2
   - FORM_ENDPOINT_ENTERPRISE → Formspree endpoint #3
   - https://buy.stripe.com/PROFESSIONAL_PRICE_LINK → your Stripe Checkout URL

Deploy on GitHub Pages (private repo allowed):
- Create a private repo, upload these files.
- Settings → Pages → Source = GitHub Actions.
- Add .github/workflows/pages.yml (see ChatGPT message for sample).
- Custom domain: abqeri.com. Keep the provided CNAME file.
