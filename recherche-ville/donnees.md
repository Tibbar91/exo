# Données

Collecte de faits. Une section par ville, sans omission.

## Convention

- `null` = non trouvé.
- `0` = absence confirmée par une source.
- Toute valeur est accompagnée de son URL et de sa date de consultation.
  Sans URL consultable, la valeur reste `null`.

## État de la collecte au 30/08/2026 — mise à jour

**12 cellules sur 84 renseignées (14,3 %).** Un seul des sept champs est couvert :
les soirées hebdomadaires. Les six autres restent à `null`.

Toutes les valeurs de ce champ proviennent du **tier 6** (`salsa.faurax.fr`,
`salsavida.com`), via le canal de recherche web : les pages n'ont pas pu être
ouvertes directement (egress bloqué), seul leur contenu indexé et résumé est
accessible. Aucune n'est vérifiée en source primaire.

### Règles de comptage appliquées

Sont comptées : les soirées **hebdomadaires** où une plage de danse libre
(social) est identifiée, et dont le style inclut la salsa.

Sont exclus, et signalés dans chaque cellule : les cours sans social ; les
soirées mensuelles ; les soirées bachata ou kizomba seules ; les soirées
saisonnières (été uniquement) ; les lieux hors commune, comptés à part.

**Déduplication** : clé `venue + jour + heure`. Trois soirées le même mardi à
Montpellier sont comptées 3 fois car les lieux diffèrent ; trois soirées au
Cabana Café à Lyon sont signalées comme un lieu unique sur trois jours.

### Fraîcheur de l'index — à lire avant d'interpréter un chiffre bas

Les pages sources n'ont pas toutes été indexées à la même date : Paris et
Montpellier « août 2026 », Toulouse « juillet 2026 », Strasbourg « juin 2026 »,
Lille « mai 2026 », Marseille « février 2026 », Nantes « juillet 2025 »,
Biarritz « juin 2025 ». Un chiffre bas ou `null` sur les villes à index ancien
peut refléter la fraîcheur du crawl et non l'état de la scène.

---

## Paris

| Donnée | Valeur | URL | Date de consultation | Tier source |
|---|---|---|---|---|
| Soirées salsa récurrentes hebdomadaires <br><sub>nombre / jour / lieu / style</sub> | **4** — lun La Station Latine (Porte des Lilas) · mer Quai F. Mauriac 13e (cubaine/rueda) · ven Quai Saint-Bernard (cubaine, ~200-400 danseurs) · sam 22 rue F. Truffaut 12e (cubaine+bachata) | https://salsa.faurax.fr/index.php/Paris ; https://www.salsavida.com/guides/france/paris/ | 2026-08-30 | tier 6 |
| Écoles enseignant la salsa <br><sub>nom / styles / niveaux / jours de cours</sub> | null | null | null | null |
| Associations de danse déclarées (RNA) <br><sub>comptage</sub> | null | null | null | null |
| Festivals ou congrès salsa dans l'année <br><sub>nom / dates</sub> | null | null | null | null |
| Ensoleillement annuel <br><sub>heures</sub> | null | null | null | null |
| Distance et temps réel jusqu'à la mer <br><sub>km / minutes / mode</sub> | null | null | null | null |
| Loyer médian T2 <br><sub>€/mois</sub> | null | null | null | null |

## Lyon

| Donnée | Valeur | URL | Date de consultation | Tier source |
|---|---|---|---|---|
| Soirées salsa récurrentes hebdomadaires <br><sub>nombre / jour / lieu / style</sub> | **1 à 3** — jeu, ven et sam au **même lieu** : Cabana Café, 30 rue de l'Annonciade 1er. Sam = soirée hebdo ; ven « latino mix » et jeu « soirée animée » de style non précisé. | https://salsa.faurax.fr/index.php/Lyon ; https://www.salsavida.com/guides/france/lyon/socials/ | 2026-08-30 | tier 6 |
| Écoles enseignant la salsa <br><sub>nom / styles / niveaux / jours de cours</sub> | null | null | null | null |
| Associations de danse déclarées (RNA) <br><sub>comptage</sub> | null | null | null | null |
| Festivals ou congrès salsa dans l'année <br><sub>nom / dates</sub> | null | null | null | null |
| Ensoleillement annuel <br><sub>heures</sub> | null | null | null | null |
| Distance et temps réel jusqu'à la mer <br><sub>km / minutes / mode</sub> | null | null | null | null |
| Loyer médian T2 <br><sub>€/mois</sub> | null | null | null | null |

