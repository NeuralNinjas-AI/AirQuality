************************************************
ACRONYMES
************************************************

- OIG/ IGO = Organisation intergouvernementale / Intergovernmental organization. Dans la description de nos fichiers, OIG est utilisé pour désigner les différentes organisations intergouvernementales relevant de la gouvernance climatique internationale (voir ci-dessous pour la liste complète des institutions en question) et que nous souhaitons représenter à travers un corpus composé des rapports publiés par ces dernières sur le sujet du changement climatique. 

- MEDIA/ Press = mobilisés pour désigner les données relevant du corpus journalistique, décrit ci-dessous.

- ONG/ NGOs = Organisation non-gouvernementale/ Non-governmental Organization

- CT = Candidat-terme

- UC = Unité composée

- US = Unité simple

- FR = Fréquence

- FR_rel = fréquence relative

- FR_ex = fréquence attendue

***********************************************
COMMENT LES DONNEES ONT-ELLES ETES COLLECTEES ?
***********************************************

Toutes les données ont été collectées à partir des différents corpus présents sur l'espace « Climate discourses ». Pour l'extraction des termes, nous avons utilisé la fonction « spécificités » du logiciel de textométrie TXM et avons conservé les candidats-termes présentant un score de spécificité supérieur à 3.09 (Drouin 2003). Pour les tableurs « IDFxspé_ONG », « IDFxspé_OIG » et « TGC ONGvs.OIG », c'est le logiciel TermoStat (ibid.) qui nous a permis d'extraire les unités terminologiques. Le corpus de référence avec lequel nos corpus spécialisés ont été confrontés pour obtenir ce score de spécificité est un extrait du Corpus of Contemporary American English (COCA) de plus de 12 millions de mots et représentant des genres divers (magazines grand public, blogs et autres pages web, fictions, articles de presse, sous-titrages de films et de programmes télévisés et textes académiques), choix motivé par le fait que ce corpus a été constitué pour être représentatif d’une variété d’anglais général (l’anglais américain), et parce que l’extrait en question est librement et gratuitement téléchargeable sur le site web dédié au COCA. Nous avons ensuite éliminé les candidats-termes ne répondant pas aux critères décrits par Bureau (2023 : en préparation) et avons catégorisé les unités restantes selon qu'elles relèvent des couches terminologiques 1, 2 ou 3 (ibid.). 


Pour l'extraction des cooccurrents, nous avons utilisé la fonction dédiée sur TXM (logiciel de textométrie). Les seuils de spécificité et de fréquence pour sélectionner les cooccurrents ont été fixés à 2, tandis que la fenêtre de mots à droite et à gauche du terme pivot était de 10. 



**********************************************************************
Tableurs « UC_Experts », « US_Experts », « UC_Presse », « US_Presse »
**********************************************************************

Ces tableurs proposent une perspective diachronique sur les termes mobilisés par l'expertise climatique (représentée par les institutions onusiennes (corpus OIG) et par les ONG internationales (corpus ONG)) et par la presse (corpus presse). Les termes ont en effet été extraits à partir des différents sous-corpus diachroniques (COP 15, COP 21 et COPs 25/ 26) experts (les sous-corpus relatifs aux corpus plus larges « OIG » et « ONG » ont été fusionnés) et « Presse » respectivement, de façon à pouvoir observer la variation terminologique au cours de la période ainsi représentée. Les colonnes « X2 » et « X2 COP15-21 » permettent de rendre compte de la significativé de la variation des fréquences sur toute la période et entre les deux premières COPs respectivement, tandis que la colonne « FILTRE X2+FR » permet d'identifier celles pour lesquelles le score du X2 sur toute la période est supérieur à 9,21 (cela signifie qu’il y a moins d’une chance sur 100 que la variation observée soit liée à l’écart de taille entre les différents sous-corpus diachroniques) et totalisant au moins 30 occurrences dans l'ensemble du corpus, seuil utilisé par Picton (2009 : 116-117) pour garantir l'applicabilité du score du X2. 

