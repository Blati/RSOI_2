from setuptools import find_packages, setup

setup(name="RSOI_2",
      version = "0.1",
      description = "RSOI Second lab using Flask",
      author = "Artem Karaulov",
      platforms = ["any"],
      license = "BSD",
      packages = find_packages(),
      install_requires = ["Flask==0.10.1", "requests==2.5.1", "wsgiref==0.1.2" ],
      )