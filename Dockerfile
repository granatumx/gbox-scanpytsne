FROM granatumx/gbox-py-sdk:1.0.0

RUN pip install scanpy==1.4.6
RUN pip install cmake==3.18.4
RUN pip install scikit-learn
RUN pip install MulticoreTSNE

COPY . .

RUN ./GBOXtranslateVERinYAMLS.sh
RUN tar zcvf /gbox.tgz package.yaml yamls/*.yaml
