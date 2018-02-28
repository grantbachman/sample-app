from setuptools import setup


def get_requirements():
    with open('requirements.txt') as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]


setup(
    name='sample-app',
    include_package_data=True,
    setup_requires=['pytest-runner'],
    install_requires=get_requirements(),
    tests_require=['pytest']
)
