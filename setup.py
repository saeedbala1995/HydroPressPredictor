from setuptools import setup, find_packages

setup(
    name='hydrodynamic_pressure_forecast',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'xgboost',
        'pandas',
    ],
    author='Saeed Balahang',
    author_email='saeedbalahang@gmail.com',
    description='A Python package for forecasting hydrodynamic pressure on bridge pier using XGBoost model',
)
