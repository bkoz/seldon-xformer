# Transformer example

Usage test

```
sudo s2i usage seldonio/seldon-core-s2i-python3:1.7.0-dev
```

Build the transformer container image using [s2i](https://github.com/openshift/source-to-image#installation)

```
sudo s2i build . seldonio/seldon-core-s2i-python3:1.12.0-dev double-transformer:0.1
```

Run the container in the background and test it locally.
```
sudo docker run -d --rm --name "double-transformer" -p 9001:9000 double-transformer:0.1
```

Curl test
```
curl -d 'json={"data":{"ndarray":[[7.0,14.0]]}}' http://0.0.0.0:9001/transform-input

{"data":{"names":["t:0","t:1"],"ndarray":[[14.0,28.0]]},"meta":{}}
```

Client test
```
$ python container_test.py
```

Example output

```
jsonData {
  list_value {
    values {
      list_value {
        values {
          number_value: 7.0
        }
        values {
          number_value: 8.0
        }
        values {
          number_value: 9.0
        }
        values {
          number_value: 10.0
        }
      }
    }
  }
}

meta {
}
data {
  names: "t:0"
  names: "t:1"
  names: "t:2"
  names: "t:3"
  tensor {
    shape: 1
    shape: 4
    values: 14.0
    values: 16.0
    values: 18.0
    values: 20.0
  }
}
```

Clean up.
```
sudo docker stop double-transformer
sudo docker rm double-transformer
```

References

[Seldon Transformers](https://docs.seldon.io/projects/seldon-core/en/latest/python/python_wrapping_s2i.html#environment-variables)

How to re-create from scratch.

```
mkdir .s2i

echo numpy > requirements.txt
```

```
cat >> DoubleTransformer.py <<EOF
import numpy as np

class DoubleTransformer(object):

   def __init__(self):
       pass

   def transform_input(self, X, feature_names):
       X = np.array(X)
       return X * 2
EOF
```

```
cat >> .s2i/environment <<EOF
MODEL_NAME=DoubleTransformer
SERVICE_TYPE=TRANSFORMER
PERSISTENCE=0
EOF
```

