# Tutorial Build Your Develop Environment and Contribute



## Pipeline in Shifu

![Shifu Pipeline](../images/pipline/pipline.png)

This picture shows Shifu's whole pipeline and just do some json configurations, whole pipeline will be executed and later you can get your first ML model.

## How to Install pyshifu

The easiest way to install pyshifu is using pip:     
```bazaar
pip install pyshifu
```
or use conda:         
```bazaar
conda install pyshifu
```

## How to Run Shifu Pipeline

Shifu will parse your Hadoop platform settings and set all Hadoop conf for Shifu runtime. 

* import shifu
    ```
    from pyshifu import shifu
    ```

* shifu new    
    ```
    >>> shifu.new("new_model", "/Users/haifwu/Model")
    ```
    shifu.new(model_name, work_directory)
    parameters: 
        model_name: the name of the new model
        work_directory: the new model will be created under this work directory
  
* shifu init
    ```
    >>> shifu.init()
    ```

* shifu stats
    ```
    >>> shifu.stats()
    ```

* shifu norm
    ```
    >>> shifu.norm()
    ```
     
* shifu varsel
    ```
    >>> shifu.varsel()
    ```

* shifu train
    ```
    >>> shifu.train()
    ```
    
* shifu eval
    ```
    >>> shifu.eval()
    ```

     
     * Evaluation supports multiple evaluation data set setting.
     * evals::dataSet: most time are the same as the ones in dataSet part
     * evals::performanceBucketNum: Bucket number to check points in final report.
     * evals::performanceScoreSelector: By default it is mean value for all bagging models.

     Evaluation results can be found in console like AUC or Gain Chart, Precision-Recal chart, and html format report can be found in evaluation local folder. Then you can get your models and model performance.
 
     
