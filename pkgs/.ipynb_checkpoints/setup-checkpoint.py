import setuptools as st

st.setup(
    name='dokr',
    version='0.1',
    author='Manpreet Padam',
    scripts=['dokr'],
    description='A Bitcoin analyzer packages',
    packages=st.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent"

    ]
)