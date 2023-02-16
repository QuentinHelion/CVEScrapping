# CVEScrapping
## Descriptif détaillé
Dans ce TP, votre objectif sera d'automatiser la récupération d'information de CVE sur le site du NIST ou
de CVE details.
## Votre script :
Pour quelques informations données par l'utilisateur :
- Équipement
- Version
- OS
- Nom de CVE
- Etc.

/!\ Les informations que vous souhaitez donner à votre programme pour la collecte des CVE dépend de
votre utilisation, vous n'êtes pas obligé d'implémenter cette fonctionnalité de recherche. Par exemple, à la
place, votre programme pourrait en fonction d'une date, d'une semaine, d'un mois donné, récupérer
l'ensemble des CVE ayant été identifié puis de les extraire dans un Excel ou autre pour votre veille cyber.
/!\

<br>
Votre outil ira chercher les résultats présents sur l'un de ces sites à l'aide de l'API ou des modules de
Web scraping comme Beautiful Soup, puis stockera ces informations dans un format json ou yaml et un
format lisible comme txt, excel ou md.
<br><br>
Utilisez au maximum les techniques et bonnes pratiques vu en cours dans votre code, décomposez en
plusieurs fichiers, utilisez un environnement virtuel etc.
<br><br>
Vous pouvez en plus utiliser les classes pour obtenir une structure plus modulable vous permettant
d'utiliser les résultats dans d'autres codes par la suite.
<br><br>
Le but de cet exercice est d'automatiser au maximum la partie reconnaissance d'un pentest ou de tout
autre type de cybersécurité offensive.

## Ressources
https://www.cvedetails.com
https://nvd.nist.gov/vuln/search
https://code.tutsplus.com/fr/tutorials/scraping-webpages-in-python-with-beautiful-soup-the-basics--cms28211
https://www.twilio.com/fr/blog/web-scraping-analyse-html-python-beautiful-soup

## Outils
Beautiful Soup, request et autres librairies python de votre choix.