La colonne « RUPTURE FR » correspond à des termes qui sont absents d’un ou de plusieurs des sous-corpus composant le corpus diachronique au sein duquel ces empreintes sont observées : cet indice peut en effet permettre de repérer des candidats-néologismes (en vert: qui seraient apparus autour de la COP 21, en bleu : qui seraient apparus autour des COPs 25/ 26) ou des unités potentiellement obsolètes (en rose : qui auraient perdu en importance autour à partir de la COP 21, en violet : qui auraient perdu en importance à partir des COPs 25/ 26), qui correspondent en ce sens à des termes absents du ou des sous-corpus les plus anciens et dont la fréquence est dès lors de zéro dans ces derniers (Picton 2009).  

*******************************************
Tableurs « IDFxspé_ONG » et « IDFxspé_OIG »
*******************************************

Ces deux tableurs présentent l'ensemble des unités respectivement extraites des corpus ONG et OIG et fournit 1/ le score de Fréquence inverse de document des unités en question en pourcentage (les scores ont été inversés afin que les plus élevés correspondent aux unités les plus répandues et non l'inverse) (colonne : « IDF (sur 100) », 2/ l'indice de spécificité (en pourcentage) et la fréquence des unités pour lesquelles cet indice est supérieur à 3,14 (seuil de spécificité par défaut de TermoStat) (colonne : « INDICE (sur 100) »), 3/ le produit du score IDF sur 100 et de l'indice de spécificité (colonne « scoreIDFxspé »), 4/ la couche terminologique (Bureau, en préparation) des unités extraites sur TermoStat.

Pour obtenir les scores IDF, nous avons découpé nos deux sous-corpus en blocs de 500 phrases sur R : cela nous a permis d’obtenir des extraits de taille équilibrée (contrairement à un découpage qui suivrait la taille initiale de chaque rapport), et ainsi d’éviter que la présence d’un terme dans un document et le score IDF résultant pour ce terme soient influencés par la taille du document en question. Nous avons ainsi obtenu 221 blocs de phrases pour le corpus ONG, et 174 pour le corpus OIG. Nous avons ensuite calculé le score IDF de tous les mots de chaque corpus sur R, puis avons inversé les scores obtenus de façon à ce que les scores les plus élevés correspondent aux unités les plus répandues et non l’inverse. 


***************************
Tableur « TGCC_ONGvs.OIG »
***************************

Ce tableur vise à comparer la variation terminologique diastratique entre deux communautés ayant acquis le statut d'expert dans le domaine du changement climatique, à savoir les institutions onusiennes et les ONG internationales, représentées par les corpus « ONG » et « OIG » respectivement. Les données correspondent plus spécifiquement à la Terminologie Générale du Changement Climatique (Bureau 2023 : en préparation, Drouin et al. 2018) mobilisée par chacune de ces deux communautés, dans la mesure où les termes extraits sont non seulement spécifiques mais également répandus dans les corpus des ONG et/ ou des organisations intergouvernementales. Afin de rendre compte de ces deux paramètres, nous avons croisé les scores de spécificité des termes à une mesure de la Fréquence inverse des documents (Inverse Document Frequency (IDF)). Le score IDF permet en effet de classer les termes en tenant compte de leur distribution, dans la mesure où une unité qui apparaît dans un nombre important de documents obtient un score plus faible qu’une unité qui est peu répandue : pour chaque corpus, les scores IDF ont été transformés en pourcentage et ont été multipliés aux scores de spécificité (sur 100 également), afin d'obtenir un score unique. Les colonnes « scoreIDFxspé_ong » et « scoreIDFxspé_oig » rendent compte du score résultant pour les termes extraits des corpus « ONG » et « OIG » respectivement. 
Les colonnes « couche_ong » et « couche_oig » correspondent à la couche terminologique (Bureau 2023 : en préparation) de l'unité.

Par ailleurs, nous avons coloré les termes qui sont spécifiques à et davantage répandus dans l'un ou l'autre des deux corpus experts, afin de les distinguer de la terminologie partagée par ces derniers : les termes en bleu et azur sont spécifiques aux ONG, tandis que ceux en vert (foncé et clair) sont spécifiques aux organisations intergouvernementales.


**********************************************
Tableur « Circulation_Termes_Experts-Presse »
**********************************************

Ce tableur vise à identifier, parmi les unités extraites des différentes sous-corpus diachroniques « Presse », celles qui apparaissent également dans l'ensemble du corpus expert (surlignées en vert dans la colonne « Termes_Experts ») : il peut permettre de rendre compte de la circulation des termes entre les experts et la presse, et dès lors de la diffusion des connaissances des premiers aux seconds. La liste de termes « Experts » contient 2013 unités différentes si l’on inclut la couche terminologique n°3 (Bureau 2023 : en préparation), et 1939 si l’on considère uniquement les termes relevant des couches 1 et 2, qui présentent un degré de termicité (Humbley 2018) plus élevé. Nous nous appuyons sur des formules Excel pour automatiser cette procédure, ce qui nous permet de surligner les termes de la liste « experts » qui sont effectivement repris par les médias (en vert) et ainsi de les identifier plus facilement. Les unités surlignées en orange dans les différentes colonnes « MEDIA-[COP] » sont spécifiques à la presse : elles n'apparaissent pas dans la liste de termes représentant l'expertise climatique.

********************************************************
Tableurs « COOC_ONGvs.OIG » et « COOC_Presse_OIG_ONG »
********************************************************

Ces tableurs comparent les principaux cooccurrents (lemmatisés) de plusieurs termes clés du domaine du changement climatique entre différents corpus. Le tableur « COOC_ONGvs.OIG » compare les cooccurrents les plus spécifiques dans le corpus « ONG » à ceux issus du corpus « OIG ». Le tableur « COOC_Presse_OIG_ONG » compare les cooccurrents les plus spécifiques dans le corpus « Presse » à ceux issus du corpus « OIG » d'une part, et « ONG » d'autre part.

Pour l'extraction des cooccurrents, nous avons utilisé la fonction dédiée sur TXM (logiciel de textométrie). Les seuils de spécificité et de fréquence pour sélectionner les cooccurrents ont été fixés à 2, tandis que la fenêtre de mots à droite et à gauche du terme pivot était de 10. Nous avons également sélectionné le critère « lemma » pour notre requête. Nous avons ensuite nettoyé le haut des listes des cooccurrents ainsi extraits (triées par ordre décroissant du score de spécificité), dans la mesure où nous ne souhaitions analyser que les 30 cooccurrents les plus spécifiques dans chaque corpus pour nos travaux : nous avons ainsi supprimé les prépositions, les articles et les signes de ponctuation.

Dans ces tableurs, la colonne « CoFréquence » correspond au nombre de fois où le cooccurrent apparaît avec le terme pivot dans le corpus correspondant, tandis que la colonne « Indice » correspond au score de spécificité du cooccurrent dans le corpus en question.


****************************
Tableur « Cosine_ONG_OIG »
****************************

Les données de ce tableur correspondent aux scores de similarité cosinus entre les versions "OIG" et "ONG" des termes les plus spécifiques et les mieux distribués dans les discours sur le changement climatique produits par ces deux communautés. Les scores ont été obtenus en utilisant la fonction word2vec_similarity() du package "word2vec" sur R après avoir extrait les plongements de mots des deux corpus représentant chacun une de ces deux communautés (les corpus "OIG" et "ONG" du dossier "climate-discourse"). La colonne “rang" correspond au classement du terme concerné en fonction de son score de similarité cosinus par rapport à celui de tous les autres termes de la liste : ainsi un rang de deux pour le terme temperature rise signifie que la version OIG de ce terme est le deuxième voisin sémantique le plus proche de sa version ONG.



************
Références
************

Bureau, Pauline. 2023. « Variation terminologique et néologie dans le domaine du changement climatique ». Thèse de doctorat en Etudes anglophones, Université Grenoble Alpes. (en préparation)

Drouin, Patrick. 2003. « Term Extraction Using Non-Technical Corpora as a Point of Leverage ». Terminology 9/ 1, 99–117.

Drouin, Patrick, Marie-Claude L’Homme & Benoît Robichaud. 2018. « Lexical Profiling of Environmental Corpora ». Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018) [En ligne]. Miyazaki (Japon) : European Language Resources Association (ELRA), 3419–25. URL : <https://aclanthology.org/L18-1539.pdf>.

