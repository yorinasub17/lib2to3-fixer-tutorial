import sys
from lib2to3 import refactor

infile = sys.argv[1]
fixers = ['fixer_generic']
tool = refactor.RefactoringTool(fixers, {}, explicit=True)
class_code = open(infile).read()
print tool.refactor_string(class_code, 'test')

