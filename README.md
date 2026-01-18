# 2526_ProjetMaker_EyeOT
## 1. Description du Projet et rétroplanning
### 1.1. Contexte et objectifs

En tant que joueur passionné de League of Legends et "Main Vel'Koz", j'ai toujours été fasciné par le concept de ce champion :
une entité du Néant qui déconstruit la réalité pour accumuler des connaissances.

L'idée de ce projet est née d'une envie simple: briser le quatrième mur. Je ne voulais plus que Vel'Koz soit uniquement une image sur mon écran, mais qu'il devienne un compagnon physique capable de réagir, en temps réel, à l'intensité de mes parties.

L'objectif est de créer une figurine interactive qui agit comme une extension sensorielle du jeu. Grâce à l'intégration de l'API de Riot Games et de composants électroniques, la figurine "vit" au rythme de la faille:

* Réaction aux événements: Un feedback visuel lors de l'application des stacks de passif (LEDs hautes qui s'allument une à une) puis la centrale lors de l'activation du passif "Organic Deconstruction".

* Analyse des mouvements: Les tentacules se déplacent en fonction de la vitesse de déplacement en jeu

### 1.2. Solutions techniques

1. ESP32 pour la commande des LEDs et des servomoteurs

2. Liaison USB pour la communication avec la *Live Client Data API* de League of Legends

3. Modélisation et impression 3D du corps et du socle pour soutenir le corps et accueillir l'électronique 

4. PCB pour l'alimentation des composants

5. Alimentation externe de type 5V 3A. (Valeur susceptibles de changer en fonction des composants choisis)
### 1.3. Rétroplanning
