
PROJECT WORKFLOW :

1.Trouver la Base de données

2.Transformer la BD en DataFrame

3.Comprendre la base de données:

  - head(): affiche les premières lignes de l'ensemble de la base
  - describe(): donne les statistiques par colonne de la base
  - info() : renseigne sur les types de données et sur les valeurs manquantes
  - isna().sum(): donne le total de veleurs manquantes s'il y a
  - isna().any(): par colonne renvoie valeur bool pour les valeurs manquantes

4.Visualisation de la base:

  - corr(): tableau de correlation entre les colones
   sns.heatmap(base_de_données.corr(),annot=True, linewidth=.5): graphique de la correlation

5.Definir la target & la(les) feature(s): X = features, y=target

6.Repartir la base en deux groupes : train_split(test-30%, train-70%)

7.Scaling & normalisation des données d'entrainement : X_train

  - minmaxscler ou  standardscaler : features numeriques
  - OneHotEncoder: features catégorielles (toutes variables non numeriques)
  - fit().transform()

7.Model: choix du modèle = LineaireRegression, LogistiqueRegression ou autre

8.Entrainement du modèle: .fit(X_train,y_train)

9.Evaluation du modèle: .score(X_test, y_test)

10.Condition de distribution normale des erreurs:

 - residus = y_pred - y_test
 - sns.displot(residus,kde=True) :
         - si loi normale respecté passer à la cross validation
         - sinon : voir en fonction de la target pour passer ou pas à la cross validation
10.Cross validation : .cross_val_score(X_train)

11.Generalisation du modèle si .cross_val_score(X_train) == .score(X_test, y_test)

12.Entrainemet sur l'ensemble de la base de données: .fit(X,y)

13.Enregistrement du modèle : pickle.dump(modèle, open("modèle.pkl", "wb"))
