from distutils.core import setup

setup(
  name = 'contextualbandits',
  packages = ['contextualbandits'],
  install_requires=[
   'pandas',
   'numpy',
   'scipy',
   'scikit-learn',
   'costsensitive',
   'joblib>=0.13'
],
  version = '0.1.6.3',
  description = 'Python Implementations of Algorithms for Contextual Bandits',
  author = 'David Cortes',
  author_email = 'david.cortes.rivera@gmail.com',
  url = 'https://github.com/david-cortes/contextualbandits',
  keywords = 'contextual bandits offset tree doubly robust policy linucb thompson sampling',
  classifiers = [],
)