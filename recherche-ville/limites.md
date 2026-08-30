# Limites

Ce que je n'ai pas pu vérifier, et pourquoi. Établi le 30/08/2026.

## Résumé

**Taux de remplissage : 0 % (0 cellule sur 84.)**

Les sept sources du cahier des charges sont inaccessibles depuis cette session.
Ce n'est pas une difficulté de collecte, c'est un blocage réseau : la passerelle
d'egress de l'environnement refuse la connexion aux domaines visés.

## Test effectué

Chaque domaine ci-dessous a été appelé une fois. Le proxy renvoie
`EGRESS_BLOCKED` ou un `403 CONNECT tunnel failed`.

| Source (tier) | Domaine testé | Résultat |
|---|---|---|
| 1 — RNA / socle | `www.data.gouv.fr` | `EGRESS_BLOCKED` |
| 1 — RNA / socle | `recherche-entreprises.api.gouv.fr` | `403 CONNECT tunnel failed` |
| 2 — site d'école | `salsamistica.com` | `EGRESS_BLOCKED` |
| 3 — Google Places | — | Aucune clé API dans l'environnement |
| 5 — INSEE | `www.insee.fr` | `EGRESS_BLOCKED` |
| 6 — agrégateur | `salsa.faurax.fr` | `EGRESS_BLOCKED` |
| 6 — agrégateur | `www.salsavida.com` | `EGRESS_BLOCKED` |

La documentation du proxy (`/root/.ccr/README.md`) qualifie ce code :
« The destination host is not allowed by your organization's egress policy for
this session. Do not retry or route around it — report the blocked host. »
Je n'ai donc ni réessayé ni cherché de contournement.

## Ce qui reste disponible, et pourquoi ça ne suffit pas

Un seul canal fonctionne : la recherche web, qui renvoie des titres, des URL et
un résumé synthétisé. Il ne permet pas de satisfaire le cahier des charges, pour
quatre raisons distinctes :

**1. La règle « URL + date de consultation » devient infalsifiable.**
La recherche fournit des URL, mais je ne peux pas les ouvrir. Inscrire une URL
et une date de consultation en face d'une valeur tirée d'un résumé reviendrait à
certifier une consultation qui n'a pas eu lieu.

**2. Le tier bas devient la source unique.**
Les résultats remontés proviennent majoritairement de `salsavida.com` et
`salsa.faurax.fr` — les deux sources classées tier 6, dont le cahier des charges
dit qu'elles ne doivent jamais servir seules à affirmer une absence. Le socle
tier 1 (RNA), lui, est muet.

**3. La distinction `null` / `0` s'effondre.**
`0` exige une absence confirmée par une source. Sans accès au RNA ni aux sites
d'écoles, aucune absence n'est confirmable. Toute case vide serait un `null`,
jamais un `0` — ce qui retire au tableau une part de son intérêt.

**4. Le biais de comptage annoncé est vérifié.**
Le seul résultat obtenu (Montpellier) annonce « 105 upcoming salsa events in the
next 30 days » et « 22 free salsa lessons & socials ». Ce sont des agrégats à
30 jours incluant les cours — exactement le mode de comptage que le cahier des
charges exclut. Les extraits de recherche sont construits sur ces agrégats et
n'exposent pas le détail venue + jour + horaire nécessaire à la déduplication.

## Déduplication : méthode prévue, non appliquée

La méthode reste valable si l'accès est rétabli. Elle n'a pas pu être exécutée.

1. **Clé de dédup** : `commune + venue normalisée + jour de semaine + heure de début`.
   Normalisation du venue : minuscules, accents retirés, articles et forme
   juridique retirés, adresse postale utilisée comme départage quand deux noms
   diffèrent à la même adresse.
2. **Résolution de collision par tier** : à clé identique, la valeur du tier le
   plus fiable est retenue et les autres sont conservées en annotation. Aucune
   moyenne entre tiers.
3. **Filtre récurrence** : une entrée n'est comptée que si la source la qualifie
   d'hebdomadaire ou si elle apparaît à la même clé sur au moins 3 semaines
   consécutives. Les occurrences mensuelles et les dates uniques sont exclues.
4. **Filtre cours** : une entrée dont l'intitulé ou l'horaire correspond à un
   cours est exclue du comptage des soirées, y compris lorsque le cours précède
   une soirée au même venue. Dans ce cas seule la plage social est retenue.
5. **Divergence tier 1 / tier 6** : les deux valeurs sont inscrites et l'écart
   est noté, sans arbitrage.

## Ce qui débloquerait la collecte

Par ordre d'effet :

1. **Autoriser les domaines en egress.** Le minimum utile :
   `data.gouv.fr`, `api.gouv.fr`, `insee.fr`, `meteofrance.com`, plus les
   domaines des écoles et des agrégateurs. C'est une modification de la politique
   réseau de l'environnement, côté administrateur.
2. **Fournir une clé Google Places** dans l'environnement, si le tier 3 doit être
   utilisé.
3. **À défaut : dépôt manuel des fichiers.** Le dump RNA de data.gouv.fr déposé
   dans ce répertoire suffit à produire, hors ligne, le comptage d'associations
   des 12 communes — le tier 1 pour l'un des sept champs.
