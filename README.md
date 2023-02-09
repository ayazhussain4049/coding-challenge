# Python coding-challenge

This program loads _.graphml_ file and calculates cost of a network according to given rate cards.

### Calculating cost for network
To calculate cost of the network, _.graphml_ file i.e., [problem.graphml](problem.graphml) , **main** file can be run as following.

* Provide _.graphml_ file in  [main.py](main.py) file.
```python
# providing graphml file.
graph_file = 'problem.graphml'
```

* Run [main.py](main.py) file.
```cmd
python main.py
```

* Output sample for the given file.
```cmd
Rate Card A cost: £42200
Rate Card B cost: £52400"
```

### Unit tests.
*   [test_cost_calculator.py](test_cost_calculator.py) contains all the unittests and uses [test.graphml](test.graphml) as a test data. 
```cmd
python test_cost_calculator.py
```