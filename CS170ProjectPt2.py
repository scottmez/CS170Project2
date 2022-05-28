from cmath import inf
from operator import countOf
import numpy as np
import re

def loaddata(fname):
    fn = open(fname, "r")
    #scan the first line to see how many entries per line
    #data = fn.readline().strip().split('  ')
    #num_columns = len(data)
    #print("data type", type(data))
    #print(data)
    twoDlist = list(list())
    floatlist = list()
    data = re.split('  | ', fn.readline().strip())
    floatlist = [float(x) for x in data] 
    twoDlist.append(np.array(floatlist))
    data = re.split('  | ', fn.readline().strip())
    while (data[0] != ''):
        floatlist = [float(x) for x in data] 
        twoDlist.append(np.array(floatlist))
        data = re.split('  | ', fn.readline().strip())

    return np.array(twoDlist)
    

def accuracy(data, current_set): 
    data_entries = len(data)
    if not (bool(current_set)): #check empty set
        #if empty we would always guess most common class
        n = countOf(data[:,0], 1.0)
        return max(n/data_entries,(data_entries - n)/data_entries)
    
    number_correctly_classified = 0
    for i in range(data_entries): #Prof said loop over number of features, but looping over data points makes more sense here? #loop worked
        object_to_classify = data[i, current_set] #grab features in current_set #should be like arr[[1,4,7]]
        label_object_to_classify = data[i, 0]

        #print("Looping over i, at the", i, "location")
        #print("The", i,  "-th object is in class", label_object_to_classify)


        nearest_neighbor_distance = inf
        nearest_neighbor_location = inf
        for k in range(data_entries):
            if (k != i): #avoid comparing to self
                #print("Ask if", i, "is nearest neighbor with", k)
                distance = np.sqrt(np.sum((object_to_classify - data[k, current_set])**2)) #compute euclidean distance
                if (distance < nearest_neighbor_distance):
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = k
                    nearest_neighbor_label = data[nearest_neighbor_location, 0]
        #print("object", i, "is class", label_object_to_classify)
        #print("Its nearest_neighbor is", nearest_neighbor_location, "which is in class", nearest_neighbor_label)
        if (label_object_to_classify == nearest_neighbor_label):
            number_correctly_classified += 1
    return number_correctly_classified/data_entries

def normalize_features(data):
    norms = np.linalg.norm(data[:,1:], axis = 0)
    #print("norms.shape", norms.shape)
    #print("data.shape", data.shape)
    data[:,1:] = data[:, 1:] * (norms**-1)[None,:] #data is shape 100,11 ; norms is shape (10,)
    return data

def main():
    data = loaddata('small-test-dataset.txt') #get data
    #data = loaddata('Large-test-dataset.txt')
    #current set is set of features being used
    #feature to add is the (only one) feature we are thinking about adding

    #some ideas from prof:
    # * set unused columns to zeros
    # * "squeeze" data/ use a smaller version of dataset

    #current_set = [1,15,27]
    current_set = [3,5,7] #features 
    #feature_to_add = 10 #int representing single feature

    #new_set = current_set.append(feature_to_add)\

    data = normalize_features(data)

    print("accuracy:",accuracy(data, current_set))
    #print("accuracy:",accuracy(data, list()))


if __name__ == "__main__":
    main()

    