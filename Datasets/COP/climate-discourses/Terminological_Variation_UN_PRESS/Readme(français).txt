************************************************
ACRONYMES
************************************************

- UN = Nations Unies (United Nations). Dans la description de nos fichiers, UN est utilisé pour désigner les différentes institutions rattachées aux Nations Unies ayant travaillé sur le sujet du changement climatique (voir ci-dessous pour la liste complète des institutions en question) et que nous souhaitons représenter à travers un corpus composé des rapports publiés par ces dernières. 

- MEDIA/ Press = mobilisés pour désigner les données relevant du corpus journalistique, décrit ci-dessous.

***********************************************
COMMENT LES DONNEES ONT-ELLES ETES COLLECTEES ?
***********************************************

Toutes les données ont été collectées en comparant deux corpus spécialisés sur le sujet du changement climatique, l'un représentant la presse généraliste britannique et américaine, l'autre les principales institutions de l'ONU ayant travaillé sur cette thématique (voir ci-dessous pour une description des corpus).

Pour obtenir les scores de similarité cosinus, nous avons tout d'abord construit deux modèles avec l'algorithme word2vec sur R (un pour chaque communauté de discours), en utilisant la méthode CBOW (Continuous Bag Of Words) pour récupérer les vecteurs. La taille de la fenêtre a été fixée à 5 et la taille du vecteur à 300. Nous avons ensuite réduit les matrices résultantes au vocabulaire partagé par les deux communautés de discours, lequel a également pour caractéristique d'être bien distribué dans les deux corpus correspondants et d'être spécifique dans le domaine du changement climatique. Après cela, les deux matrices ont été alignées pour garantir la comparabilité spatiale (Analyse de Procrustres). Enfin, nous avons calculé les scores de similarité cosinus entre les versions UN et MEDIA de chaque terme dans la liste résultante, en utilisant la fonction word2vec_similarity() sur R.

Pour l'extraction des cooccurrents, nous avons utilisé la fonction dédiée sur TXM (logiciel de textométrie). Les seuils de spécificité et de fréquence pour sélectionner les cooccurrents ont été fixés à 2, tandis que la fenêtre de mots à droite et à gauche du terme pivot était de 10. 


************************************************
CARACTERISTIQUES DES CORPUS
************************************************

• Le corpus journalistique (désigné par l'expression "Press_corpus" dans le jeu de données) contient des articles publiés entre 2007 et 2021 par la presse généraliste britannique et américaine sur le sujet du changement climatique. Il s'agit d'articles authentiques et complets, publiés en ligne. Les journaux représentés sont le Financial Times, le New York Times, USA Today, le Guardian, et le Telegraph. Les articles ont été collectés su Europress, à partir de la requête suivante : 

TEXT= ("climate change"  | "climate action"  | "climate crisis"  | "climate response"  | "climate resilience"  | "climate devastation"  | "climate justice"  | "climate plan"  | "global warming"  | "global heating" | “climate deal” |  “climate mitigation”  | "greenhouse effects") >1
& TIT_HEAD= (climate+ | "global warming" | "global heating"  |  "greenhouse effect" | IPCC | temperature+ )

Cette dernière permet de récupérer des documents contenant plus d'une occurrence d'au moins un des mots-clés suivants : "climate deal”, “climate mitigation”, “climate action”
 “climate crisis”, “global heating”, “climate action”, “climate justice”, “climate devastation”, “climate plan”, “climate response”, “climate resilience”, “climate agreement”. Ils contiennent également une référence directe (« climate » compounds, "global warming", "global heating", "greenhouse effect") ou indirecte ("temperature", "IPCC") au changement climatique dans leur titre. Le corpus résultant contient 1 363 183 mots et 1 433 articles.

• Le corpus « UN » contient des rapports sur le sujet du changement climatique et publiés entre 2007 et 2021 par les institutions onusiennes ayant travaillé sur cette thématique, en l'occurrence la CCNUCC (Convention-cadre des Nations unies sur les changements climatiques), le GIEC (Groupe d’experts intergouvernemental sur l’évolution du climat), le PNUD (Programme des Nations unies pour le développement), le PNUE (Programme des Nations unies pour l’environnement), l'ONU (Organisation des Nations unies), le FENU (Fond d’équipement des Nations unies), l'OMM (Organisation météorologique mondiale), la Banque mondiale, et l'ONU-REDD (le Programme des Nations Unies pour la réduction des émissions liées à la déforestation et à la dégradation des forêts dans les pays en développement).Ces institutions ont été choisies parce qu'elles ont toutes publié au moins un rapport sur le changement climatique au cours de la période à l'étude. En fait, tous les rapports publiés par ces organisations sur cette thématique ont été intégrés au corpus. Les rapports ont été téléchargés à partir des sites officiels des différentes institutions et sont authentiques et complets : seuls ont été supprimés les schémas, références, images, et tableaux, afin de permettre l'analyse numérique du corpus par des logiciels de traitement automatique. Le corpus UN contient 1 217 351 words et 48 rapports. Remarque: le nombre de documents dans ce corpus est bien inférieur à celui du corpus journalistique, dans la mesure où les rapports sont beaucoup plus longs que les articles de presse (ils contiennent généralement entre 50 et 100 pages).