## Marseille

| Donnée | Valeur | URL | Date de consultation | Tier source |
|---|---|---|---|---|
| Soirées salsa récurrentes hebdomadaires <br><sub>nombre / jour / lieu / style</sub> | **3** — lun MS Club (13014, bachata+salsa) · mar La Place des Canailles (Joliette, 19h-1h) · mer 17 bd J. Saadé (cubaine/porto/kizomba, gratuit). Exclu : jeu La Paillotte (bachata seule) ; ven Kidspark **Marignane** (hors commune) | https://salsa.faurax.fr/index.php/Marseille ; https://www.salsavida.com/guides/france/marseille/socials/ | 2026-08-30 | tier 6 |
| Écoles enseignant la salsa <br><sub>nom / styles / niveaux / jours de cours</sub> | null | null | null | null |
| Associations de danse déclarées (RNA) <br><sub>comptage</sub> | null | null | null | null |
| Festivals ou congrès salsa dans l'année <br><sub>nom / dates</sub> | null | null | null | null |
| Ensoleillement annuel <br><sub>heures</sub> | null | null | null | null |
| Distance et temps réel jusqu'à la mer <br><sub>km / minutes / mode</sub> | null | null | null | null |
| Loyer médian T2 <br><sub>€/mois</sub> | null | null | null | null |

## Toulouse

| Donnée | Valeur | URL | Date de consultation | Tier source |
|---|---|---|---|---|
| Soirées salsa récurrentes hebdomadaires <br><sub>nombre / jour / lieu / style</sub> | **1** — ven « 144% Salsa », Le 144 Dance Studio, 144 rue de la Providence, 21h30-01h30, 2 salles, 8€ | https://salsa.faurax.fr/index.php/Toulouse ; https://www.salsavida.com/guides/france/toulouse/socials/ | 2026-08-30 | tier 6 |
| Écoles enseignant la salsa <br><sub>nom / styles / niveaux / jours de cours</sub> | null | null | null | null |
| Associations de danse déclarées (RNA) <br><sub>comptage</sub> | null | null | null | null |
| Festivals ou congrès salsa dans l'année <br><sub>nom / dates</sub> | null | null | null | null |
| Ensoleillement annuel <br><sub>heures</sub> | null | null | null | null |
| Distance et temps réel jusqu'à la mer <br><sub>km / minutes / mode</sub> | null | null | null | null |
| Loyer médian T2 <br><sub>€/mois</sub> | null | null | null | null |

## Montpellier

| Donnée | Valeur | URL | Date de consultation | Tier source |
|---|---|---|---|---|
| Soirées salsa récurrentes hebdomadaires <br><sub>nombre / jour / lieu / style</sub> | **5** — mar ×3 : Manzanillo Libre (caleña) · L'Atmosphère (cubaine/porto) · Mosquito Latino (cubaine). mer ×2 : Manzanillo Libre (porto, social dès 21h30) · Jungle Pub (cubaine+bachata). Exclu : ven Manzanillo (cours seuls) ; mer Place de Venise (bachata) ; lun Le Patio **Lattes** (hors commune) | https://salsa.faurax.fr/index.php/Montpellier ; https://www.salsavida.com/guides/france/montpellier/socials/ | 2026-08-30 | tier 6 |
| Écoles enseignant la salsa <br><sub>nom / styles / niveaux / jours de cours</sub> | null | null | null | null |
| Associations de danse déclarées (RNA) <br><sub>comptage</sub> | null | null | null | null |
| Festivals ou congrès salsa dans l'année <br><sub>nom / dates</sub> | null | null | null | null |
| Ensoleillement annuel <br><sub>heures</sub> | null | null | null | null |
| Distance et temps réel jusqu'à la mer <br><sub>km / minutes / mode</sub> | null | null | null | null |
| Loyer médian T2 <br><sub>€/mois</sub> | null | null | null | null |

## Bordeaux

