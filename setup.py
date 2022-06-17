from distutils.core import setup
setup(
  name = 'QuestAnalyse',  
  packages = ['QuestAnalyse'],   
  version = '0.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'allow user to test the questionnaire and compare results between questionnaire',   # short description about my library
  author = 'Nina Abittan', 
  author_email = '...@gmail.com',     
  url = 'https://github.com/Sinha1111/QuestAnalyse', 
  download_url = 'https://github.com/Sinha1111/QuestAnalyse/archive/refs/tags/v_04.tar.gz',
  keywords = ['', '', ''],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
          'openpyxl',
          'pycel',
          'IPython',
          'formulas',
          'numpy',
          'matplotlib',
          'ipywidgets',
          'pathlib',
          'dataframe_image',
          'aspose.words',
          'wordcloud',
          'scipy',
          'statsmodels',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
