from setuptools import setup, find_packages
setup(
        name='Spider',
        version='0.1',
        packages=find_packages('spider'),
        package_dir = {'':'spider'},
        install_requires=[
            'aiohttp==3.5.4',
            'aiosqlite==0.8.1',
            'async-timeout==3.0.1',
            'attrs==18.2.0',
            'chardet==3.0.4',
            'idna==2.8',
            'idna-ssl==1.1.0',
            'multidict==4.5.2',
            'pkg-resources==0.0.0',
            'typing-extensions==3.7.2',
            'yarl==1.3.0'],
    )
