#!/usr/bin/env bash



mongoexport --type=csv --fieldFile 2.log -d ejinsui -c company_info -o test.csv