# Transformando com PySpark

Esse projetinho contém meu estudo de PySpark.

## Build

É necessário que você baixe o 'quarto' antes em:
[Quarto](https://quarto.org/docs/get-started/)

E, infelizmente, você terá de baixar o Java SDK:

```{bash}
sudo apt install openjdk-17-jdk
```

E configurar o java_home no seu '.bashrc':

```{bash}
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH
```

Finalmente, você consegue:

```{bash}
python3 -m venv .venv
source .venv/bin/activate

pip install kagglehub pyspark jupyter matplotlib plotly
```

E, rodar..

```{bash}
quarto preview notebook.qmd
```
