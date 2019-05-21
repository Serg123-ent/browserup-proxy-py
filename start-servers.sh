#!/usr/bin/env bash
TOOLS=$(pwd)/tools
cd $TOOLS/browserup-proxy-1.1.0/bin/ && \
./browserup-proxy --port 9090 & \
cd $TOOLS && \
java -Dwebdriver.chrome.driver=chromedriver -Dwebdriver.gecko.driver=geckodriver -jar selenium-server-standalone-3.141.59.jar &
