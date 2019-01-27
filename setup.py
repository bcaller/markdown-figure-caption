from os import path
from setuptools import setup


def readme():
    with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding="utf8") as f:
        return f.read()

setup(
    name='markdown-figure-caption',
    version='0.0.1',
    description='Add <figcaption> elements to your images',
    long_description=readme(),
    url='https://github.com/bcaller/pinyin_markdown',
    py_modules=['markdown_figure_caption'],
    packages=['markdown_figure_caption'],
    license='AGPLv3',
    author='Ben Caller',
    author_email='bcallergmai@l.com',
    keywords='markdown',
    tests_require=['pytest'],
    install_requires=['markdown>=3.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML',
        'License :: OSI Approved :: GNU Affero General Public License v3'
      ]
)
