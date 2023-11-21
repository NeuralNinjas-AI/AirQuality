


************************************************
ACRONYMS
************************************************

- UN = United Nations. In the description of our files, UN is used to refer to the various institutions attached to the United Nations which have been working on the topic of climate change (see below for a full list of the institutions) and which we sought to represent through a corpus made of the reports published by the latter.
- MEDIA = used to refer to data pertaining to the press corpus, described below. 

***********************************************
HOW WERE THE DATA COLLECTED?
***********************************************

All the data were collected by comparing two specialized corpora dealing with climate change, one representing the US and British mainstream press, and one representing major UN institutions (see below for a description of the corpora). 

To obtain the cosine scores, we first built two Word2vec models in R (one for each discourse community) using CBOW as the method to retrieve the vectors. The window size was set at 5 and the vector size at 300. We then reduced the resulting matrices to the common vocabulary between the two corpora, which also had to be well-distributed across the corpora and specific in the domain of climate change. Next, the two matrices were aligned to allow for spatial comparability (Procrustres analysis). Finally, we calculated the cosine similarity scores between the UN and the press versions of each term in the resulting list, using the word2vec_similarity() function in R.

To obtain the collocates, we used the dedicated function in TXM (textometry software). The frequency and specificity thresholds for selecting the collocates were set at 2, while the word window was of 10 on the left and right of the node. We removed punctuations and grammatical words from the top of the resulting lists, as we wanted to observe the 30 most co-frequent lexical collocates in each list. 


************************************************
CHARACTERISTICS OF THE CORPORA 
************************************************


• The press corpus (referred to as « MEDIA corpus » in the description) is composed of articles published by the US and British mainstream press on the topic of climate change. The newspapers represented are the Financial Times, the New York Times, USA Today, the Guardian, and the Telegraph. The articles have been collected on Europress using the following keyword request :


TEXT= ("climate change"  | "climate action"  | "climate crisis"  | "climate response"  | "climate resilience"  | "climate devastation"  | "climate justice"  | "climate plan"  | "global warming"  | "global heating" | “climate deal” |  “climate mitigation”  | "greenhouse effects") >1
& TIT_HEAD= (climate+ | "global warming" | "global heating"  |  "greenhouse effect" | IPCC | temperature+ )



The latter aimed at gathering documents that contained more than one occurrence of at least one of the following keywords: "climate deal”, “climate mitigation”, “climate action”
 “climate crisis”, “global heating”, “climate action”, “climate justice”, “climate devastation”, “climate plan”, “climate response”, “climate resilience”, “climate agreement” and one direct (« climate » compounds, "global warming", "global heating", "greenhouse effect") or indirect ("temperature", "IPCC") reference to climate change in its title. The resulting corpus contains 1 363 183 words and 1 433 articles.

• The « UN corpus » contains reports on climate change published between 2007 and 2021 by the various UN institutions which have been working on that topic, namely the UNFCCC (United Nations Framework Convention on Climate Change), the IPCC (Intergovernmental Panel on Climate Change), the UNDP (United Nations Development Program), the UNEP (United Nations Environment Program), the UN (United Nations), the UNCDF (United Nations Capital Development Fund), the World Meteorological Organization (WMO), the World Bank (WB) and the UN-REDD (United Nations Collaborative Programme on Reducing Emissions from Deforestation and Forest Degradation in Developing Countries). These institutions were selected on the basis of their publishing at least one report on climate change during the period. In fact, all reports published by UN institutions around that time were included in the corpus. The reports were downloaded from the official websites of the various institutions and are authentic and complete, in spite of their lacking tables, references and figures, which have been removed for the sake of computerized analysis of the corpus.
The UN corpus contains 1 217 351 words and 48 reports. Note that the number of documents in this corpus is much lower than in the press one, as reports are much longer than press articles (they usually contain around 50 to 100 pages). 

