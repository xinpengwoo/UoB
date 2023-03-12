# Split the data into training, validation, test sets
def split_data(DA, seed=2443250962):
    np.random.seed(seed)
    # Randomise the data order
    D = np.random.permutation(DA)
    # Split the data into folds
    Folds = np.array_split(D,3)
    # Assign the Folds to train, validate, test sets and sort (not necessary)
    Folds[0].argsort()
    Folds[1].argsort()
    Folds[2].argsort()
    TrainData = {'x': Folds[0][:,0].reshape((-1,1)), 't': Folds[0][:,1].reshape((-1,1))}
    ValidateData = {'x': Folds[1][:,0].reshape((-1,1)), 't': Folds[1][:,1].reshape((-1,1))}
    TestData = {'x': Folds[2][:,0].reshape((-1,1)), 't': Folds[2][:,1].reshape((-1,1))}
    return TrainData, ValidateData, TestData