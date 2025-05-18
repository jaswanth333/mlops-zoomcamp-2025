from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def train_data(data, *args, **kwargs):

    features = ['PULocationID', 'DOLocationID']
    target = 'duration'
    
    dicts = data[features].astype(str).to_dict(orient='records')
    
    dv = DictVectorizer()
    X = dv.fit_transform(dicts)
    y = data[target].values
    
    lr = LinearRegression()
    lr.fit(X, y)
    
    print(f"Model intercept: {lr.intercept_:.3f}")
    
    return {
        'dv': dv,
        'model': lr
    }


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
