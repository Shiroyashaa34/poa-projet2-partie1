# Journal de bord - Projet 2 (partie 1)

HAI716I, tournoi d'Axelrod modifié.

## Objectif

Coder un tournoi de dilemme du prisonnier itéré, faire jouer des stratégies entre elles et expliquer les classements.

## Plan

D'abord le moteur et les 5 stratégies du cours (ALL-D, RANDOM, TIT-FOR-TAT, TESTER, JOSS), pour voir si TIT-FOR-TAT gagne. Ensuite j'ajoute 2 stratégies hors cours et je compare. Enfin je modifie 2 règles du tournoi, en notant ma prédiction avant de lancer.

## Protocole

Chaque paire de stratégies joue 5 parties de 200 tours, comme dans le tournoi d'Axelrod du cours, avec les gains du sujet (CC = 3/3, CD = 0/5, DC = 5/0, DD = 2/2). Une stratégie ne joue pas contre elle-même, parce que le sujet dit "chaque autre". La graine aléatoire est fixée à 42 pour que les résultats soient les mêmes à chaque lancement.

## Stratégies

**ALL-D** vient du cours : elle joue toujours D, c'est la stratégie "rationnelle" de la récurrence à rebours. Je pense qu'elle va bien s'en sortir contre ceux qui coopèrent sans jamais punir, comme RANDOM, puisqu'elle prend 5 à chaque fois que l'autre joue C. Par contre contre ceux qui ripostent, elle gagne le premier tour puis ne prend plus que 2 par tour.

**TIT-FOR-TAT** vient aussi du cours, c'est celle qui a gagné le tournoi d'Axelrod en 1980 : elle commence par C puis copie le dernier coup de l'adversaire. Je m'attends à ce qu'elle marche bien contre les stratégies qui coopèrent, et contre ALL-D elle ne se fait avoir qu'une fois. Par contre elle ne peut jamais battre son adversaire en duel, au mieux elle fait égalité.

**RANDOM** vient du cours : elle joue C ou D au hasard, une chance sur deux. Elle sert de témoin, pour voir si les autres font mieux que le hasard. Je pense qu'elle va finir dernière, parce qu'elle ne punit jamais et ne récompense jamais, donc tout le monde peut l'exploiter, surtout ALL-D.

**TESTER** vient du cours : elle commence par D pour tester l'adversaire. Si l'adversaire riposte, elle passe en TIT-FOR-TAT, sinon elle répète C, C, D pour l'exploiter. La diapo ne dit pas exactement ce que veut dire "riposter", j'ai pris "l'adversaire a joué D au moins une fois". Je m'attends à ce qu'elle profite des stratégies naïves, mais contre TIT-FOR-TAT son D du premier tour risque de déclencher des représailles.

**JOSS** vient du cours : c'est TIT-FOR-TAT, mais une fois sur dix elle remplace son C par un D. Dans le code, elle hérite de TIT-FOR-TAT et ne fait que modifier son coup. Je pense qu'elle gagne un peu contre ceux qui ne punissent pas, mais contre TIT-FOR-TAT chaque trahison va lancer un échange de représailles qui coûte des points aux deux.

**GRIM** ne vient pas du cours, c'est la stratégie de l'économiste Friedman (1971)(aussi appelée "Grim Trigger"). Elle coopère tant que l'adversaire n'a jamais trahi, mais dès la première trahison elle trahit pour toujours, sans jamais pardonner. Je pense qu'elle va bien marcher contre TIT-FOR-TAT, avec qui elle coopérera tout le long. Contre ALL-D, elle se fait avoir une seule fois, comme TFT. Par contre, contre JOSS et RANDOM, une seule trahison au hasard suffit pour qu'elle trahisse jusqu'à la fin, donc elle risque de perdre beaucoup de points à cause de sa rancune.

**PAVLOV** ne vient pas du cours non plus, elle a été rendue célèbre par Nowak et Sigmund (1993) (aussi appelée "win-stay, lose-shift"). Elle commence par C, puis si son dernier coup lui a rapporté 3 ou 5 elle le rejoue, sinon elle change. Je pense qu'elle va bien coopérer avec TFT et GRIM. Par contre, contre ALL-D elle va alterner : elle prend 0, passe à D, prend 2, repasse à C, et ainsi de suite, donc elle va perdre des points en revenant tout le temps coopérer. Contre RANDOM, quand elle trahit un C elle garde D, donc elle peut l'exploiter un peu.


## Suivi

### Vendredi 13/11

#### Compréhension du sujet

J'ai lu le sujet et le cours 4. J'ai créé le dépôt, le README et le journal.
Pour le langage, j'ai choisi Python (plus à l'aise).

#### Etape 1

J'ai écrit le moteur : une fonction `partie` qui fait jouer deux stratégies pendant un nombre de tours donné, et une fonction `tournoi` qui fait jouer tout le monde contre tout le monde. J'ai fixé les paramètres du tournoi au passage (voir protocole).

### Samedi 14/11

J'ai fait une classe par stratégie avec une méthode `jouer(mes_coups, coups_adv, rng)` qui renvoie C ou D. J'ai mis ALL-D et TIT-FOR-TAT.

