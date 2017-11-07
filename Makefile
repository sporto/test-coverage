run:
	python -c 'import app; print app.run()'

test:
	nosetests --with-coverage --cover-erase --cover-package ./