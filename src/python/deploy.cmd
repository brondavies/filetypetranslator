@echo off
setlocal
set path=%path%;C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64

::cleanup
del /Q dist\*.*

::Requirements
::python -m pip install --user --upgrade setuptools twine wheel
::python -m pip install --upgrade packaging
py -m pip install --upgrade build
py -m build
::These commands require the user name and password for your pypi accounts (test and prod are different accounts)
::TEST
::python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
::PROD
py -m twine upload dist/*

endlocal