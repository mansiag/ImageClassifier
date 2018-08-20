import numpy as np
from PIL import Image

X = np.empty((12000,4096))
y = np.empty((12000,1))

#unrolling images into dataset
for i in range(6000):
    image = Image.open('./mario_images/{}.png'.format(i+1))
    x = np.array(image)
    x = x.flatten()
    X[i] = x
    y[i] = 1
    
for i in range(6000,12000):
    image = Image.open('./wario_images/{}.png'.format(i-5999))
    x = np.array(image)
    x = x.flatten()
    X[i] = x
    y[i] = 0

#split dataset between test and train dataset
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 29)

#perform feature normalization
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
X_test2 = sc.transform(X_test2)

#Model training
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

#Prediction on Test data set
y_pred = classifier.predict(X_test)

#create confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)





    

