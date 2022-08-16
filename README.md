# pytest-template
Pytest multi-stage test 




## Howto


### Setup env
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```


### Basic test
```
pytest --env=dev
```



### More test option
```
--junit-xml=result/report.xml                    <  generate junit xml report
--reruns 5 --reruns-delay 1                      <  rerun failure case.    pip install pytest-rerunfailures
--html=result/report.html --self-contained-html  <  generate html report
```
