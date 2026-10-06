from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score

x = [
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8]
]

y = [
    "no",
    "no",
    "no",
    "no",
    "yes",
    "yes",
    "yes",
    "yes"
]

x_train,x_test,y_train,y_test = train_test_split(
    x,
    y,
    test_size=0.25,
    random_state=42
)

model = DecisionTreeClassifier()

model.fit(x_train,y_train)

predictions = model.predict(x_test)

accuracy = accuracy_score(predictions,y_test)

print("actual:", y_test)

print("prediction:", predictions)

print("accuracy:", accuracy)


matrix = confusion_matrix(y_test,predictions)

print("confusion matrix:", matrix)

precision = precision_score(
    y_test,
    predictions,
    pos_label="yes"
)

recall = recall_score(
    y_test,
    predictions,
    pos_label="yes"
)

print("precision:", precision)
print("recall :", recall)