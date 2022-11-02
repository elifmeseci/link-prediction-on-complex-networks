# Neighborhood-Based Link Prediction on PDC World Darts Championship Complex Networks

Recently, with the increase of interaction between people and widespread use of social communication tools, new complex network structures have emerged. The study of complex networks is an active field of scientific research based on experimental and topological findings of real-world networks such as biological networks, technological networks, global networks, and social networks. The structures of complex networks change over time with the formation or loss of nodes and connections. In order to reveal these changes and predict new links that may occur in the future, it is important to analyze complex network structures. The data obtained using the topological structure of the network can contain significant information about how the network will proceed in the future. In this context, link prediction is used to reveal new links that may occur in the future in complex networks. Many link prediction methods have been proposed for use in real-world networks, and these proposed methods are used in real-world networks. In this study, networks consisting of different time periods were created based on the interaction between the players and the data obtained from the matches in the world darts championship held by the Professional Darts Corporation (PDC) between 1994 and 2022. The purpose of creating networks from various time periods is to examine the impact of density of players and matches on link prediction. Neighborhood-based link prediction methods are used to predict new connections that may occur in the future in the created networks. The AUC metric was used to measure the success of the prediction results obtained. The results of the experimental studies show that neighborhood-based link prediction methods can be used to predict new links that will occur in networks created from dart championship competitions.

## Requirements
 - networkx == 2.8.5
 - pandas
 - sklearn
 - matplotlib

## Dataset
PDC World Championship data from 1994-2022 were used.

| index 	| Tournament Year 	|      Stage     	| player_1name 	| player_2name 	| player_1sore 	| player_2score 	|
|:-----:	|:---------------:	|:--------------:	|:------------:	|:------------:	|:------------:	|:-------------:	|
|   0   	|       2022      	|      FINAL     	|   Smith M.   	|   Wright P.  	|       5      	|       7       	|
|   1   	|       2022      	|   SEMI-FINALS  	|   Wright P.  	|  Anderson G. 	|       6      	|       4       	|
|   2   	|       2022      	|   SEMI-FINALS  	|   Smith M.   	|    Wade J.   	|       6      	|       3       	|
|   3   	|       2022      	| QUARTER-FINALS 	|   Price G.   	|   Smith M.   	|       4      	|       5       	|
|   4   	|       2022      	| QUARTER-FINALS 	|   Wright P.  	|    Rydz C.   	|       5      	|       4       	|

## Request Dataset



## Citation
If you use this research paper, please cite:


Meşeci, E., Ozkaynak, E., Dilmaç, M., & Ozdemir, D. (2022). PDC Dünya Dart Şampiyonası Karmaşık Ağlarında Komşuluk Tabanlı Bağlantı Tahmini. ICONDATA'22 Proceedings Book, 1, 148–153.




    @inproceedings{inproceedings,
    author = {Meşeci, Elif and Ozkaynak, Emrah and Dilmaç, Muhammet and Ozdemir, Dilara},
    volume = {1},
    year = {2022},
    pages = {148--153},
    title = {PDC Dünya Dart Şampiyonası Karmaşık Ağlarında Komşuluk Tabanlı Bağlantı Tahmini},
    booktitle = {ICONDATA'22 Proceedings Book}
    }