from setuptools import setup,find_packages

HYPEN_E_DOT="-e ."

def get_requirements(filepath)-> list:
    requirements=[]
    with open(filepath,"r") as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="Customer Churn Analysis and Prediction",

    version="0.0.1",
    author="Debopam Dey(Pritam)",
    author_email="letsdecode2014@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    keywords=["Customer Churn","Customer Churn Prediction","Customer Churn Analysis"]

)