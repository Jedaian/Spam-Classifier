svm = SVC()
svm.fit(x_train_tfidf, y_train)

prediction_svm = svm.predict(x_test_tfidf)
accuracy_svm = accuracy_score(y_test, prediction_svm)
print(f"SVM Classifier Accuracy: {accuracy_svm*100}")

conf_matrix = confusion_matrix(y_test, prediction_svm)

sb.heatmap(conf_matrix, annot=True, fmt="d", cmap="crest")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix - SVM")
plt.show()

import pickle

with open('/Users/jedai/Desktop/Data Science Projects/Spam Classifier/model_spam.pkl','wb') as f:
    pickle.dump(svm,f)