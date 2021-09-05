import setuptools
with open('README.md','r') as f:
	long_description=f.read()

setuptools.setup(
	name='preprocess_akhil',
	version='0.001',
	author='akhil anand',
	author_email='akhilanandkspa@gmail.com',
	description='This is one shot nlp text preprocessing package',
	long_description=long_description,
	long_description_content_type='text/markdown',
	packages=setuptools.find_packages(),
	classifiers=['Programming Language :: python :: 3',
	             'License :: OSI Approved :: MIT License',
	             'Operating System :: OS Independent'],
	python_requires ='>=3.5')