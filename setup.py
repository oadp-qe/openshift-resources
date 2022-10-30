from setuptools import setup, find_packages

PACKAGE_NAME = "resources"

install_requires_ = [
    'pydantic',
]

if __name__ == "__main__":
    setup(
        name=PACKAGE_NAME,
        version='0.0.1',
        description='python openshift resources',
        url='https://github.com/oadp-qe/openshift-resources.git',
        author='OADP QE Team',
        package_dir={
            PACKAGE_NAME: 'src/%s' % PACKAGE_NAME,
        },
        packages=find_packages(where='src/'),
        install_requires=install_requires_,
    )