| Donnée | Valeur | URL | Date de consultation | Tier source |
|---|---|---|---|---|
| Soirées salsa récurrentes hebdomadaires <br><sub>nombre / jour / lieu / style</sub> | `null` — aucune hebdomadaire identifiée. Seule récurrence trouvée : « Salsa Bachata y Mas », Café de l'Horloge, **3e jeudi du mois** (mensuelle, exclue). La source indique elle-même ne pas détailler les hebdomadaires. | https://salsa.faurax.fr/index.php/Bordeaux ; https://www.salsavida.com/guides/france/bordeaux/socials/ | 2026-08-30 | tier 6 |
| Écoles enseignant la salsa <br><sub>nom / styles / niveaux / jours de cours</sub> | null | null | null | null |
| Associations de danse déclarées (RNA) <br><sub>comptage</sub> | null | null | null | null |
| Festivals ou congrès salsa dans l'année <br><sub>nom / dates</sub> | null | null | null | null |
| Ensoleillement annuel <br><sub>heures</sub> | null | null | null | null |
| Distance et temps réel jusqu'à la mer <br><sub>km / minutes / mode</sub> | null | null | null | null |
| Loyer médian T2 <br><sub>€/mois</sub> | null | null | null | null |

## Nantes

| Donnée | Valeur | URL | Date de consultation | Tier source |
|---|---|---|---|---|
| Soirées salsa récurrentes hebdomadaires <br><sub>nombre / jour / lieu / style</sub> | `null` — aucune soirée salsa hebdomadaire identifiée. Seul résultat : cours de bachata le lundi (L'Orphéon) — cours, et bachata : exclu deux fois. Page faurax indexée « juillet 2025 ». | https://salsa.faurax.fr/index.php/Nantes ; https://www.salsavida.com/guides/france/nantes/ | 2026-08-30 | tier 6 |
| Écoles enseignant la salsa <br><sub>nom / styles / niveaux / jours de cours</sub> | null | null | null | null |
| Associations de danse déclarées (RNA) <br><sub>comptage</sub> | null | null | null | null |
| Festivals ou congrès salsa dans l'année <br><sub>nom / dates</sub> | null | null | null | null |
| Ensoleillement annuel <br><sub>heures</sub> | null | null | null | null |
| Distance et temps réel jusqu'à la mer <br><sub>km / minutes / mode</sub> | null | null | null | null |
| Loyer médian T2 <br><sub>€/mois</sub> | null | null | null | null |

## Nice

| Donnée | Valeur | URL | Date de consultation | Tier source |
|---|---|---|---|---|
| Soirées salsa récurrentes hebdomadaires <br><sub>nombre / jour / lieu / style</sub> | **0 confirmée toute l'année** — « Rendez-Vous Latino », Place du Palais de Justice, tous les mercredis **l'été uniquement**. Una Locura Mi Amor (La Bode) : jour non précisé, non comptabilisable. | https://salsa.faurax.fr/index.php/dpt/06 ; https://www.salsavida.com/guides/france/nice/socials/ | 2026-08-30 | tier 6 |
| Écoles enseignant la salsa <br><sub>nom / styles / niveaux / jours de cours</sub> | null | null | null | null |
| Associations de danse déclarées (RNA) <br><sub>comptage</sub> | null | null | null | null |
| Festivals ou congrès salsa dans l'année <br><sub>nom / dates</sub> | null | null | null | null |
| Ensoleillement annuel <br><sub>heures</sub> | null | null | null | null |
| Distance et temps réel jusqu'à la mer <br><sub>km / minutes / mode</sub> | null | null | null | null |
| Loyer médian T2 <br><sub>€/mois</sub> | null | null | null | null |

## Lille

| Donnée | Valeur | URL | Date de consultation | Tier source |
|---|---|---|---|---|
| Soirées salsa récurrentes hebdomadaires <br><sub>nombre / jour / lieu / style</sub> | **1 + 1** — ven Latina Café, 42/44 rue Masséna (cours 20h puis social 21h, 8€). Hors commune : ven Salsa Picante, Star-Fun **Seclin** (salsa porto) | https://salsa.faurax.fr/index.php/Lille ; https://www.salsavida.com/guides/france/lille/ | 2026-08-30 | tier 6 |
| Écoles enseignant la salsa <br><sub>nom / styles / niveaux / jours de cours</sub> | null | null | null | null |
| Associations de danse déclarées (RNA) <br><sub>comptage</sub> | null | null | null | null |
| Festivals ou congrès salsa dans l'année <br><sub>nom / dates</sub> | null | null | null | null |
| Ensoleillement annuel <br><sub>heures</sub> | null | null | null | null |
| Distance et temps réel jusqu'à la mer <br><sub>km / minutes / mode</sub> | null | null | null | null |
| Loyer médian T2 <br><sub>€/mois</sub> | null | null | null | null |

## Strasbourg

| Donnée | Valeur | URL | Date de consultation | Tier source |
|---|---|---|---|---|
| Soirées salsa récurrentes hebdomadaires <br><sub>nombre / jour / lieu / style</sub> | **0 confirmée toute l'année** — Salsa Loca jeu 19h-22h = **cours** par niveaux, exclu. Salsa Docks = plein air, **juin à septembre**, vendredis choisis. | https://salsa.faurax.fr/index.php/Strasbourg ; https://www.salsavida.com/guides/france/strasbourg/socials/ | 2026-08-30 | tier 6 |
| Écoles enseignant la salsa <br><sub>nom / styles / niveaux / jours de cours</sub> | null | null | null | null |
| Associations de danse déclarées (RNA) <br><sub>comptage</sub> | null | null | null | null |
| Festivals ou congrès salsa dans l'année <br><sub>nom / dates</sub> | null | null | null | null |
| Ensoleillement annuel <br><sub>heures</sub> | null | null | null | null |
| Distance et temps réel jusqu'à la mer <br><sub>km / minutes / mode</sub> | null | null | null | null |
| Loyer médian T2 <br><sub>€/mois</sub> | null | null | null | null |

## Rennes

| Donnée | Valeur | URL | Date de consultation | Tier source |
|---|---|---|---|---|
| Soirées salsa récurrentes hebdomadaires <br><sub>nombre / jour / lieu / style</sub> | **1** — jeudis S.B.K.R., Bowling Alma (salsa/bachata/kizomba/rock). Exclues car mensuelles : Qué Rico Mambo (3e ven) · Salsolyk's (1er ven) | https://salsa.faurax.fr/index.php/Rennes ; https://www.salsavida.com/guides/france/rennes/socials/ | 2026-08-30 | tier 6 |
| Écoles enseignant la salsa <br><sub>nom / styles / niveaux / jours de cours</sub> | null | null | null | null |
| Associations de danse déclarées (RNA) <br><sub>comptage</sub> | null | null | null | null |
| Festivals ou congrès salsa dans l'année <br><sub>nom / dates</sub> | null | null | null | null |
| Ensoleillement annuel <br><sub>heures</sub> | null | null | null | null |
| Distance et temps réel jusqu'à la mer <br><sub>km / minutes / mode</sub> | null | null | null | null |
| Loyer médian T2 <br><sub>€/mois</sub> | null | null | null | null |

## Bayonne-Anglet-Biarritz

| Donnée | Valeur | URL | Date de consultation | Tier source |
|---|---|---|---|---|
| Soirées salsa récurrentes hebdomadaires <br><sub>nombre / jour / lieu / style</sub> | `null` — aucune soirée listée pour les trois communes. Seule trace : festival « Latin Summer Days », Anglet, **2018**. Pages faurax indexées « juin 2025 ». | https://salsa.faurax.fr/index.php/Biarritz ; https://salsa.faurax.fr/index.php/Bayonne | 2026-08-30 | tier 6 |
| Écoles enseignant la salsa <br><sub>nom / styles / niveaux / jours de cours</sub> | null | null | null | null |
| Associations de danse déclarées (RNA) <br><sub>comptage</sub> | null | null | null | null |
| Festivals ou congrès salsa dans l'année <br><sub>nom / dates</sub> | null | null | null | null |
| Ensoleillement annuel <br><sub>heures</sub> | null | null | null | null |
| Distance et temps réel jusqu'à la mer <br><sub>km / minutes / mode</sub> | null | null | null | null |
| Loyer médian T2 <br><sub>€/mois</sub> | null | null | null | null |

