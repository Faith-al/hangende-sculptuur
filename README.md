# Planning Hangende Sculptuur

Gedeelde planning voor de casus *Hangende sculptuur (asymmetrisch)*: weekplanning, mijlpalen, taken per team, teamleden, voortgang en het overdrachtslog.

**Website:** https://faith-al.github.io/hangende-sculptuur/

- **Kijken** kan iedereen, zonder account.
- **Bewerken** kan iedereen met de **teamcode**: klik bovenaan op *Bewerken met teamcode*. Wijzigingen staan direct online (soms na een minuutje).
- **Mijn pagina**: kies je naam en zie je eigen taken en voortgang. **Wat er gebeurt** laat zien wat er nieuw is sinds je laatste bezoek.
- **Foto's** bij voortgang worden verkleind en in de map `photos/` gezet. De repository is openbaar: zet er geen gezichten of persoonlijke dingen op.

## Hoe het werkt
Alle gegevens staan in `data.json`. De website slaat wijzigingen op met een GitHub-sleutel van Faith. Die sleutel staat versleuteld in `secret.json` en gaat alleen open met de teamcode. Elke wijziging is een commit, dus alles is terug te zetten via de geschiedenis van `data.json`.

## Teamcode instellen of wijzigen (Faith)
1. GitHub → **Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token**.
2. Naam `planning sculptuur`, vervaldatum ná 20 november.
3. **Repository access:** *Only select repositories* → `hangende-sculptuur`.
4. **Permissions → Repository permissions → Contents:** *Read and write*. Verder niets.
5. Kopieer de sleutel (`github_pat_…`).
6. Open de website → onderaan **Beheer** → plak de sleutel, kies een teamcode (minstens 10 tekens, bijv. drie woorden met streepjes) → **Teamcode opslaan**.
7. Deel de code met je team via jullie groepsapp. Deel nooit de sleutel zelf.

**Code uitgelekt?** Verwijder de oude sleutel op GitHub (stap 1) en stel met een nieuwe sleutel een nieuwe code in. De oude code werkt dan meteen niet meer.

## Bestanden
- `index.html` – de website
- `data.json` – alle planningsgegevens (wordt door de website bijgewerkt)
- `secret.json` – versleutelde sleutel (wordt door Beheer aangemaakt)
- `photos/` – foto's bij voortgang (wordt door de website gevuld)
- `tools/sync.py` – oud hulpscript om gegevens uit de Claude-versie over te zetten
