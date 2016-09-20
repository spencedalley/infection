Running tests on Ubuntu: 

Nosetests won't run tests in executable files, so if your tests have executable permissions just run
chmod -x $(find tests/ -name '*.py') to remove executable privlages. 

From there, you can just run `nosetests` from the top level directory run the tests.  

Or you can also run `nosetests --exe` to run the executable files without changing their permissions. 