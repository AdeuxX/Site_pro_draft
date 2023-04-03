from sklearn.neural_network import MLPClassifier
import sklearn
import numpy as np
import matplotlib.pyplot as plt
import jsonpickle,json
from main import number_into_champion
import pickle
with open("data_x_lpl.json","r") as file:
    data_x_json = jsonpickle.decode(file.read())
    data_x = np.array(data_x_json)

with open("data_y_lpl.json","r") as file:
    data_y_json = jsonpickle.decode(file.read())
    print(len(data_y_json))
    data_y = np.array(data_y_json)

split_index = int(len(data_x) * 0.90)
data_x_train,data_x_test =np.split(data_x, [split_index])

split_index = int(len(data_y) * 0.90)
data_y_train,data_y_test = np.split(data_y, [split_index])
# x_train = []
# y_train = []
# x = []
# y=[]
# nbr = 1000
# for i in range (0,nbr):
#     arr1 = np.random.choice(5, size=4, replace=False) + 1
#     arr2 = np.setdiff1d(np.arange(1, 6), arr1)
#     x_train.append(arr1)
#     y_train.append(arr2)
#
# x_train = np.array(x_train)
# y_train = np.array(y_train)
# y_train = y_train.reshape(nbr)

# print(clf.predict_proba([[1.,4.,3.,2.]]))
# for i in range (0,30):
#     arrr1 = np.random.choice(5, size=4, replace=False) + 1
#     arrr2 = np.setdiff1d(np.arange(1, 6), arrr1)
#     x.append(arrr1)
#     y.append(arrr2)
# x = np.array(x)
# y = np.array(y)
# y = y.reshape(30)
clf = pickle.load(open("model.sav", 'rb'))
# clf = MLPClassifier(solver='lbfgs',max_iter=10000, alpha=1e-5,hidden_layer_sizes=(100, 100), random_state=1)
# clf.fit(data_x_train, data_y_train)
test = clf.predict([[1,60,3,5]])
if str(test) == str(data_y_test):
    print("good")
else:
    print("sad")
test = test.tolist()
data_y_test = data_y_test.tolist()
test_name = []
for i in test:
    name_champ = number_into_champion(i)
    test_name.append(name_champ)
data_y_test_name = []
for i in data_y_test:
    name_champ = number_into_champion(i)
    data_y_test_name.append(name_champ)
for u in range (len(test)):
    print(test_name[u],data_y_test_name[u])
print(data_y_test_name,test_name)
pickle.dump(clf, open("model2.sav", 'wb'))
# # , [5.,4.,2.,3.]])
['heimerdinger', 'heimerdinger', 'yuumi', 'yuumi', 'lulu', 'nami', 'karma', 'yuumi', 'nami', 'yuumi', 'nami', 'yuumi', 'nami', 'yuumi', 'nami', 'nami', 'ashe', 'nami', 'karma', 'lux', 'yuumi', 'ashe', 'heimerdinger', 'yuumi', 'lulu', 'yuumi', 'nami', 'lulu', 'lux', 'yuumi', 'nami', 'nami', 'yuumi', 'nami', 'yuumi', 'yuumi', 'nami', 'yuumi', 'nami', 'heimerdinger', 'leona', 'karma', 'lulu', 'lulu', 'yuumi', 'nami', 'lulu', 'heimerdinger', 'lux', 'renata glasc', 'blitzcrank', 'lux', 'nautilus', 'lulu', 'yuumi']
['karma', 'nautilus', 'karma', 'nautilus', 'nautilus', 'nami', 'nami', 'renata glasc', 'heimerdinger', 'varus', 'nami', 'lulu', 'heimerdinger', 'lulu', 'nami', 'karma', 'nami', 'nami', 'heimerdinger', 'lux', 'annie', 'kalista', 'renata glasc', 'ashe', 'rakan', 'miss fortune', 'annie', 'karma', 'rakan', 'annie', 'karma', 'nami', 'ashe', 'nami', 'ashe', 'leona', 'heimerdinger', 'renata glasc', 'nami', 'yuumi', 'nautilus', 'lulu', 'blitzcrank', 'annie', 'miss fortune', 'nami', 'rakan', 'nautilus', 'nami', 'rakan', 'annie', 'renata glasc', 'lulu', 'soraka', 'caitlyn']