from distutils.core import setup, Extension

cnmrstarparser = Extension('cnmrstarparser',
                    sources = ['cnmrstarparsermodule.c'],
                    extra_compile_args=["-funroll-loops", "-O3"])

setup (name = 'cNMR-STAR Parser',
       version = '1.0',
       description = 'This is a really fast NMR-STAR parser.',
       ext_modules = [cnmrstarparser])
