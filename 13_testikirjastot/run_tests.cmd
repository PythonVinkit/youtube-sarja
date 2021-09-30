@Echo off
rem ajetaan skripti sen omassa kansiossa
Pushd "%~dp0"
python -m pytest --doctest-modules -vv
popd