J'ai hésité à faire des fonctions à la place des classes, vu que l'historique est donné à chaque tour, les stratégies n'ont pas besoin de garder un état. Mais j'ai quand meme décider de garder les classes : le nom est rangé avec la stratégie (et en prévision JOSS pourra hériter de TFT).

Pour vérifier le moteur, je refais l'exemple du cours : TFT contre ALL-D sur 10 tours. Je trouve 18 pour TFT et 23 pour ALL-D, pareil que la diapo.

![Test moteur](captures/test_moteur.png)

J'ai ajouté les 3 stratégies du cours qui manquaient : RANDOM, TESTER et JOSS (voir le détail dans la section Stratégies).

J'ai lancé le tournoi avec les 5 stratégies et une graine 42. Je l'ai lancé deux fois et j'ai exactement le même classement, donc la graine marche.

![Classement étape 1](captures/etape1.png)


TIT-FOR-TAT gagne-t-il ? 
Non, il finit 3e. C'est ALL-D qui gagne, TESTER est 2e juste devant TFT (22 points d'écart, presque rien).

![Résultat match par match](captures/detail_etape1.png)

En regardant les scores match par match, je vois qu'ALL-D gagne surtout grâce à RANDOM : contre les autres elle fait environ 2 par tour, mais contre RANDOM elle prend 5 une fois sur deux (3458 points contre RANDOM, environ 2000 contre chacun des autres). Mon hypothèse : sans RANDOM, ALL-D ne gagnerait plus.

La différence avec 1980 vient de la population. Ici TFT est la seule stratégie qui ne trahit jamais en premier, donc elle n'a personne avec qui coopérer à 3 par tour. En plus, TESTER et JOSS la piègent dans des échanges de représailles : contre TESTER elle fait 2500 au lieu de 3000, parce que TESTER commence par D, TFT riposte, et les deux se renvoient la trahison toute la partie. En 1980 il y avait 14 programmes, et beaucoup étaient "gentils" (ils ne trahissent jamais en premier), c'est avec eux que TFT faisait ses points. C'est ce que dit le cours : TFT marche seulement si elle rencontre assez de stratégies qui pensent comme elle.

### Dimanche 15/11

Pour vérifier, j'ai relancé le tournoi sans RANDOM (ligne en commentaire dans `etape1.py`). TFT passe 1re et ALL-D tombe dernière : l'hypothèse est confirmée, ALL-D gagnait grâce aux points pris contre RANDOM. TFT ne gagne que de 21 points devant TESTER, donc ça reste serré.

![sans RANDOM](captures/etape1_sansrandom.png)

#### Étape 2

J'ajoute 2 stratégies qui ne sont pas dans le cours : GRIM et PAVLOV (voir le détail dans la section Stratégies). Je les ai choisies parce qu'elles sont toutes les deux "gentilles" comme TFT, mais avec deux idées opposées : GRIM ne pardonne jamais, PAVLOV se corrige selon ce que son coup lui a rapporté. D'après ce que j'ai vu à l'étape 1, avoir plus de stratégies gentilles devrait aider TFT, puisqu'elle aura enfin des partenaires avec qui coopérer.

J'ai lancé le tournoi avec les 7 stratégies, toujours avec la graine 42.

![Classement étape 2](captures/etape2.png)

C'est GRIM qui gagne, TFT est 2e et ALL-D tombe 3e. Par rapport à l'étape 1, TFT passe de 3e à 2e et ALL-D perd la 1re place.

![Résultat match par match étape 2](captures/detail_etape2.png)

Comme je l'avais prévu, ajouter des stratégies gentilles aide TFT : contre GRIM et contre PAVLOV elle fait 3000, c'est-à-dire qu'elles coopèrent tout le long, à 3 par tour. Tous les matchs entre TFT, GRIM et PAVLOV finissent à 3000 des deux côtés.

Par contre je me suis trompé sur GRIM. Je pensais que sa rancune allait lui faire perdre beaucoup de points contre RANDOM, mais c'est l'inverse, c'est même son meilleur match (3457). Dès que RANDOM trahit une fois, GRIM trahit pour toujours, donc elle joue comme ALL-D et prend 5 à chaque fois que RANDOM joue C. TFT, lui, continue de copier RANDOM et lui pardonne, il ne fait que 2476. C'est presque toute la différence entre GRIM et TFT au classement. Donc ne jamais pardonner, ici, ça paye contre une stratégie qui trahit au hasard.

Pour PAVLOV, j'avais raison contre ALL-D : elle alterne C et D, prend 0 puis 2, donc 1 par tour en moyenne (1000 points). Mais je n'avais pas vu que ça profite aussi à ALL-D, qui fait 3500 contre elle, son meilleur match avec celui contre RANDOM. C'est ce qui permet à ALL-D de rester 3e alors qu'elle fait environ 2000 contre tous les autres.

En résumé, à l'étape 1 TFT perdait parce qu'elle n'avait personne avec qui coopérer. Avec deux gentilles en plus, les stratégies qui coopèrent passent devant, mais celle qui gagne est celle qui sait aussi punir pour de bon ceux qui trahissent (GRIM).

## Impasses

Les scores sont rangés par nom de stratégie, donc si je mets deux fois la même stratégie dans un tournoi, leurs scores s'additionnent (pas grave pour l'instant, j'ai une seule instance de chaque).
