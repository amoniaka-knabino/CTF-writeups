# EKOPARTY CTF 2019 – Thirsty

* **Category:**  Misc

## Challenge

> You get a .docx file and need to find a flag.

## Solution

unzip documento.docx -d documento_extracted
cd documento_extracted/docProps
cat secret.xml | tail -n 1