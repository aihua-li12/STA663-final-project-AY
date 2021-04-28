from setuptools import setup

setup(name='SSVD',
      version='0.1',
      description='SSVD algorithm for biclustering',
      author='Aihua Li, Yuxuan Chen',
      author_email='yc450@duke.edu',
      packages=['SSVD'],
      url='https://github.com/YuxuanMonta/STA663-final-project-AY',
      classifiers=[
                  'Intended Audience :: Developers',
                  'Topic :: Software Development :: Libraries :: Python Modules',
                  'License :: OSI Approved :: MIT License',
                  'Programming Language :: Python :: 3',
                  ],
      package_dir={"": "src"},
      packages=setuptools.find_packages(where="src"),
      python_requires=">=3.6",
      zip_safe=False)

