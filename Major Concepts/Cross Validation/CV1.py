from sklearn.model_selection import train_test_split, KFold, StratifiedKFold, cross_val_score
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Load dataset
data = load_iris()
X, y = data.data, data.target

# Holdout Validation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
print("Holdout Validation Accuracy:", model.score(X_test, y_test))

# K-Fold Cross-Validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)
kf_scores = cross_val_score(model, X, y, cv=kf)
print("K-Fold Cross-Validation Accuracy:", kf_scores.mean())

# Leave-One-Out Cross-Validation
from sklearn.model_selection import LeaveOneOut
loo = LeaveOneOut()
loo_scores = cross_val_score(model, X, y, cv=loo)
print("Leave-One-Out Cross-Validation Accuracy:", loo_scores.mean())

# Stratified K-Fold Cross-Validation
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
skf_scores = cross_val_score(model, X, y, cv=skf)
print("Stratified K-Fold Cross-Validation Accuracy:", skf_scores.mean())
