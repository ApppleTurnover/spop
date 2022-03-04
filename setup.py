from setuptools import find_packages, setup

setup(
    name='spop',
    version='0.1.0',
    description='Selenium Page Objer Pretty framework',
    author='AthonD',
    license='MIT',
    install_requires=[
    ],
    setup_requires=[
        'pytest-runner==6.0.0'
    ],
    tests_require=[
        'pytest==7.0.1'
    ],
    test_suite='tests',
    packages=[
        'spop'
    ],
)
