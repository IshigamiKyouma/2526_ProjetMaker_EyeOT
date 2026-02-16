# 2526_ProjetMaker_EyeOT

Projet de MANSARD Johann réalisé dans le cadre du projet Maker.

## 1. Description du Projet et rétroplanning
### 1.1. Contexte et objectifs

En tant que joueur passionné de League of Legends et "Main Vel'Koz", j'ai toujours été fasciné par le concept de ce champion :
une entité du Néant qui déconstruit la réalité pour accumuler des connaissances.

<details>
  <summary>Cliquez ici pour voir le modèle 3D de Vel'Koz</summary>
  <br>
  <div align="center">
    <img src="https://static.wikia.nocookie.net/leagueoflegends/images/d/d6/Vel%27Koz_Render.png/revision/latest/scale-to-width-down/1200?cb=20200514004403" width="500" alt="Modèle 3D Vel'Koz">
    <p><i>Rendu 3D du modèle Vel'Koz (Source : Riot Games)</i></p>
  </div>
</details>

L'idée de ce projet est née d'une envie simple: briser le quatrième mur. Je ne voulais plus que Vel'Koz soit uniquement une image sur mon écran, mais qu'il devienne un compagnon physique capable de réagir, en temps réel, à l'intensité de mes parties.

L'objectif est de créer une figurine interactive qui agit comme une extension sensorielle du jeu. Grâce à l'intégration de l'API de Riot Games et de composants électroniques, la figurine "vit" au rythme de la faille:

* Réaction aux événements: Un feedback visuel lors de l'application des stacks de passif (LEDs hautes qui s'allument une à une) puis la centrale lors de l'activation du passif "Organic Deconstruction".

* Analyse des mouvements: Les tentacules se déplacent en fonction de la vitesse de déplacement en jeu

### 1.2. Solutions techniques

* **Cœur du système :** Microcontrôleur **ESP32**, choisi pour sa gestion fluide des interruptions et ses multiples canaux PWM nécessaires au pilotage synchrone des servomoteurs et du bus NeoPixel.
* **Communication de données :** Script en **Python** interrogeant la *Live Client Data API* de Riot Games à haute fréquence (HTTPS) et transmettant les états à l'ESP32 via une liaison **Série (USB)**.
* **Actionneurs & Visuels :**  3 Servomoteurs pour l'animation cinétique.
    * 3 LEDs adressables (NeoPixel) pour les stacks et 1 bloc circulaire pour l'œil central.
* **Gestion de l'énergie :** Conception d'un **PCB dédié** à la distribution de puissance, incluant un filtrage par condensateurs pour lisser les appels de courant des servos et une alimentation externe **5V 3A**.
* **Structure & Design :** Modélisation CAO et impression 3D. Le châssis est conçu pour masquer l'électronique dans le socle.

---

### 1.3. Obtention des valeurs

Pour obtenir:
* la vitesse de déplacement du joueur: on utilisera directement l'API
* les stacks de passif: Apparaissent visuelement quand on clique sur un ennemie

### Mécanisme de mouvement : Le système à câbles
Pour reproduire le mouvement fluide et "invertébré" des tentacules de Vel'Koz avec seulement 3 servomoteurs, le projet utilise un système de **flexion par câbles (tendeurs)** :

* **Principe :** Chaque tentacule est imprimée en matériau semi-rigide ou composée de vertèbres articulées.
* **Transmission :** Un câble (type fil de pêche ou nylon) parcourt l'intérieur de la tentacule jusqu'à l'extrémité. 
* **Actionnement :** Le servomoteur, situé dans la base, tire sur le câble pour courber la structure. Un ressort interne ou la mémoire de forme du plastique permet le retour à la position initiale.
* **Résultat :** Cela permet d'obtenir une ondulation organique plutôt qu'une rotation robotique rigide.

---

### Rétro-planning

| Session | Phase | Objectif principal |
| ------- | ----- | ------------------ |
| **TP 1** | **PoC Logiciel** | Script Python : récupération des données API et envoi vers l'ESP32. |
| **TP 2** | **Électronique** | Montage breadboard : test simultané des 3 servos et des LEDs. |
| **TP 3** | **Design PCB** | Routage du circuit d'alimentation et préparation à la soudure. |
| **TP 4** | **Modélisation 3D** | CAO du corps et du mécanisme de tension des tentacules. |
| **TP 5** | **Mécanique** | Assemblage des servos et tests des câbles de traction. |
| **TP 6** | **Intégration** | Soudure finale sur PCB et insertion dans la structure 3D. |
| **TP 7** | **Calibration** | Mapping des data LoL -> angles de servos et finitions visuelles. |
