# Planning Hangende Sculptuur

Gedeelde planning voor de casus *Hangende sculptuur (asymmetrisch)*: weekplanning, mijlpalen, taken per team, teamleden en het overdrachtslog.

**Website:** https://faith-al.github.io/hangende-sculptuur/

- **Teamleden** openen de site en kijken mee. Geen account nodig, alleen lezen.
- **Communicators (Faith en Nariman)** bewerken de planning in de Claude-versie (claude.ai).
- Een geplande taak in Claude neemt de gegevens over naar `data.json` in deze repository (elke 2 uur tussen 8:00 en 22:00). Bovenaan de site staat wanneer de gegevens voor het laatst zijn bijgewerkt.

Niet met de hand in `data.json` werken: bij de volgende synchronisatie wordt het overschreven met de Claude-versie.

## GitHub Pages aanzetten (eenmalig)
Repository → **Settings → Pages** → *Source: Deploy from a branch* → Branch `main`, map `/ (root)` → **Save**. Na ongeveer een minuut staat de site online.

## Bestanden
- `index.html` – de website
- `data.json` – alle planningsgegevens (wordt door de site zelf bijgewerkt; niet tegelijk met de hand bewerken)
