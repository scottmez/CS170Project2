from cmath import inf
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

    return twoDlist
    

def accuracy(data, current_set, feature_to_add): 
    data_entries = len(data)
    number_correctly_classified = 0
    for i in range(data_entries): #Prof said loop over number of features, but looping over data points makes more sense here?
        object_to_classify = data[i][1:] #loop above worked
        label_object_to_classify = data[i][0]

        #print("Looping over i, at the", i, "location")
        #print("The", i,  "-th object is in class", label_object_to_classify)


        nearest_neighbor_distance = inf
        nearest_neighbor_location = inf
        for k in range(data_entries):
            if (k != i): #avoid comparing to self
                #print("Ask if", i, "is nearest neighbor with", k)
                distance = np.sqrt(np.sum((object_to_classify - data[k][1:])**2)) #compute euclidean distance
                if (distance < nearest_neighbor_distance):
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = k
                    nearest_neighbor_label = data[nearest_neighbor_location][0]
        #print("object", i, "is class", label_object_to_classify)
        #print("Its nearest_neighbor is", nearest_neighbor_location, "which is in class", nearest_neighbor_label)
        if (label_object_to_classify == nearest_neighbor_label):
            number_correctly_classified += 1
    return number_correctly_classified/data_entries

def main():
    data = loaddata('small-test-dataset.txt') #get data
    #current set is set of features being used
    #feature to add is the (only one) feature we are thinking about adding

    #some ideas from prof:
    # * set unused columns to zeros
    # * "squeeze" data/ use a smaller version of dataset

    current_set = set([1,4,7]) #features 1,4,7
    feature_to_add = 10 #int representing single feature

    print("accuracy:",accuracy(data, current_set, feature_to_add))


if __name__ == "__main__":
    main()

    