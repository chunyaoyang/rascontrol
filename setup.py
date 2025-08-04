from setuptools import setup

setup(
      name='rascontrol',
      version='0.15',
      description='Control RAS using win32 COM objects', 
      author='Mike Bannister, Chun-Yao Yang',
      author_email='mikebannis@gmail.com, cyyang411@gmail.com',
      packages=['rascontrol'],
      install_requires=[
            "psutil",
            "pywin32",
            "pytest"
      ]
)
