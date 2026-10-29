# Planning Hangende Sculptuur

Gedeelde planning voor de casus *Hangende sculptuur (asymmetrisch)*: weekplanning, mijlpalen, taken per team, teamleden en het overdrachtslog.

**Website:** https://faith-al.github.io/hangende-sculptuur/

- **Teamleden** kunnen de site gewoon openen en meekijken. Geen account nodig.
- **Communicators (Faith en Nariman)** loggen op de site in met een GitHub-sleutel en kunnen dan alles bewerken. Elke wijziging wordt direct opgeslagen in `data.json` in deze repository.

Wijzigingen zijn voor kijkers binnen een paar minuten zichtbaar (de pagina ververst elke 2 minuten vanzelf).

---

## Inloggen als communicator

### Faith (eigenaar van de repository)
1. Ga naar **GitHub → Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token**.
2. Naam: `planning sculptuur`, vervaldatum: na 20 november (bijv. 60 dagen).
3. **Repository access:** *Only select repositories* → `hangende-sculptuur`.
4. **Permissions → Repository permissions → Contents:** *Read and write*.
5. Klik *Generate token* en kopieer de sleutel (begint met `github_pat_`).
6. Open de website, klik **Inloggen als communicator** en plak de sleutel.

### Nariman
1. Faith voegt Nariman toe: repository → **Settings → Collaborators → Add people** → Narimans GitHub-naam. Nariman accepteert de uitnodiging (via e-mail of github.com/notifications).
2. Nariman maakt een sleutel aan: **Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token (classic)**, vink alleen **`public_repo`** aan, vervaldatum na 20 november.
   (Een *fine-grained* sleutel werkt hier niet, omdat de repository van Faith is.)
3. Website openen → **Inloggen als communicator** → sleutel plakken.

**Let op:** deel je sleutel met niemand en zet hem nooit in een bestand of chat. De sleutel blijft alleen in je eigen browser bewaard; klik op **Uitloggen** op een gedeelde computer.

---

## GitHub Pages aanzetten (eenmalig)
Repository → **Settings → Pages** → *Source: Deploy from a branch* → Branch `main`, map `/ (root)` → **Save**. Na ongeveer een minuut staat de site online.

## Bestanden
- `index.html` – de website
- `data.json` – alle planningsgegevens (wordt door de site zelf bijgewerkt; niet tegelijk met de hand bewerken)
