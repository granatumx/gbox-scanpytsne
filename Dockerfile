FROM granatumx/gbox-py-sdk:1.0.0

RUN pip install scanpy==1.4.6
RUN pip install cmake
RUN pip install scikit-learn

COPY . .

RUN ./GBOXtranslateVERinYAMLS.sh
RUN tar zcvf /gbox.tgz package.yaml yamls/*.yaml
