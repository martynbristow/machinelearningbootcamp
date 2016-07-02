#!/bin/sh


if [[ $1 == "install" ]]; then
    pip install Plotly
    pip install keras
    pip install matplotlib
    pip install numpy
    pip install scikit-learn
    pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git
    git clone https://github.com/cambridgecoding/machinelearningbootcamp.git
    curl https://github.com/Itseez/opencv/archive/2.4.13.zip
elif [[ $1 == "notebook" ]]; then
    # Run a jupyter notebook server
    jupyter notebook
    #--ip=0.0.0.0
    #!/bin/sh
elif [[ $1 == "build" ]]; then
    docker build notebook
elif [[ $1 == "run" ]]; then
    docker run --rm -it -p 8888:8888 -v "$(pwd):/notebooks" notebook
fi