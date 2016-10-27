from distutils.core import setup

setup(
        name='isdc-client',
        version='1.0',
        py_modules= ['isdcclient'],
        package_data     = {
            "": [
                "*.txt",
                "*.md",
                "*.rst",
                "*.py"
                ]
            },
        license='Creative Commons Attribution-Noncommercial-Share Alike license',
        long_description=open('README.md').read(),
        )
