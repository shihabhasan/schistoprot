# SchistoProt: A Highly-Accurate Web Server for Identifying Schistosome-Specific Surface Proteins and Secretory Peptides

SchistoProt is implemented in Python and the web-server is freely accessible at http://schistoprot.bioapps.org. Currently local installation is not available. Source code and documentation are available from [GitHub](https://github.com/shihabhasan/schistoprot).

SchistoProt is a supervised machine learning based tool which uses 16 supervised machine learning techniques using Scikit-Learn to discriminate between i) surface and non-surface proteins and ii) secretory and non-secretory peptides. These 16 techniques are: 

1. [Gradient Boosting Machine (GBM)](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html)
2. [Support Vector Machine with Radial Bias Function (RBF SVM)](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC)
3. [SVMs with linear kernel (Linear SVM)](http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC)
4. [Decision Tree](http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier)
5. [Random Forest](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier)
6. [Ada Boost](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html)
7. [Gaussian Naive Bayes (GNB)](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB)
8. [Linear Discriminant Analysis (LDA)](http://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis)
9. [Ridge regression](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html)
10. [Stochastic gradient descent (SGD)](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier)
11. [Perceptron](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html#sklearn.linear_model.Perceptron)
12. [Passive aggressive](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveClassifier.html#sklearn.linear_model.PassiveAggressiveClassifier)
13. [Bernoulli Naive Bayes (BNB)](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB)
14. [Multinomial Naive Bayes (MNB)](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB)
15. [Nearest Centroid method](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveClassifier.html#sklearn.linear_model.PassiveAggressiveClassifier)
16. [Multi-layer Perceptron (MLP)](http://scikit-learn.org/dev/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier)

Generated predictions are stored in a database, which facilitates the rapid reuse of predictions without rerunning the time-consuming machine learning classifications. This saves considerabe runtime if the same sequences are uploaded multiple times, e.g. by different users. SchistoProt predictions are highly valuable for identifying genes important for host-parasite interaction and the discovery of novel drug and vaccine targets.

## Data & Source Code
The data set can be downloded from [here](http://schistoprot.bioapps.org/static/data.zip) and the source codes of SchistoProt can be found on [GitHub](https://github.com/shihabhasan/schistoprot).

## Input options
SchistoProt takes the fasta formatted text or file. File extension can be any type (eg. .txt, .fas, .fasta etc.). File extension does not have any effect on SchistoProt. SchistoProt can not predict the protein class if the protein sequence is less than 20 amino acids. 

## Output
After completing the task, a result page with a prediction table is appeared. The result is also sent by email if a valid email address is provided during data submission. The prediction table is a list of Sequence ID of test protein sequence, category prediction, score. The methods table is a list of Sequence ID of test protein sequence, name of the machine learning technique, category prediction, decision score and probability. Plots and Charts can be drawn from 'Draw Charts' section. Click on a row of the Prediction table, then click any of the buttons from 'Draw Charts' section to draw plot. 